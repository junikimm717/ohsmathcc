from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AvailableTimeForm

# Create your views here.

@login_required(login_url="/accounts/login")
def scheduleform(request):
    form = None
    errors = None
    if request.method == "POST":
        avail = AvailableTimeForm(request.POST)
        if avail.is_valid():
            avail.cleaned_data["times"]
            form = AvailableTimeForm(times=avail.cleaned_data["times"])
        else:
            errors = True
            # form needs to be populated with original values (run queries)
        pass
    else:
        # form needs to be populated with original values (run queries)
        pass
    return render(request, "times/scheduleform.html", {'form': form, 'errors': errors})