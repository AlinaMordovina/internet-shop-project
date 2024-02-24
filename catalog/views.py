from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        'object_list': products
    }
    return render(request, 'catalog/product_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        with open('contacts.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{name} {phone}: {message}\n')

        print(f"{name} {phone}: {message}")

    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product
    }
    return render(request, 'catalog/product_detail.html', context)
