from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *

# Create your views here.
def posapp(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'posapp/openpos.html', context)

def itemList(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'posapp/ItemList.html', context)

def itemAdd(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/itemList')
        
    context = {'form':form}
    return render(request, 'posapp/ItemAdd.html', context)

def itemUpdate(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/itemList')
        
    context = {'form':form}
    return render(request, 'posapp/ItemUpdate.html', context)

def itemDelete(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('/itemList')

def confirm_order(request):
    if(request.method == "POST"):
        ptype = request.POST.get('payment_method')
        items = request.POST.get('complete_order')
        print(items)
        totamt = request.POST.get('total_amount')
        ord = Order.objects.create(total_amount=totamt, payment_type=ptype)

        item_fixed = items[:-1]
        stuff = item_fixed.split("-")
        for it in stuff:
            item_obj = Item.objects.get(pk=it[0])
            itprice = item_obj.getPrice()
            lt = itprice * int(it[2])
            ItemOrder.objects.create(item_id = item_obj, order_id = ord, line_total=lt, quantity=it[2])
            item_obj.depleteStock(int(it[2]))
            item_obj.save()

    return redirect('/itemList')



