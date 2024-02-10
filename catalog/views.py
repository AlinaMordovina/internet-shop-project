from django.shortcuts import render


def homepage(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        with open('contacts.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{name} {phone}: {message}\n')

        print(f"{name} {phone}: {message}")

    return render(request, 'catalog/contacts.html')
