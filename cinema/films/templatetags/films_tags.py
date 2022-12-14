from django import template
from datetime import date, timedelta
from films.models import Films

register = template.Library()

@register.simple_tag()
def get_list_date():
    list_date = []
    today = date.today()

    for i in range(1, 7):
        delta = timedelta(days=i)
        date_next = today + delta
        list_date.append(date_next)

    return list_date




