from django.shortcuts import render
from .models import SendMssg

# Create your views here.
def index(requests):
    sendmssgs = SendMssg.objects.all().order_by("-c_date")
    return render(requests, "index.html", {"sendmssgs" : sendmssgs})