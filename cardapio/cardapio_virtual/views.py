from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from cardapio_virtual.forms import ItemForm
from cardapio_virtual.models import Item
from cardapio_virtual.models import Temperatura
from django.views.decorators.csrf import csrf_exempt
import json

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
    obj_temp = Temperatura.objects.get(id=1)
    itens = Item.objects.all().order_by('-curtidas')
    return render(request,"show.html",{'itens':itens, 'temp':obj_temp})
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
        itens = Item.objects.all().order_by('-curtidas')
        return render(request,"administrator.html",{'itens':itens})
    else:
        return redirect("/show")

def like(request, id):
    item = Item.objects.get(id=id)
    item.curtidas = item.curtidas + 1
    item.save()
    return redirect("/show")

@csrf_exempt
def send_temp(request):
    if request.method == "POST":
        obj_temp = Temperatura.objects.get(id=1)
        temp_json = json.loads(request.body)
        obj_temp.temperatura = temp_json['temp']
        obj_temp.save()
        return HttpResponse("OK")

def get_temp(request):
    obj_temp = Temperatura.objects.get(id=1)
    temperatura_atual = obj_temp.temperatura
    return HttpResponse(temperatura_atual)

