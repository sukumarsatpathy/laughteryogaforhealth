import urllib
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import adBlock, lyJournals, banner, bannerImage, ContactPage, Copyright, webSettings, TermPages, pageCategory, AboutPage
from .forms import adBlockForm, journalForm, bannerForm, bannerImageForm, ContactPageForm, CopyrightPageForm, webSettingsForm, termPageForm
from blogs.models import Blog
from testimonials.models import Testimonial
from reports.models import Contact, Invite, Newsletter
from reports.forms import contactForm, inviteForm, newsletterForm
# Email
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def home(request):
    all_testimonials = Testimonial.objects.filter(status='Published').order_by('-submission_date')
    all_blogs = Blog.objects.filter(status='Published').order_by('-submission_date')
    all_journals = lyJournals.objects.filter(status='Published').order_by('-submission_date')
    context = {
        'all_testimonials': all_testimonials,
        'all_blogs': all_blogs,
        'all_journals': all_journals,
    }
    return render(request, 'front/pages/home.html', context)


def aboutDetailPage(request, slug):
    singlePage = get_object_or_404(AboutPage, category__slug=slug, status='Published')
    context = {
        'singlePage': singlePage,
    }
    return render(request, 'front/pages/aboutLanding.html', context)


def aboutTrainer(request):
    site_key = settings.RECAPTCHA_PUBLIC_KEY
    if request.method == 'POST':
        fullName = request.POST['fullName']
        email = request.POST['email']
        contact = request.POST['contact']
        country = request.POST['country']
        message = request.POST['message']

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            # Contact Form submission
            invite_form = inviteForm()
            invite_form.fullName = fullName
            invite_form.email = email
            invite_form.contact = contact
            invite_form.country = country
            invite_form.message = message
            form_submission = Invite.objects.create(
                fullName=invite_form.fullName,
                email=invite_form.email,
                contact=invite_form.contact,
                country=invite_form.country,
                message=invite_form.message,
            )
            form_submission.save()

            # Sending Email
            mail_subject = 'New Invite Received from ' + fullName
            message_content = {
                'fullName': fullName,
                'email': email,
                'contact': contact,
                'country': country,
                'message': message,
            }
            from_email = 'Laughter Yoga For Health <settings.DEFAULT_FROM_EMAIL>'
            to_email = (email, 'Laughter Yoga For Health <settings.DEFAULT_FROM_EMAIL>')
            html_content = render_to_string('front/email/invite-email.html', message_content)
            if fullName and email and contact and country and message:
                try:
                    send_mail(mail_subject, message, from_email, to_email, html_message=html_content)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, 'Thank you. We have received your invite.')
                return redirect('aboutTrainer')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')

        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('aboutTrainer')

    context = {
        'site_key': site_key,
    }
    return render(request, 'front/pages/about-trainer.html', context)


def contact(request):
    contactPageDetail = get_object_or_404(ContactPage, id=1)
    site_key = settings.RECAPTCHA_PUBLIC_KEY
    if request.method == 'POST':
        fullName = request.POST['fullName']
        email = request.POST['email']
        message = request.POST['message']

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            # Contact Form submission
            contact_form = contactForm()
            contact_form.fullName = fullName
            contact_form.email = email
            contact_form.message = message
            form_submission = Contact.objects.create(
                fullName=contact_form.fullName,
                email=contact_form.email,
                message=contact_form.message,
            )
            form_submission.save()

            # Sending Email

            mail_subject = 'New Enquiry Received from ' + fullName
            message_content = {
                'fullName': fullName,
                'email': email,
                'message': message,
            }
            from_email = 'Laughter Yoga For Health <settings.DEFAULT_FROM_EMAIL>'
            to_email = (email, 'Laughter Yoga For Health <settings.DEFAULT_FROM_EMAIL>')
            html_content = render_to_string('front/email/contact-email.html', message_content)
            if fullName and email and message:
                try:
                    send_mail(mail_subject, message, from_email, to_email, html_message=html_content)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, 'Thank you. We have received your enquiry.')
                return redirect('contact')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')

        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('contact')

    context = {
        'site_key': site_key,
        'contactPageDetail': contactPageDetail,
    }
    return render(request, 'front/pages/contact.html', context)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        newsletter_form = newsletterForm(request.POST)
        if newsletter_form.is_valid():
            subscribe_user = Newsletter.objects.filter(email=email).first()
            if subscribe_user:
                messages.error(request, f"{email} email address is already subscriber.")
                return redirect(request.META.get("HTTP_REFERER", "/"))
            else:
                newsletter_form.save()
                messages.success(request, 'Successfully subscribed to our newsletter!')

                # Sending Email
                mail_subject = 'Yuppie, new subscriber '
                message_content = {
                    'email': email,
                }
                from_email = 'Laughter Yoga For Health <settings.DEFAULT_FROM_EMAIL>'
                to_email = (email, 'Laughter Yoga For Health <settings.DEFAULT_FROM_EMAIL>')
                html_content = render_to_string('front/email/contact-email.html', message_content)
                if email:
                    try:
                        send_mail(mail_subject, from_email, to_email, html_message=html_content)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'Thank you. We have received your enquiry.')
                    return redirect('contact')
                else:
                    return HttpResponse('Make sure all fields are entered and valid.')
    else:
        messages.error(request, 'Don\'t act smart. Follow routine procedure')
        return redirect(request.META.get("HTTP_REFERER", "/"))


def termPage(request, slug):
    singlePage = get_object_or_404(TermPages, slug=slug, status='Published')
    context = {
        'singlePage': singlePage,
    }
    return render(request, 'front/pages/termPage.html', context)


@login_required(login_url='login')
def adblockList(request):
    all_ad_blocks = adBlock.objects.all().order_by('-submission_date')
    paginator = Paginator(all_ad_blocks, 10)
    page = request.GET.get('page')
    paged_all_ad_blocks = paginator.get_page(page)
    context = {
        'all_ad_blocks': paged_all_ad_blocks,
    }
    return render(request, 'back/adBlock/adBlockList.html', context)


@login_required(login_url='login')
def adblockAdd(request):
    adForm = adBlockForm()
    if request.method == "POST":
        adForm = adBlockForm(request.POST, request.FILES)
        if adForm.is_valid():
            adForm.save()
            messages.success(request, 'Your ad has been published.')
            return redirect('adblockList')

    context = {
        'adForm': adForm,
    }
    return render(request, 'back/adBlock/adBlockAdd.html', context)


@login_required(login_url='login')
def adblockEdit(request,pk):
    obj = get_object_or_404(adBlock, id=pk)
    adForm = adBlockForm(instance=obj)
    if request.method == "POST":
        adForm = adBlockForm(request.POST, instance=obj)
        if adForm.is_valid():
            adForm.save()
            messages.success(request, 'Your ad has been updated.')
            return redirect('adblockList')

    context = {
        'obj': obj,
        'adForm': adForm,
    }
    return render(request, 'back/adBlock/adBlockEdit.html', context)


@login_required(login_url='login')
def journalList(request):
    all_journals = lyJournals.objects.all().order_by('-submission_date')
    paginator = Paginator(all_journals, 10)
    page = request.GET.get('page')
    paged_all_journals = paginator.get_page(page)
    context = {
        'all_journals': paged_all_journals,
    }
    return render(request, 'back/journals/journalsList.html', context)


@login_required(login_url='login')
def journalAdd(request):
    jForm = journalForm()
    if request.method == "POST":
        jForm = journalForm(request.POST, request.FILES)
        if jForm.is_valid():
            jForm.save()
            messages.success(request, 'Your journal has been published.')
            return redirect('journalList')

    context = {
        'jForm': jForm,
    }
    return render(request, 'back/journals/journalsAdd.html', context)


@login_required(login_url='login')
def journalEdit(request,pk):
    obj = get_object_or_404(lyJournals, id=pk)
    jForm = journalForm(instance=obj)
    if request.method == "POST":
        jForm = journalForm(request.POST, instance=obj)
        if jForm.is_valid():
            jForm.save()
            messages.success(request, 'Your journal has been updated.')
            return redirect('journalList')

    context = {
        'obj': obj,
        'jForm': jForm,
    }
    return render(request, 'back/journals/journalsEdit.html', context)


@login_required(login_url='login')
def bannerList(request):
    all_banners = banner.objects.all().order_by('-created_date')
    #all_bannerImage = bannerImage.objects.filter(banner__in=all_banners).order_by('-created_date')
    paginator = Paginator(all_banners, 10)
    page = request.GET.get('page')
    paged_all_banners = paginator.get_page(page)
    context = {
        'all_banners': paged_all_banners,
    }
    return render(request, 'back/banner/bannerList.html', context)


@login_required(login_url='login')
def bannerEdit(request,pk):
    obj = get_object_or_404(banner, id=pk)
    bnrForm = bannerForm(instance=obj)
    if request.method == "POST":
        bnrForm = bannerForm(request.POST, instance=obj)
        if bnrForm.is_valid():
            bnrForm.save()
            messages.success(request, 'Your banner has been updated.')
            return redirect('bannerList')

    context = {
        'obj': obj,
        'bnrForm': bnrForm,
    }
    return render(request, 'back/banner/bannerEdit.html', context)


@login_required(login_url='login')
def bannerImageList(request):
    all_bannerImg = bannerImage.objects.all().order_by('-created_date')
    paginator = Paginator(all_bannerImg, 10)
    page = request.GET.get('page')
    paged_all_bannerImg = paginator.get_page(page)
    context = {
        'all_bannerImg': paged_all_bannerImg,
    }
    return render(request, 'back/banner/bannerImageList.html', context)


@login_required(login_url='login')
def bannerImageAdd(request):
    bannerImgForm = bannerImageForm()
    if request.method == "POST":
        bannerImgForm = bannerImageForm(request.POST, request.FILES)
        if bannerImgForm.is_valid():
            bannerImgForm.save()
            messages.success(request, 'Your banner image has been published.')
            return redirect('bannerImageList')

    context = {
        'bannerImgForm': bannerImgForm,
    }
    return render(request, 'back/banner/bannerImageAdd.html', context)


@login_required(login_url='login')
def bannerImageEdit(request,pk):
    obj = get_object_or_404(bannerImage, id=pk)
    bannerImgForm = bannerImageForm(instance=obj)
    if request.method == "POST":
        bannerImgForm = bannerImageForm(request.POST, request.FILES, instance=obj)
        if bannerImgForm.is_valid():
            bannerImgForm.save()
            messages.success(request, 'Your banner image has been updated.')
            return redirect('bannerImageList')

    context = {
        'obj': obj,
        'bannerImgForm': bannerImgForm,
    }
    return render(request, 'back/banner/bannerImageEdit.html', context)


@login_required(login_url='login')
def contactPageEdit(request):
    obj = ContactPage.objects.get(user=request.user)
    contactPageForm = ContactPageForm(instance=obj)
    if request.method == 'POST':
        contactPageForm = ContactPageForm(request.POST, instance=obj)
        if contactPageForm.is_valid():
            contactPageForm.save()
            messages.success(request, 'Your contact page details has been updated.')
            return redirect('contactPageEdit')
    context = {
        'contactPageForm': contactPageForm,
    }
    return render(request, 'back/settings/contactPageEdit.html', context)


@login_required(login_url='login')
def copyrightPageEdit(request):
    obj = Copyright.objects.get(user=request.user)
    copyrightPageForm = CopyrightPageForm(instance=obj)
    if request.method == 'POST':
        copyrightPageForm = CopyrightPageForm(request.POST, instance=obj)
        if copyrightPageForm.is_valid():
            copyrightPageForm.save()
            messages.success(request, 'Your copyright content has been updated.')
            return redirect('copyrightPageEdit')
    context = {
        'copyrightPageForm': copyrightPageForm,
    }
    return render(request, 'back/settings/copyrightPageEdit.html', context)


@login_required(login_url='login')
def webSettingsEdit(request):
    obj = webSettings.objects.get(user=request.user)
    webForm = webSettingsForm(instance=obj)
    if request.method == 'POST':
        webForm = webSettingsForm(request.POST, request.FILES, instance=obj)
        if webForm.is_valid():
            webForm.save()
            messages.success(request, 'Your websettings has been updated.')
            return redirect('webSettingsEdit')
    context = {
        'webForm': webForm,
    }
    return render(request, 'back/settings/webSettingsEdit.html', context)


@login_required(login_url='login')
def ListTermPage(request):
    all_termPages = TermPages.objects.all().order_by('-updated_on')
    context = {
        'all_termPages': all_termPages,
    }
    return render(request, 'back/termPage/List.html', context)


@login_required(login_url='login')
def editTermPage(request, slug):
    obj = TermPages.objects.get(slug=slug)
    tpForm = termPageForm(instance=obj)
    if request.method == 'POST':
        tpForm = termPageForm(request.POST, request.FILES, instance=obj)
        if tpForm.is_valid():
            tpForm.save()
            messages.success(request, 'Your term page has been updated.')
            return redirect('ListTermPage')
    context = {
        'obj': obj,
        'tpForm': tpForm,
    }
    return render(request, 'back/termPage/Edit.html', context)


@login_required(login_url='login')
def aboutCategory(request):
    allAboutPageCategory = pageCategory.objects.all().order_by('-created_date')
    context = {
        'allAboutPageCategory': allAboutPageCategory,
    }
    return render(request, 'back/termPage/List.html', context)