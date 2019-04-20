from django import forms
from django.contrib.auth.models import User,Group
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)#inbuilt user field
    last_name = forms.CharField(max_length=30, required=True)#inbuilt user field
    email=forms.EmailField(required=True)#inbuilt user field
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password',]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username=self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user