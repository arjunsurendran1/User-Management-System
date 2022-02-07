from django.urls import path
import usermanage.views

urlpatterns = [
    path('', usermanage.views.home, name='home'),
    path('home', usermanage.views.home, name='home'),
    path('register', usermanage.views.register, name='register'),

]