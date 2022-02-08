from django.urls import path
import updateuser.views

urlpatterns = [
    path('show',updateuser.views.show, name='show'),
    path('edit/<int:id>', updateuser.views.edit, name='edit'),
    path('update/<int:id>',updateuser.views.update, name='update'),
    path('delete/<int:id>',updateuser.views.delete, name='delete'),
    ]
