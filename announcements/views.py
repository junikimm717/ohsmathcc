from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from announcements.models import Announcement

from django.utils.safestring import mark_safe
import markdown

# Create your views here.
def index(request):
    announcements = Announcement.objects.all()
    paginator = Paginator(announcements, 10)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, "announcements/index.html", {'page_obj': page_obj})

def show_announcement(request, uuid):
    announcement = get_object_or_404(Announcement, id=uuid)
    text = mark_safe(markdown.markdown(announcement.text))
    return render(request, "announcements/show.html", 
                {'announcement': announcement, 'text': text})
