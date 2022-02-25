from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
from usermanage.models import UserRegistration


def create_user(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        User_name = request.POST['User_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if UserRegistration.objects.filter(username=User_name).exists():
                messages.info(request,'User name taken')
                return redirect('create_user')
            elif UserRegistration.objects.filter(email=email).exists():
                messages.info(request,'Email name taken')
                return redirect('create_user')

            else:
                user = UserRegistration.objects.create_user(username=User_name, password=password1, email=email, first_name=First_name, last_name=Last_name)
                user.save()

                reg = UserRegistration()
                reg.First_name = First_name
                reg.Last_name = Last_name
                reg.Email = email
                reg.User_name = User_name
                reg.password1 = password1
                reg.password2 = password2
                reg.user = user
                reg.save()
                messages.info(request,'user created')
                return redirect('create_user')
        else:
            messages.info(request, ' password not maching.')
            return redirect('create_user')

    else:
        return render(request, 'login.html')

