from django.urls import path
import login.views

urlpatterns = [
    path('login', login.views.login, name='login'),
    path('home_page', login.views.home_page, name='home_page'),
path('webpage', login.views.webpage, name='webpage')]