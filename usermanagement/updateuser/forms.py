from django.forms import ModelForm
from usermanage.models import UserRegistration


class UserUpdateForm(ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"
