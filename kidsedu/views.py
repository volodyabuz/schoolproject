from typing import Any, Dict
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import *
from django.views.generic import ListView, CreateView
from .forms import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page

social = {
    'vk': 'https://vk.com/id462686534',
    'instagram': 'https://www.instagram.com/volodyabuz/',
    'telegram': 'https://t.me/volodyabuz',
}

nav_item = {
    '#home': 'Главная',
    '#about': 'О нас',
    '#class': 'Занятия',
    '#schedule': 'Расписание',
    '#contact': 'Контакты',
    # '/register': 'Регистрация'
}

context = {
    'title': 'SchoolEdu',
    'social': social,
    'nav_item': nav_item,
    }

@cache_page(60)
def index(request):
    # Формы
    if request.method == 'POST':

        form = AddPersonForm(request.POST)
        form_fb = FeedBackForm(request.POST)

        # Форма заявки
        if form.is_valid():
            send_email_func(form, 'Новая заявка пользователя')
            form.save()
            form = AddPersonForm()
            form_fb = FeedBackForm()

        # Форма обратной связи
        if form_fb.is_valid():
            send_email_func(form_fb, 'Новая обратная связь')
            form = AddPersonForm()
            form_fb = FeedBackForm()

    else:
        form = AddPersonForm()
        form_fb = FeedBackForm()

    context['title'] = 'Главная | SchoolEdu'
    context['form'] = form
    context['form_fb'] = form_fb
    return render(request, 'kidsedu/index2.html', context=context)


class AllPosts(ListView):
    paginate_by = 3
    model = ProgramEdu
    context_object_name = 'progs'
    template_name = 'kidsedu/all_classes.html'
    form = AddPersonForm
    success_url = '/all'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все программы | SchoolEdu'
        context['social'] = social
        context['form'] = AllPosts.form
        return context

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'kidsedu/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация | SchoolEdu'
        context['social'] = social
        context['form'] = Register.form_class
        return context

def send_email_func(used_form, subject_mail):
    # Получаем данные полей формы для отправки
    data = {}
    if used_form.declared_fields:
        for field in used_form.declared_fields.keys():
            data[field] = used_form.cleaned_data[field]
    else:
        for field in used_form.base_fields.keys():
            data[field] = used_form.cleaned_data[field]
    print(data)
    # Отправляем данные в шаблон пиьсма
    html_body = render_to_string('kidsedu/email.html', context={'data': data})
    # Отправляем пиьсмо
    msg = EmailMultiAlternatives(
        subject=f'SchoolEdu(Django): {subject_mail}',
        to=['volodyabuz@gmail.com']
    )
    msg.attach_alternative(html_body, "text/html")
    msg.send()

    return redirect('home')

def view_404(request, exception):
    context['title'] = 'Страница не найдена | SchoolEdu'
    return render(request, 'kidsedu/404.html')
