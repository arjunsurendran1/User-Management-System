from django import forms
from usermanage.models import UserRegistration


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"
