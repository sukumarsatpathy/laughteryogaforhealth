from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import category, service
from .forms import categoryForm, serviceForm


def serviceDetail(request, slug):
    singleService = get_object_or_404(service, category__slug=slug, status='Published')
    context = {
        'singleService': singleService,
    }
    return render(request, 'front/pages/serviceLanding.html', context)


@login_required(login_url='login')
def serviceCategoryList(request):
    all_categories = category.objects.all().order_by('-created_date')
    paginator = Paginator(all_categories, 10)
    page = request.GET.get('page')
    paged_all_categories = paginator.get_page(page)
    context = {
        'all_categories': paged_all_categories,
    }
    return render(request, 'back/services/categoryList.html', context)


def serviceCategoryAdd(request):
    sCatform = categoryForm()
    if request.method == "POST":
        sCatform = categoryForm(request.POST, request.FILES)
        if sCatform.is_valid():
            sCatform.save()
            messages.success(request, 'Your category has been published.')
            return redirect('serviceCategoryList')

    context = {
        'sCatform': sCatform,
    }
    return render(request, 'back/services/categoryAdd.html', context)

def serviceCategoryEdit(request, pk):
    obj = get_object_or_404(category, id=pk)
    sCatform = categoryForm(instance=obj)
    if request.method == "POST":
        sCatform = categoryForm(request.POST, request.FILES, instance=obj)
        if sCatform.is_valid():
            sCatform.save()  # Save the form data into the database
            messages.success(request, 'Your category has been updated.')  # Define the message for the user
            return redirect('serviceCategoryList')  # Return the response
    context = {
        'obj': obj,
        'sCatform': sCatform,
    }
    return render(request, 'back/services/categoryEdit.html', context)


@login_required(login_url='login')
def serviceList(request):
    all_services = service.objects.all().order_by('-created_date')
    paginator = Paginator(all_services, 10)
    page = request.GET.get('page')
    paged_all_services = paginator.get_page(page)
    context = {
        'all_services': paged_all_services,
    }
    return render(request, 'back/services/serviceList.html', context)


def serviceAdd(request):
    sform = serviceForm()
    if request.method == "POST":
        sform = serviceForm(request.POST, request.FILES)
        if sform.is_valid():
            sform.save()
            messages.success(request, 'Your service has been published.')
            return redirect('serviceList')

    context = {
        'sform': sform,
    }
    return render(request, 'back/services/serviceAdd.html', context)


def serviceEdit(request, pk):
    obj = get_object_or_404(service, id=pk)
    sform = serviceForm(instance=obj)
    if request.method == "POST":
        sform = serviceForm(request.POST, request.FILES, instance=obj)
        if sform.is_valid():
            sform.save()  # Save the form data into the database
            messages.success(request, 'Your service has been updated.')  # Define the message for the user
            return redirect('serviceList')  # Return the response
    context = {
        'obj': obj,
        'sform': sform,
    }
    return render(request, 'back/services/serviceEdit.html', context)