from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_protect
# Create your views here.


@login_required
@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home_page")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def home_page(request):
    return render(request, 'home_page.html')
