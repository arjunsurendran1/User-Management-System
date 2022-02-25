from django.urls import path
import createuser.views

urlpatterns = [
    path('createuser', createuser.views.create_user, name='createuser'),

    ]
