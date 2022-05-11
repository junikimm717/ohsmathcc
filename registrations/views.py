from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from registrations.models import Registration, Contest

from django.utils.safestring import mark_safe
import markdown
import datetime

from .forms import RegisterForm

# TODO: implement GET vs POST request here (for when people actually sign up).
def contests(request):
    # TODO: change this query so that the deadline did not happen. 
    contests = Contest.objects.filter(deadline__gte=datetime.date.today()).all()
    paginator = Paginator(contests, 10)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, "registrations/contests.html", {'page_obj': page_obj})

def show_contest(request, uuid):
    contest = get_object_or_404(Contest, id=uuid)
    text = mark_safe(markdown.markdown(contest.description))
    if not request.user.is_authenticated:
        return render(request, "registrations/showcontest.html", 
                    {'contest': contest, 'text': text})
    else:
        registration = None
        invalid = False
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid() and form.cleaned_data['username'] == request.user.username:
                if form.cleaned_data['registered'] == "Y":
                    registration = True
                    Registration.objects.get_or_create(user=request.user, contest=contest)
                else:
                    registration = False
                    Registration.objects.filter(user=request.user, contest=contest).delete()
            else:
                invalid = True
        try:
            if registration is None:
                registration = Registration.objects.get(user=request.user, contest=contest)
        except Registration.DoesNotExist:
            pass
        form = RegisterForm(initial={"registered": "Y" if registration else "N"})
        return render(request, "registrations/showcontest.html", 
                    {'contest': contest, 'text': text, 'form': form, 'invalid': invalid, 'registered': registration})

@login_required
def registrations(request):
    registrations = []
    try:
        registrations = Registration.objects.filter(user=request.user).all()
    except Registration.DoesNotExist:
        pass
    paginator = Paginator(registrations, 10)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, "registrations/registrations.html", {'page_obj': page_obj})

# hardcoded URL (is an anti-pattern and needs to be fixed, corresponds to the 'login' view)
@staff_member_required(login_url="/accounts/login")
def registrations_for_contest(request, uuid):
    contest = get_object_or_404(Contest, id=uuid)
    registrations = Registration.objects.filter(contest=contest).all()
    paginator = Paginator(registrations, 25)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, "registrations/registrations_for_contest.html", 
    {'page_obj': page_obj, 'contest': contest})