from django.shortcuts import render, redirect
from usermanage.models import UserRegistration
from .forms import UserUpdateForm


def show(request):
    ums = UserRegistration.objects.all
    return render(request, 'show.html', {'ums': ums})


def edit(request,id):
    ums = UserRegistration.objects.get(id=id)
    return render(request, 'update.html', {'ums': ums})


def update(request,id):
    ums = UserRegistration.objects.get(id=id)
    form = UserUpdateForm(request.POST, instance=ums)
    form.save()
    return redirect('/show')


def delete(request,id):
    ums = UserRegistration.objects.get(id=id)
    ums.delete()
    return redirect('/show')


def load_form(request):
    form = UserUpdateForm
    return render(request, "index1.html", {'form': form})


def add(request):
    form = UserUpdateForm(request.POST)
    form.save()
    return redirect('/show')


