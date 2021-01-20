from django.template.defaulttags import register

"""Количество строк на экране константа COUNT_OF_LINE"""
from todo.settings import COUNT_OF_LINE

@register.filter()
def get_count(lists):
    return range(COUNT_OF_LINE-len(lists))
