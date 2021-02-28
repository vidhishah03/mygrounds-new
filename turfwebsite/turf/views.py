import os
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from django.contrib import messages
from .filters import Turf_ListFilter
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    cform = ContactForm()
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            cform.save()
            messages.success(
                request, 'Application sent successfully', extra_tags='alert')
            return redirect('home')
    return render(request, 'turf/landingpage.html', {'cform': cform})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# Create your views here.
def detailsform_view(request):
    form = TurfForm()
    currentuser = request.user
    user = User.objects.values_list(
        'username', flat=True).get(username=currentuser)
    if request.method == 'POST':
        form = TurfForm(request.POST, request.FILES)
        if form.is_valid():
            owner = form.cleaned_data['owner']
            form.save()
            messages.success(
                request, 'Application sent successfully', extra_tags='alert')
            return redirect('home')
    return render(request, 'registration/turfdetailsform.html', {'form': form, 'user': user})


def show_turf(request):
    display = Turf_List.objects.all()
    myFilter = Turf_ListFilter(request.GET, queryset=display)
    display = myFilter.qs
    context = {'display': display, 'myFilter': myFilter}
    return render(request, 'registration/display.html', context)


def show_contacts(request):
    Contact_show = Contact.objects.all()
    return render(request, 'turf/contact_show.html', {'Contact_show': Contact_show})


def show_myturfs(request):
    logged_in_user = request.user
    logged_in_user_posts = Turf_List.objects.filter(owner=logged_in_user)
    logged_in_user_bookings = Booking.objects.filter(username=logged_in_user)
    return render(request, 'registration/myturfs.html', {'myturfs': logged_in_user_posts, 'mybookings': logged_in_user_bookings})


class myaccountview(generic.UpdateView):
    form_class = MyAccountForm
    success_url = reverse_lazy('myaccount')
    template_name = 'registration/myaccount.html'

    def get_object(self):
        return self.request.user


class passwordchangeview(PasswordChangeView):
    form_class = passwordchangeForm
    success_url = reverse_lazy('myaccount')
    template_name = 'registration/changepassword.html'


# Create your views here.
def feedbackview(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thank you for your feedback :)', extra_tags='alert')
            return redirect('home')
    return render(request, 'turf/gallery.html', {'form': form})


def bookingview(request):
    turf_id_new = request.GET.get("turfId")
    turf = Turf_List.objects.values_list(
        'name', flat=True).get(turf_id=turf_id_new)
    number_of_turfs = Turf_List.objects.values_list(
        'num_5v5_turfs', flat=True).get(turf_id=turf_id_new)
    # return HttpResponse(turf)
    if str(request.user) != "AnonymousUser":
        currentuser = request.user
        user = User.objects.values_list(
            'username', flat=True).get(username=currentuser)

        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST, request.FILES)
            if form.is_valid():
                if request.POST.get("date") >= date.today().strftime("%Y-%m-%d"):
                    prevBookings = []
                    numberOfClashedTurfs = 0

                    # For loop going 1-3 hours behind requested startTime to check for clashes
                    for i in range(1, 4):
                        timeSplit = request.POST.get("startTime").split(":")
                        prevStartTime = str(
                            int(timeSplit[0])-i) + ":"+timeSplit[1]

                        # Previous bookings
                        preBooking = Booking.objects.filter(date=request.POST.get(
                            "date"), startTime=prevStartTime, booked_turf_name=request.POST.get("booked_turf_name"))

                        # From the previous bookings, getting total booked turf values
                        tot = sum([int(i.num_5v5) for i in preBooking])

                        bookedSlotHours = 0
                        clash = 0
                        hourSets = []

                        # To check multiple previous bookings in the same timeslot,
                        # eg) 12pm-2pm 2turfs, 12pm-1pm 1 turf
                        for j in preBooking:
                            bookedSlotHours = int(j.hours)
                            hourSets.append(bookedSlotHours)

                            # Clash logic
                            clash = (
                                int(timeSplit[0])-i + bookedSlotHours) > int(timeSplit[0])

                            # If there's a clash, getting the turfs that are already booked in the requested timeslot
                            if clash:
                                numberOfClashedTurfs += int(j.num_5v5)
                        # prevBookings.append(
                        #     [prevStartTime, tot, hourSets, clash])
                    if int(request.POST.get("num_5v5")) + numberOfClashedTurfs <= int(number_of_turfs):

                        availableTurfs = int(
                            number_of_turfs) - numberOfClashedTurfs

                        # Turfs in current slot
                        booked = Booking.objects.filter(date=request.POST.get(
                            "date"), startTime=request.POST.get("startTime"), booked_turf_name=request.POST.get("booked_turf_name"))

                        # Ignore next 2 lines
                        # currentTurf = Turf_List.objects.filter(
                        #     name=request.POST.get("booked_turf_name"))

                        # Total number of booked turfs in the requested time slot
                        totalTurfsInRequestedTimeSlot = sum(
                            [int(i.num_5v5) for i in booked])

                        # Availability condition
                        if(totalTurfsInRequestedTimeSlot + int(request.POST.get("num_5v5")) <= availableTurfs):

                            # To save the form values, below code to be uncommented
                            form.save()
                            messages.success(request, 'Booking Successfull :)',
                                             extra_tags='alert')
                            # return redirect('myturfs')

                            return HttpResponse([availableTurfs, "Available", totalTurfsInRequestedTimeSlot, "Can be booked"])
                        else:
                            return render(request, 'registration/booking.html', {'form': form, 'alert_1': True})
                    else:
                        return render(request, 'registration/booking.html', {'form': form, 'alert_2': True})

        return render(request, 'registration/booking.html', {'form': form, 'turf': turf, 'user': user})
    else:
        return redirect("login")


def editturfview(request):
    form = EditTurfForm()
    if request.method == 'POST':
        form = EditTurfForm(request.POST, request.FILES, instance=Turf_List)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Successfull :)',
                             extra_tags='alert')
            return redirect('myturfs')
    return render(request, 'turf/editturf.html', {'form': form})

    def get_object(self):
        return self.request.Turf_List
