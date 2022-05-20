from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import datetime
import markdown
from .forms import AvailableTimeForm
from .models import AvailableTime, Event
from .utils import NUM_PERIODS, TIME_OPTIONS

# Create your views here.
def events(request):
    query = Q(date__gte=datetime.date.today()) | Q(date__isnull=True)
    events = Event.objects.filter(query).all()
    #print(Event.objects.all()[0])
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, "times/events.html", {'page_obj': page_obj})


@login_required(login_url="/accounts/login")
def eventform(request, eventid):
    event = get_object_or_404(Event, id=eventid)
    form = AvailableTimeForm()
    errors = None
    success = False
    description = mark_safe(markdown.markdown(event.description))
    if request.method == "POST":
        avail = AvailableTimeForm(request.POST)
        if avail.is_valid():
            AvailableTime.objects.filter(user=request.user, event=event).delete()
            for t in avail.cleaned_data['times']:
                AvailableTime(user=request.user, time=t, event=event).save()
            form = AvailableTimeForm(initial={'times': avail.cleaned_data["times"]})
            success = True
        else:
            errors = True
            times = list(map(lambda x: x.time, AvailableTime.objects.filter(user=request.user, event=event)))
            form = AvailableTimeForm(initial={'times': times})
            # form needs to be populated with original values (run queries)
    else:
        times = list(map(lambda x: x.time, AvailableTime.objects.filter(user=request.user, event=event)))
        form = AvailableTimeForm(initial={'times': times})
        pass
    return render(request, "times/eventform.html", {'form': form, 
                    'errors': errors, 'success': success, 'event': event, 'description': description})


@staff_member_required(login_url="/accounts/login")
def viewtimes(request, eventid):
    event = get_object_or_404(Event, id=eventid)
    times = list(filter(lambda x : len(x[1]) != 0, [
        (
            (period, TIME_OPTIONS[period-1]), 
            AvailableTime.objects.filter(event=event, time=str(period)).all()
        )
        for period in range(1, NUM_PERIODS+1)
    ]))
    return render(request, 'times/viewtimes.html', {'times': times, 'event': event,})