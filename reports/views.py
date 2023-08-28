from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact, Invite, Newsletter


@login_required(login_url='login')
def contactData(request):
    all_cfd = Contact.objects.all().order_by('-submitted_date')
    context = {
        'all_cfd': all_cfd,
    }
    return render(request, 'back/reports/contactData.html', context)


@login_required(login_url='login')
def contactDataView(request, pk):
    single_cfd = get_object_or_404(Contact, id=pk)
    context = {
        'single_cfd': single_cfd,
    }
    return render(request, 'back/reports/contactDataView.html', context)


@login_required(login_url='login')
def inviteData(request):
    all_invtd = Invite.objects.all().order_by('-submitted_date')
    context = {
        'all_invtd': all_invtd,
    }
    return render(request, 'back/reports/inviteData.html', context)


@login_required(login_url='login')
def inviteDataView(request, pk):
    single_ifd = get_object_or_404(Invite, id=pk)
    context = {
        'single_ifd': single_ifd,
    }
    return render(request, 'back/reports/inviteDataView.html', context)


@login_required(login_url='login')
def newsletterData(request):
    all_nwsld = Newsletter.objects.all().order_by('-submitted_date')
    context = {
        'all_nwsld': all_nwsld,
    }
    return render(request, 'back/reports/newsletterData.html', context)
