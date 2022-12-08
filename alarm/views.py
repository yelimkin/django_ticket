from django.shortcuts import render
from .models import SendMssg

# Create your views here.
def index(requests):
    sendmssgs = SendMssg.objects.all().order_by("-c_date")
    return render(requests, "index.html", {"sendmssgs" : sendmssgs})

def dashboard(requests):
    boards = SendMssg.objects.all()
    return render(requests, "dashboard.html", {"boards": boards})