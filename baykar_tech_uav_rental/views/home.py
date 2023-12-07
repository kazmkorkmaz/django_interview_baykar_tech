from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import UAV, Rental, Category


@login_required(login_url="/login")
def index(request):
    uav_count = UAV.objects.count()
    rental_count = Rental.objects.count()
    category_count = Category.objects.count()

    return render(request, 'baykar_tech_uav_rental/index.html', {
        'uav_count': uav_count,
        'rental_count': rental_count,
        'category_count': category_count,
    })
