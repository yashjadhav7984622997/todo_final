from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser, UserType

class UserEditForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False, help_text='Leave empty to keep current password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    user_type = forms.ModelChoiceField(queryset=UserType.objects.all(), required=True)
    is_active = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'user_type', 'is_active']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
