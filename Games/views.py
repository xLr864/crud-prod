from django.shortcuts import render, HttpResponseRedirect
from .forms import Games_Review
from .models import Product
# Create your views here.

def create_read(request):
    if request.method == 'POST':
        fobj = Games_Review(request.POST)
        if fobj.is_valid():
            T = fobj.cleaned_data['title']
            D = fobj.cleaned_data['description']
            P = fobj.cleaned_data['price']
            S = fobj.cleaned_data['summary']
            reg = Product(title=T,description=D,price=P,summary=S)
            reg.save()
        fobj = Games_Review()
    else:
        fobj = Games_Review()
    peak = Product.objects.all()
    return render(request,'Games_Frontend/create_read.html',{'form':fobj,'views':peak})

def delete_record(request,id):
    if request.method=='POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        fobj = Games_Review(request.POST,instance=pi)
        if fobj.is_valid():
            fobj.save()
    else:
        pi = Product.objects.get(pk=id)
        fobj = Games_Review(instance=pi)       
    return render(request,'Games_Frontend/update.html',{'form':fobj})
      