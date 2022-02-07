from django.urls import path
import login.views

urlpatterns = [
    path('login', login.views.login, name='login'),
    path('home_page', login.views.home_page, name='home_page'),
    path('create_user', login.views.create_user, name='create_user'),
    path('update_user', login.views.update_user, name='update_user'),
    path('delete_user', login.views.delete_user, name='delete_user'),
    path('home', login.views.home, name='home'),
]