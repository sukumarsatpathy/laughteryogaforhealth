from django.shortcuts import get_object_or_404
from blogs.models import Blog
from .models import adBlock, banner, bannerImage, ContactPage, Copyright, webSettings, TermPages, pageCategory


def Blogs(request):
    all_blogs = Blog.objects.filter(status='Published').order_by('-submission_date')[:4]
    return dict(all_blogs=all_blogs)


def adBlockGen(request):
    all_adBlocks = adBlock.objects.filter(type="General", status='Published').order_by('-submission_date')[:4]
    return dict(all_adBlocks=all_adBlocks)


def adBlocksHome(request):
    all_home_adBlocks = adBlock.objects.filter(type="Home", status='Published').order_by('-submission_date')[:3]
    return dict(all_home_adBlocks=all_home_adBlocks)


def bannerHome(request):
    all_banner = banner.objects.filter(status='Published').order_by('created_date')
    all_bannerImg = bannerImage.objects.filter(banner__in=all_banner, status='Published').order_by('created_date')
    return dict(all_banner=all_banner, all_bannerImg=all_bannerImg)


def contactPageUniversal(request):
    contactPageUniversalDetail = ContactPage.objects.get(id=1)
    return dict(contactPageUniversalDetail=contactPageUniversalDetail)


def copyrightUniversal(request):
    copyrightUniversal = Copyright.objects.get(id=1)
    return dict(copyrightUniversal=copyrightUniversal)


def webSettingsUnivarsal(request):
    webSettingsUniversal = get_object_or_404(webSettings, id=1)
    return dict(webSettingsUniversal=webSettingsUniversal)


def termPageUniversal(request):
    termPage = TermPages.objects.filter(status='Published')
    return dict(termPage=termPage)


def pageCategoryUniversal(request):
    allPageCat = pageCategory.objects.filter(status='Published')
    return dict(allPageCat=allPageCat)