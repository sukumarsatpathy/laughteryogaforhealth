import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from .models import Account, UserProfile
from .forms import UserForm, UserProfileForm
from blogs.models import Blog
from testimonials.models import Testimonial
from pages.models import adBlock, lyJournals
from reports.models import Contact, Invite, Newsletter

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def login(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                url = request.META.get('HTTP_REFERER')
                try:
                    query = requests.utils.urlparse(url).query
                    params = dict(x.split('=') for x in query.split('&'))
                    if 'next' in params:
                        nextPage = params['next']
                        return redirect(nextPage)
                except:
                    return redirect('dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
        return render(request, 'front/accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message_content = {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            }
            from_email = 'Laughter Yoga For Health <settings.DEFAULT_FROM_EMAIL>'
            to_email = (email,)
            html_content = render_to_string('front/email/reset-password-email.html', message_content)
            if email:
                try:
                    send_mail(mail_subject, None, from_email, to_email, html_message=html_content)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, 'Password reset email has been sent to your email address.')
                return redirect('login')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'front/accounts/forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'front/accounts/resetPassword.html')


@login_required(login_url='login')
def dashboard(request):
    contacts_count = Contact.objects.count()
    invite_count = Invite.objects.count()
    newsletter_count = Newsletter.objects.count()
    blog_count = Blog.objects.count()

    recent_blogs = Blog.objects.filter(status='Published').order_by('-submission_date')[:4]
    popular_blogs = Blog.objects.filter(status='Published', views__gt=100)[:4]
    latest_testimonials = Testimonial.objects.filter(status='Published').order_by('-submission_date')[:5]
    latest_ads = adBlock.objects.filter(status='Published')[:4]
    latest_journals = lyJournals.objects.filter(status='Published')[:8]

    latest_contacts = Contact.objects.all().order_by('-submitted_date')[:3]
    latest_invites = Invite.objects.all().order_by('-submitted_date')[:3]
    latest_subscribers = Newsletter.objects.all().order_by('-submitted_date')[:3]
    context = {
        'contacts_count': contacts_count,
        'invite_count': invite_count,
        'newsletter_count': newsletter_count,
        'blog_count': blog_count,
        'recent_blogs': recent_blogs,
        'popular_blogs': popular_blogs,
        'latest_testimonials': latest_testimonials,
        'latest_ads': latest_ads,
        'latest_journals': latest_journals,
        'latest_contacts': latest_contacts,
        'latest_invites': latest_invites,
        'latest_subscribers': latest_subscribers,
    }
    return render(request, 'back/pages/dashboard.html', context)


@login_required(login_url = 'login')
def editProfile(request):
    userDetail = get_object_or_404(UserProfile, user=request.user)
    if userDetail is None:
        profile_form = UserProfileForm()
    else:
        if request.method == 'POST':
            user_form = UserForm(request.POST, request.FILES, instance=request.user)
            profile_form = UserProfileForm(request.POST, request.FILES, instance=userDetail)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your profile has been updated.')
                return redirect('editProfile')
        else:
            user_form = UserForm(instance=request.user)
            profile_form = UserProfileForm(instance=userDetail)

    context = {
        'userDetail': userDetail,
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'back/pages/editProfile.html', context)