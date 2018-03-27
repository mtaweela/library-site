from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, get_user_model, authenticate

class Search(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control mr-sm-2 mySearchForm' , 'id': "ex2",'placeholder':"Search"}), label="", max_length=200)

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control mr-sm-2' , 'id': "ex2"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control mr-sm-2', 'id':"inputPassword2", 'placeholder':"Password"}))
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        if username and password:
            user = authenticate(username = username , password = password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control mr-sm-2' , 'id': "ex2"}))
    email = forms.EmailField(label = 'Email address', widget=forms.TextInput(attrs={'class' : 'form-control mr-sm-2' , 'id': "ex2"}))
    email2 = forms.EmailField(label = 'Confirm Email', widget=forms.TextInput(attrs={'class' : 'form-control mr-sm-2' , 'id': "ex2"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control mr-sm-2', 'id':"inputPassword2", 'placeholder':"Password"}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]
    
    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError("Emails must match")
        
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email