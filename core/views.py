from django.shortcuts import render,redirect
from item.models import Category,Item
from .forms import SignupForm
from django.contrib import messages
# Create your views here.

def index(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold = False)
    return render(request,"core/index.html",
    {"category":categories,
    "item":items}
    )


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("login/")
        
    else:
        form = SignupForm()

    return render(request,"core/signup.html",{
        "form" :form
    })
    


