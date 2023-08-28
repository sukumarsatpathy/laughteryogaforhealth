from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.core.paginator import Paginator
from .models import imgCategory, imgGallery, vdoCategory, vdoGallery
from .forms import imgCategoryForm, imgGalleryForm, vdoCategoryForm, vdoGalleryForm


def pictureCL(request):
    all_categories = imgCategory.objects.filter(status='Published').order_by('-created_date')
    paginator = Paginator(all_categories, 12)
    page = request.GET.get('page')
    paged_categories = paginator.get_page(page)
    context = {
        'all_categories': paged_categories,
    }
    return render(request, 'front/gallery/pictureCL.html', context)


def pictureDetail(request, slug):
    single_category = get_object_or_404(imgCategory, slug=slug)
    all_images = imgGallery.objects.filter(category=single_category,status='Published')
    context = {
        'single_category': single_category,
        'all_images': all_images,
    }
    return render(request, 'front/gallery/pictureDetail.html', context)


@login_required(login_url='login')
def pcatList(request):
    all_category = imgCategory.objects.all().order_by('-created_date')
    paginator = Paginator(all_category, 10)
    page = request.GET.get('page')
    paged_all_category = paginator.get_page(page)
    context = {
        'all_category': paged_all_category,
    }
    return render(request, 'back/gallery/picture/categoryList.html', context)


@login_required(login_url='login')
def pcatAdd(request):
    pCatForm = imgCategoryForm()
    if request.method == "POST":
        pCatForm = imgCategoryForm(request.POST, request.FILES)
        if pCatForm.is_valid():
            pCatForm.save()
            messages.success(request, 'Your category has been published.')
            return redirect('pcatList')

    context = {
        'pCatForm': pCatForm,
    }
    return render(request, 'back/gallery/picture/categoryadd.html', context)


@login_required(login_url='login')
def pcatEdit(request,slug):
    obj = get_object_or_404(imgCategory, slug=slug)
    pCatForm = imgCategoryForm(instance=obj)
    if request.method == "POST":
        pCatForm = imgCategoryForm(request.POST, instance=obj)
        if pCatForm.is_valid():
            pCatForm.save()
            messages.success(request, 'Your image category has been updated.')
            return redirect('pcatList')

    context = {
        'obj': obj,
        'pCatForm': pCatForm,
    }
    return render(request, 'back/gallery/picture/categoryedit.html', context)


@login_required(login_url='login')
def photoList(request):
    all_photos = imgGallery.objects.all().order_by('-created_date')
    paginator = Paginator(all_photos, 10)
    page = request.GET.get('page')
    paged_all_photos = paginator.get_page(page)
    context = {
        'all_photos': paged_all_photos,
    }
    return render(request, 'back/gallery/picture/photoList.html', context)


@login_required(login_url='login')
def photoAdd(request):
    photoForm = imgGalleryForm()
    if request.method == "POST":
        photoForm = imgGalleryForm(request.POST, request.FILES)
        if photoForm.is_valid():
            photoForm.save()
            messages.success(request, 'Your photo has been published.')
            return redirect('photoList')

    context = {
        'photoForm': photoForm,
    }
    return render(request, 'back/gallery/picture/photoAdd.html', context)


@login_required(login_url='login')
def photoEdit(request,pk):
    obj = get_object_or_404(imgGallery, id=pk)
    photoForm = imgGalleryForm(instance=obj)
    if request.method == "POST":
        photoForm = imgGalleryForm(request.POST, instance=obj)
        if photoForm.is_valid():
            photoForm.save()
            messages.success(request, 'Your photo has been updated.')
            return redirect('photoList')

    context = {
        'obj': obj,
        'photoForm': photoForm,
    }
    return render(request, 'back/gallery/picture/photoEdit.html', context)


def vdoList(request):
    all_categories = vdoCategory.objects.filter(status='Published').order_by('-created_date')
    paginator = Paginator(all_categories, 12)
    page = request.GET.get('page')
    paged_categories = paginator.get_page(page)
    context = {
        'all_categories': paged_categories,
    }
    return render(request, 'front/gallery/vdoList.html', context)


def vdoDetail(request, slug):
    single_category = get_object_or_404(vdoCategory, slug=slug)
    all_videos = vdoGallery.objects.filter(category=single_category, status='Published').order_by('-created_date')
    paginator = Paginator(all_videos, 12)
    page = request.GET.get('page')
    paged_vdos = paginator.get_page(page)
    context = {
        'single_category': single_category,
        'all_videos': paged_vdos,
    }
    return render(request, 'front/gallery/vdoDetail.html', context)


@login_required(login_url='login')
def vcatList(request):
    all_category = vdoCategory.objects.all().order_by('-created_date')
    paginator = Paginator(all_category, 10)
    page = request.GET.get('page')
    paged_all_category = paginator.get_page(page)
    context = {
        'all_category': paged_all_category,
    }
    return render(request, 'back/gallery/video/vdocategoryList.html', context)


@login_required(login_url='login')
def vcatAdd(request):
    vCatForm = vdoCategoryForm()
    if request.method == "POST":
        vCatForm = vdoCategoryForm(request.POST, request.FILES)
        if vCatForm.is_valid():
            vCatForm.save()
            messages.success(request, 'Your category has been published.')
            return redirect('vcatList')

    context = {
        'vCatForm': vCatForm,
    }
    return render(request, 'back/gallery/video/vdocategoryAdd.html', context)


@login_required(login_url='login')
def vcatEdit(request,slug):
    obj = get_object_or_404(vdoCategory, slug=slug)
    vCatForm = vdoCategoryForm(instance=obj)
    if request.method == "POST":
        vCatForm = vdoCategoryForm(request.POST, request.FILES, instance=obj)
        if vCatForm.is_valid():
            vCatForm.save()
            messages.success(request, 'Your category has been updated.')
            return redirect('vcatList')

    context = {
        'obj': obj,
        'vCatForm': vCatForm,
    }
    return render(request, 'back/gallery/video/vdocategoryEdit.html', context)


@login_required(login_url='login')
def videoList(request):
    all_videos = vdoGallery.objects.all().order_by('-created_date')
    paginator = Paginator(all_videos, 10)
    page = request.GET.get('page')
    paged_all_videos = paginator.get_page(page)
    context = {
        'all_videos': paged_all_videos,
    }
    return render(request, 'back/gallery/video/videoList.html', context)


@login_required(login_url='login')
def videoAdd(request):
    videoForm = vdoGalleryForm()
    if request.method == "POST":
        videoForm = vdoGalleryForm(request.POST, request.FILES)
        if videoForm.is_valid():
            videoForm.save()
            messages.success(request, 'Your video has been published.')
            return redirect('videoList')

    context = {
        'videoForm': videoForm,
    }
    return render(request, 'back/gallery/video/videoAdd.html', context)


@login_required(login_url='login')
def videoEdit(request,pk):
    obj = get_object_or_404(vdoGallery, id=pk)
    videoForm = vdoGalleryForm(instance=obj)
    if request.method == "POST":
        videoForm = vdoGalleryForm(request.POST, request.FILES, instance=obj)
        if videoForm.is_valid():
            videoForm.save()
            messages.success(request, 'Your video has been updated.')
            return redirect('videoList')

    context = {
        'obj': obj,
        'videoForm': videoForm,
    }
    return render(request, 'back/gallery/video/videoEdit.html', context)