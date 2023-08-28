from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def event(request):
    all_events = Event.objects.filter(status="Published").order_by('start_date')
    context = {
        'all_events': all_events,
    }
    return render(request, 'front/events/eventList.html', context)


def eventDetail(request, slug):
    single_event = get_object_or_404(Event, slug=slug)
    single_event.views = single_event.views + 1
    single_event.save()
    related_events = Event.objects.all().order_by('-created_date').exclude(slug=slug)
    context = {
        'single_event' : single_event,
        'related_events': related_events,
    }
    return render(request, 'front/events/eventDetail.html', context)


@login_required(login_url='login')
def listEvent(request):
    all_events = Event.objects.all().order_by('-created_date')
    paginator = Paginator(all_events, 10)
    page = request.GET.get('page')
    paged_all_events = paginator.get_page(page)
    context = {
        'all_events': paged_all_events,
    }
    return render(request, 'back/event/listEvents.html', context)


@login_required(login_url='login')
def addEvent(request):
    eform = EventForm()
    if request.method == "POST":
        eform = EventForm(request.POST, request.FILES)
        if eform.is_valid():
            eform.save()
            messages.success(request, 'Your event has been published.')
            return redirect('listEvents')

    context = {
        'eform': eform,
    }
    return render(request, 'back/event/addEvent.html', context)


@login_required(login_url='login')
def editEvent(request,slug):
    obj = get_object_or_404(Event, slug=slug)
    eform = EventForm(instance=obj)
    if request.method == "POST":
        eform = EventForm(request.POST, instance=obj)
        if eform.is_valid():
            eform.save()
            messages.success(request, 'Your event has been updated.')
            return redirect('listEvents')

    context = {
        'obj': obj,
        'eform': eform,
    }
    return render(request, 'back/event/editEvent.html', context)