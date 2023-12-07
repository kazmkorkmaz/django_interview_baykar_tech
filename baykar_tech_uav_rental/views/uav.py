from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import UAV
from ..forms.uav import UAVForm
from ..filters.uav import UAVFilter


@login_required(login_url="/login")
def uav_list(request):
    uavs = UAV.objects.all()
    items_per_page = 10

    uav_filter = UAVFilter(request.GET, queryset=uavs)
    uavs = uav_filter.qs

    paginator = Paginator(uavs, items_per_page)
    page = request.GET.get('page', 1)

    try:
        uavs = paginator.page(page)
    except PageNotAnInteger:
        uavs = paginator.page(1)
    except EmptyPage:
        uavs = paginator.page(paginator.num_pages)

    return render(request, 'baykar_tech_uav_rental/uav/list.html', {
        'uavs': uavs,
        'uav_filter': uav_filter,
    })


@login_required(login_url="/login")
def uav_add(request):
    if request.method == 'POST':
        form = UAVForm(request.POST)
        if form.is_valid():
            uav = form.save(commit=False)
            uav.created_by = request.user
            uav.save()
            return redirect('uav_list')
    else:
        form = UAVForm()

    return render(request, 'baykar_tech_uav_rental/uav/create.html', {'form': form})


@login_required(login_url="/login")
def uav_update(request, slug):
    uav = get_object_or_404(UAV, slug=slug)

    if request.method == 'POST':
        form = UAVForm(request.POST, instance=uav)
        if form.is_valid():
            form.save()
            return redirect('uav_list')
    else:
        form = UAVForm(instance=uav)

    return render(request, 'baykar_tech_uav_rental/uav/update.html', {'form': form, 'uav': uav})


@login_required(login_url="/login")
def uav_delete(request, slug):
    uav = get_object_or_404(UAV, slug=slug)

    if request.method == 'POST':
        uav.delete()
        return redirect('uav_list')

    return render(request, 'baykar_tech_uav_rental/uav/delete.html', {'uav': uav})
