from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        User_name = request.POST['User_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=User_name).exists():
                messages.info(request,'User name taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email name taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=User_name, password=password1, email=email, first_name=First_name, last_name=Last_name)
                user.save();
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request, ' password not maching.')
            return redirect('register')

        return redirect('/')
    else:
        return render(request, 'register.html')


def registeration(request):
    return render(request, 'home.html')


#def login(request):
   # return render(request, 'login.html')
