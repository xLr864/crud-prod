from django.shortcuts import render, HttpResponseRedirect
from .forms import Games_Review
from .models import Review
# Create your views here.

def create_read(request):
    if request.method == 'POST':
        fobj = Games_Review(request.POST)
        if fobj.is_valid():
            T = fobj.cleaned_data['title']
            R = fobj.cleaned_data['ratting']
            V = fobj.cleaned_data['verdict']
            reg = Review(title=T,ratting=R,verdict=V)
            reg.save()
        fobj = Games_Review()
    else:
        fobj = Games_Review()
    peak = Review.objects.all()
    return render(request,'Games_Frontend/create_read.html',{'form':fobj,'views':peak})

def delete_record(request,id):
    if request.method=='POST':
        pi = Review.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method == "POST":
        pi = Review.objects.get(pk=id)
        fobj = Games_Review(request.POST,instance=pi)
        if fobj.is_valid():
            fobj.save()
    else:
        pi = Review.objects.get(pk=id)
        fobj = Games_Review(instance=pi)       
    return render(request,'Games_Frontend/update.html',{'form':fobj})
      