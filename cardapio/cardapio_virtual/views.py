from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from cardapio_virtual.forms import ItemForm
from cardapio_virtual.models import Item
# Create your views here.
def emp(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ItemForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/administrator')
                except:
                    pass
        else:
            form = ItemForm()
        return render(request,'index.html',{'form':form})
    else:
        return redirect("/show")
def show(request):
    itens = Item.objects.all()
    return render(request,"show.html",{'itens':itens})
def edit(request, id):
    if request.user.is_authenticated:
        item = Item.objects.get(id=id)
        return render(request,'edit.html', {'item':item})
    else:
        return redirect("/show")
def update(request, id):
    if request.user.is_authenticated:
        item = Item.objects.get(id=id)
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("/administrator")
        return render(request, 'edit.html', {'item': item})
    else:
        return redirect("/show")
def destroy(request, id):
    if request.user.is_authenticated:
        item = Item.objects.get(id=id)
        item.delete()
        return redirect("/administrator")
    else:
        return redirect("/show")
def administrator(request):
    if request.user.is_authenticated:
        itens = Item.objects.all()
        return render(request,"administrator.html",{'itens':itens})
    else:
        return redirect("/show")