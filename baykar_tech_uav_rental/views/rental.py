from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from ..models.rental import Rental
from ..filters.rental import RentalFilter
from ..forms.rental import RentalForm


@login_required(login_url="/login")
def rental_list(request):
    rentals = Rental.objects.all()
    items_per_page = 10

    rental_filter = RentalFilter(request.GET, queryset=rentals)
    rentals = rental_filter.qs

    paginator = Paginator(rentals, items_per_page)
    page = request.GET.get('page', 1)

    try:
        rentals = paginator.page(page)
    except PageNotAnInteger:
        rentals = paginator.page(1)
    except EmptyPage:
        rentals = paginator.page(paginator.num_pages)

    return render(request, 'baykar_tech_uav_rental/rental/list.html', {
        'rentals': rentals,
        'rental_filter': rental_filter,
    })


@login_required(login_url="/login")
def rental_add(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user
            rental.save()
            return redirect('rental_list')
    else:
        form = RentalForm()

    return render(request, 'baykar_tech_uav_rental/rental/create.html', {'form': form})


@login_required(login_url="/login")
def rental_update(request, slug):
    rental = get_object_or_404(Rental, slug=slug)

    if request.method == 'POST':
        form = RentalForm(request.POST, instance=rental)
        if form.is_valid():
            form.save()
            return redirect('rental_list')
    else:
        form = RentalForm(instance=rental)

    return render(request, 'baykar_tech_uav_rental/rental/update.html', {'form': form, 'rental': rental})


@login_required(login_url="/login")
def rental_delete(request, slug):
    rental = get_object_or_404(Rental, slug=slug)

    if request.method == 'POST':
        rental.delete()
        return redirect('rental_list')

    return render(request, 'baykar_tech_uav_rental/rental/delete.html', {'rental': rental})
