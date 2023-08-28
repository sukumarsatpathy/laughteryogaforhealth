from .models import category


def serviceCategory(request):
    all_serviceCat = category.objects.filter(status='Published').order_by('created_date')
    return dict(all_serviceCat=all_serviceCat)