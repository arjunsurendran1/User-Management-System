from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_protect
from usermanage.models import UserRegistration
from django.contrib.auth import authenticate, login
# Create your views here.




@csrf_protect
def login(request):
    if request.method == 'POST':
        user_type = request.POST.getlist('type')
        print(user_type)
        if user_type == ['ADMIN']:

            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("home_page")
            else:
                messages.info(request, 'invalid credentials')
                return redirect('login')
        elif user_type == ['USER']:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("webpage")
            else:
                messages.info(request, 'invalid credentials')
                return redirect('login')
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def home_page(request):
    return render(request, 'home_page.html')


def webpage(request):
    return render(request, 'webpage.html')
