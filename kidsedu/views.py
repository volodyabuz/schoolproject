from typing import Any, Dict
from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from .forms import *

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
}

context = {
    'title': 'SchoolEdu',
    'social': social,
    'nav_item': nav_item,
    }


def index(request):
    if request.method == 'POST':
        form = AddPersonForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddPersonForm()
    else:
        form = AddPersonForm()
    context['title'] = 'Главная страница'
    context['form'] = form
    return render(request, 'kidsedu/index2.html', context=context)


class AllPosts(ListView):
    model = ProgramEdu
    context_object_name = 'progs'
    template_name = 'kidsedu/all_classes.html'
    form = AddPersonForm
    success_url = '/all'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все программы'
        context['social'] = social
        context['form'] = AllPosts.form
        return context
