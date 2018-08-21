from django import forms
from account.models import CustomUser

class UserRegisterForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password*')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password*')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError ('Password and Confirm Password must match')
        return confirm_password

    def save(self, commit=True):
        user= super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
# done through django documentation  https://docs.djangoproject.com/en/2.1/topics/auth/customizing/
    class Meta:
            model = CustomUser
            fields = ['first_name', 'last_name', 'email']
            labels = {
            'id': 'ID*',
            'first_name': 'First Name*',
            'last_name': 'Last Name*',
            'email': 'Email Address'}

class LoginForm (forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
