from django.urls import path
import createuser.views

urlpatterns = [
    path('createuser', createuser.views.create_user, name='createuser'),
    path('create_user', createuser.views.create_user, name='create_user'),

    ]