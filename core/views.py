from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class FrontendAppView(TemplateView):
    template_name = "index.html"


def about(request):
    selected_plan = request.GET.get("plan")  # будет ценовой план full / third / eighth
    return render(request, "about.html", {"plan": selected_plan})

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        subscribe = request.POST.get('subscribe') == 'on'
        gender = request.POST.get('gender')
        message = request.POST.get('message')
        plan = request.POST.get('plan')

        # Здесь можно сохранять данные в базу или делать что-то ещё
        print("Форма отправлена:")
        print(
            f"Выбранный план: {plan}, Имя: {name}, Email: {email}, Пароль: {password}, Подписка: {subscribe}, Пол: {gender}, Сообщение: {message}")

        return redirect('home')  # возвращаем на главную после отправки

    return redirect('home')


""" from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def my_action(request):
    if request.method == 'POST':
        print("Кнопка отправки формы нажата!")
        # Здесь можно добавить логику: сохранять данные, вызывать функции и т.д.
    return redirect('home')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        subscribe = request.POST.get('subscribe') == 'on'
        gender = request.POST.get('gender')
        message = request.POST.get('message')

        # Здесь можно сохранять данные в базу или делать что-то ещё
        print("Форма отправлена:")
        print(
            f"Имя: {name}, Email: {email}, Пароль: {password}, Подписка: {subscribe}, Пол: {gender}, Сообщение: {message}")

        return redirect('home')  # возвращаем на главную после отправки

    return redirect('home')"""