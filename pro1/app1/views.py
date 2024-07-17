from django.shortcuts import render, redirect
from .models import Manangesystem
from .forms import ManageForm
from django.http import HttpResponse


def manageview(request):
    template_name = 'create.html'
    form = ManageForm
    if request.method == "POST":
        form = ManageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data field')
    context = {"form":form}
    return render(request, template_name, context)




def show(request):
    template_name = 'app1/show.html'
    obj = Manangesystem.get.all()
    form = ManageForm
    if request.method == "POST":
        form = ManageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data show")
    context = {"form": form}
    return render(request, template_name, context)


def update(request, pk):
    template_name = 'app1/create.html'
    obj = ManageForm.get.instance()
    if request.method == "POST":
        form = ManageForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse("data updated")
    context = {"form": form}
    return render(request, template_name, context)



def delete(request, pk):
    form = ManageForm
    obj = ManageForm.get.id(id=pk)
    if request.method == "Post":
        obj.delete()
        return HttpResponse("record delete")












