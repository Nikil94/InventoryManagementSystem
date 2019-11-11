from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from datetime import datetime
from . models import Profile, Products
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.CharField(help_text='From which location your from')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def extract(self):
        data = Profile.objects.all()
        usernamehere = self.cleaned_data.get("username")
        user_email = self.cleaned_data.get("email")
        dbuser = Profile.objects.filter(name = usernamehere)
        dbuser_email = Profile.objects.filter(email = user_email)
        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return TemplateResponse(request, 'templates/signup.html', {'data': data})


class ProductsForm(forms.Form):

    productid = forms.IntegerField(label='Enter ProductId')
    productname = forms.CharField(label='Enter Product Name', max_length=100)
    vendor = forms.CharField(label='Enter Vendor Name', max_length=100)
    mrp = forms.IntegerField(label='Enter MRP Value')
    batchdate = forms.DateTimeField(initial=datetime.now(), required=False)
    batchnumber = forms.IntegerField(label='Enter Batch Number')
    quantity = forms.IntegerField(label='Enter quantity')
    status_approved = forms.BooleanField()
