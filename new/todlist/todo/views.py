from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .models import Shift
from .forms import ShiftForm
from django.contrib import messages

# Create your views here.


def shift_create(request):
    form  =ShiftForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Shift for the day is created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Not created")
    context = {
            "form":form
        }
    return render(request,"shift_form.html",context)


def shift_detail(request,id=None):  # retrieve
    instance = get_object_or_404(Shift,id=id)
    context={
        "date":instance.Date,
        "instance":instance,
    }
    return render(request,"shift_details.html",context)


def shift_list(request):  # list items
    queryset = Shift.objects.all()
    context = {
        "object_list":queryset,
         "date" : "List"
    }

    return  render(request,"index.html",context)
    #return HttpResponse("<h1>List</h1>")


def shift_update(request,id=None):
    instance = get_object_or_404(Shift, id=id)
    form = ShiftForm(request.POST or None , instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Shift for the day is updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "date": instance.Date,
        "instance": instance,
        "form":form,

    }
    return render(request, "shift_form.html", context)

def shift_delete(request):
    instance = get_object_or_404(Shift, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")

