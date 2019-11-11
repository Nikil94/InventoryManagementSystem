# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . models import Products, Profile
from . forms import SignUpForm, ProductsForm
from django.shortcuts import render, redirect

def samplemethod(request):
    return HttpResponse("This a test message")

@login_required
def home(request):
    products = Products.objects.all()
    #profile = Profile.objects.all()
    return render(request, 'home.html', {'product': products })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            Profile.username = form.cleaned_data.get("username")
            #print("what?:", user.refresh_from_db())
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})



def addproducts(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('Your data has been submitted')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductsForm()

    return render(request, 'products_form.html', {'form': form})
