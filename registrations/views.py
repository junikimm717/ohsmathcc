from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from registrations.models import Registration, Contest

from django.utils.safestring import mark_safe
import markdown

# TODO: implement contests.html, registrations.html, and showcontest.html.
# TODO: implement GET vs POST request here (for when people actually sign up).
def contests(request):
    # TODO: change this query so that the deadline did not happen. 
    contests = Contest.objects.all()
    paginator = Paginator(contests, 10)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, "registrations/contests.html", {'page_obj': page_obj})

# show the details about a specific contest..
def show_contest(request, uuid):
    contest = get_object_or_404(Contest, id=uuid)
    text = mark_safe(markdown.markdown(announcement.text))
    return render(request, "registrations/showcontest.html", 
                {'contest': announcement, 'text': text})

# TODO: user only decorator needed
def registrations(request):
    registrations = Registrations.objects.get(user=request.user)
    paginator = Paginator(registrations, 10)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, "registrations/registrations.html", {'page_obj': page_obj})
