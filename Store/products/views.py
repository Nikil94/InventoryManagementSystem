# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from . models import Products, Profile
from django.db.models import Q
from . forms import SignUpForm, ProductsForm
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from . serializers import ProductsSerializer

def samplemethod(request):
    return HttpResponse("This a test message")

@login_required

def home(request):
        products = Products.objects.filter(user_id=request.user.id)
        #profile = Profile.objects.all()
        return render(request, 'home.html', {'product': products })

def deleteproduct(request, id):
    note = get_object_or_404(Products, productid=id).delete()
    return redirect('viewproducts')

def viewproducts(request):
    allproducts = Products.objects.all()
    return render(request, 'allproducts.html', {'allproducts': allproducts})

def updateproductstatus(request, id):
    precord = Products.objects.get(productid=id)
    precord.status_approved = 'Approved'
    precord.save()
    return redirect('viewproducts')

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
            store = form.save(commit=False)
            user = User.objects.get(id=request.user.id) #Fetching Logged In user ID from DB
            store.user_id = user #Setting LoggedIn UserID to Product table
            #store.refresh_from_db()
            store.save()
            return redirect('home')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductsForm()

    return render(request, 'products_form.html', {'form': form})


class productsview(APIView):

    def get(self, request, format=None):
        pdata = Products.objects.get(productid=request.GET['pid'])
        products = ProductsSerializer(pdata)
        return Response(products.data)

    def delete(self, request, format=None):
        res = get_object_or_404(Products, productid=id).delete()
        return redirect('viewproducts')


class allproducts(APIView):

    def get(self, request, format=None):
        pdsdata = Products.objects.all()
        serializer = ProductsSerializer(pdsdata, many=True)
        return Response(serializer.data)

#view is used for searching a feed of user and proving Sentiment Analysis to that feed based on Title
def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(productname__icontains=query) | Q(productid__icontains=query)

            results= Products.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')