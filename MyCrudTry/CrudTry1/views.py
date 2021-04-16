from django.shortcuts import render, redirect
from CrudTry1.models import Laptop
from CrudTry1.forms import LaptopForm

# Create your views here.


def lap(request):
    if request.method=="POST":
        obj=LaptopForm(request.POST)
        if obj.is_valid():
            try:
                obj.save()
                return redirect('/lists')
            except:pass
    else:
        obj=LaptopForm()
    return render(request,'lap.html',{'obj':obj})

def lists(request):
    laptops=Laptop.objects.all()
    return render(request,"list.html",{'laptops':laptops})
def edit(request, id):  
    laptop = Laptop.objects.get(id=id)
    return render(request,'edit.html', {'laptop':laptop})  
def update(request, id):  
    laptop = Laptop.objects.get(id=id)  
    form = LaptopForm(request.POST, instance = laptop)  
    if form.is_valid():  
        form.save()  
        return redirect("/lists")  
    return render(request, 'edit.html', {'laptop': laptop})  
def destroy(request, id):  
    laptop = Laptop.objects.get(id=id)  
    laptop.delete()
    return redirect("/lists")