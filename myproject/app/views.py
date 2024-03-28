from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = User(username=username, password=password)
        user.save()
        return redirect("/result")
    return render(req, 'index.html', {})


def result(req):
    return render(req, 'result.html', {"users":User.objects.all()})
