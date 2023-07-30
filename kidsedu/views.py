from typing import Any, Dict
from django.shortcuts import render
from .models import *
from django.views.generic import ListView

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
    context['title'] = 'Главная страница'
    return render(request, 'kidsedu/index2.html', context=context)


class AllPosts(ListView):
    model = ProgramEdu
    context_object_name = 'progs'
    template_name = 'kidsedu/all_classes.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все программы'
        context['social'] = social
        return context
