from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item,Category
from .forms import NewItemForm,EditItemForm
# Create your views here.
def items(request):
    query = request.GET.get("query","")
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get("category",0)

    if query:
        items = items.filter(name__icontains=query)
    if category_id:
        items = items.filter(category_id=category_id)
    return render(request,"item/items.html",{
        "items":items,
        "query":query,
        "categories":categories,
        "category_id":category_id
    })


def detail(request,pk):
    related_items = Item.objects.filter(is_sold = False).exclude(pk=pk)[0:3]
    item = get_object_or_404(Item,pk=pk)
    return render(request,"item/detail.html",{
        "item":item,
        "related_items":related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()
            return redirect("item:detail",pk=new_item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect("dashboard:index")

@login_required
def edit(request,pk):
    
    item = get_object_or_404(Item,pk=pk,created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()       
            
            return redirect("item:detail",pk=new_item.id)
 
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })