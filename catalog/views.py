from django.shortcuts import render


def home(request):
    """Контроллер для главной страницы"""
    return render(request, 'catalog/home.html')


def contacts(request):
    """Контроллер для страницы контактов"""
    if request.method == 'POST':
        # Обработка формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"📩 Новая заявка: {name}, {phone}, {message}")
        return render(request, 'catalog/contacts.html', {'success': True})

    return render(request, 'catalog/contacts.html')