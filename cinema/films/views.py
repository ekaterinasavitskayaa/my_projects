import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Films
from .forms import FilmsForm


class HomeFilms(ListView):
    model = Films
    template_name = 'films/home_films_list.html'
    context_object_name = 'films'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):

        return Films.objects.filter(is_published=True)




class ViewFilms(DetailView):
    model = Films
    pk_url_kwarg = 'films_id'
    context_object_name = 'films_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Краткое описание фильма'
        return context


class CreateFilms(CreateView):
    form_class = FilmsForm
    template_name = 'films/add_films.html'

#
# def add_films(request):
#     if request.method == 'POST':
#         form = FilmsForm(request.POST)
#         if form.is_valid():
#             film_add = form.save()
#             # film_add = Films.objects.create(**form.cleaned_data)
#             return redirect(film_add)
#     else:
#         form = FilmsForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'films/add_films.html', context)


def price(request):
    today = datetime.now()
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    wd = datetime.weekday(today)
    weekday_now = days[wd]
    year = today.strftime("%Y")
    my_date = today.strftime("%d %B %a")
    context = {
        'title': 'Цены',
        'today': today,
        'weekday_now': weekday_now,
        'year': year,
        'date': my_date,
    }
    return render(request, 'films/price.html', context)


def about(request):
    list_date = []
    today = datetime.datetime.now()
    for i in range(7):
        delta = datetime.timedelta(days=i)
        list_date.append(today + delta)

    context = {
        'title': 'О нас',
        'list_date': list_date,
    }

    return render(request, 'films/about.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'films/contacts.html', context)


