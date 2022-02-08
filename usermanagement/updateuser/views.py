from django.shortcuts import render,redirect
from usermanage.models import UserRegistration
from .forms import UserUpdateForm


def show(request):
    ums = UserRegistration.objects.all
    return render(request,'show.html', { 'ums': ums })


def edit(request,id):
    ums = UserRegistration.objects.get(id=id)
    return render(request, 'edit.html', {'ums' : ums})


def update(request,id):
    ums = UserRegistration.objects.get(id=id)
    form = UserUpdateForm(request.POST, instance=ums)
    form.save()
    return redirect('/show')


def delete(request,id):
    employee = UserRegistration.objects.get(id=id)
    employee.delete()
    return redirect('/show')