from django.urls import path
import updateuser.views

urlpatterns = [
    path('load_form', updateuser.views.load_form, name='load_form'),

    ]
