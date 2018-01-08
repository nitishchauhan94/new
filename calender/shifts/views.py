from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import shifts
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .forms import ShiftForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def shift_create(request):
    form = ShiftForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Shift for the day is created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not created")
    context = {
        "form": form
    }
    return render(request, "shift_form.html", context)

def shift_detail(request,id=None): #retrieve
    instance = get_object_or_404(shifts, id=id)
    context = {
        "date": instance.date,
        "instance": instance,
    }
    return render(request,"shift_details.html",context)


def shift_list(request): #list items
    queryset = shifts.objects.all()
    queryset_list = shifts.objects.all()
    paginator = Paginator(queryset_list,30)
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(date = query)|
            Q(Day=query)|
            Q(Morning=query)
        ).distinct()
    page_request_var  = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "Date": "List",
        "page_request_var":page_request_var
        # "day": "List"
    }
    return render(request, "index.html", context)
    #return HttpResponse("<h1>List</h1>")

def shift_update(request,id=None):
    instance = get_object_or_404(shifts, id=id)
    form = ShiftForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Shift for the day is updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "date": instance.date,
        "instance": instance,
        "form": form,
    }
    return render(request, "shift_form.html", context)

def shift_delete(request,id=None):
    instance = get_object_or_404(shifts, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")

    return render(request, "index.html")