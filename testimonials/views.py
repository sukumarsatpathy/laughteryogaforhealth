from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Testimonial
from .forms import TestimonialForm


def testimonial(request):
    all_testimonials = Testimonial.objects.filter(status="Active").order_by('-submission_date')
    context = {
        'all_testimonials': all_testimonials,
    }
    return render(request, 'front/pages/testimonial.html', context)


@login_required(login_url='login')
def listTestimonials(request):
    all_blogs = Testimonial.objects.all().order_by('-submission_date')
    paginator = Paginator(all_blogs, 10)
    page = request.GET.get('page')
    paged_all_blogs = paginator.get_page(page)
    context = {
        'all_blogs': paged_all_blogs,
    }
    return render(request, 'back/testimonial/listTestimonial.html', context)


@login_required(login_url='login')
def addTestimonial(request):
    tForm = TestimonialForm()
    if request.method == "POST":
        tForm = TestimonialForm(request.POST, request.FILES)
        if tForm.is_valid():
            tForm.save()
            messages.success(request, 'Your testimonial has been published.')
            return redirect('listTestimonials')

    context = {
        'tForm': tForm,
    }
    return render(request, 'back/testimonial/addTestimonial.html', context)


@login_required(login_url='login')
def editTestimonial(request, pk):
    obj = get_object_or_404(Testimonial, id=pk)
    tForm = TestimonialForm(instance=obj)
    if request.method == "POST":
        tForm = TestimonialForm(request.POST, instance=obj)
        if tForm.is_valid():
            tForm.save()
            messages.success(request, 'Your testimonial has been updated.')
            return redirect('listTestimonials')

    context = {
        'obj': obj,
        'tForm': tForm,
    }
    return render(request, 'back/testimonial/editTestimonial.html', context)
