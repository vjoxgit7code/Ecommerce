from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def search_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query, available=True))
    return render(request, 'search.html', {'query': query, 'products': products})

