from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def join_meeting(request):
    return HttpResponseRedirect("https://pcadobeconnect.stanford.edu/mathcompetitionsclub")