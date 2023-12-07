from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Category
from ..forms.category import CategoryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..filters.category import CategoryFilter


@login_required(login_url="/login")
def category_list(request):
    categories = Category.objects.all()
    items_per_page = 10

    # Apply filtering
    category_filter = CategoryFilter(request.GET, queryset=categories)
    categories = category_filter.qs

    paginator = Paginator(categories, items_per_page)
    page = request.GET.get('page', 1)

    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    return render(request, 'baykar_tech_uav_rental/category/list.html', {
        'categories': categories,
        'category_filter': category_filter,
    })


@login_required(login_url="/login")
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'baykar_tech_uav_rental/category/create.html', {'form': form})


@login_required(login_url="/login")
def category_update(request, slug):
    category = get_object_or_404(Category, slug=slug)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'baykar_tech_uav_rental/category/update.html', {'form': form, 'category': category})


@login_required(login_url="/login")
def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    return render(request, 'baykar_tech_uav_rental/category/delete.html', {'category': category})
