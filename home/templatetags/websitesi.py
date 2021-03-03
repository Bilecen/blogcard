import datetime

from django import template

register = template.Library()

@register.simple_tag()
def bitistarihi(value:datetime):
    if value is None:
        return "Devam Etmekte"
    else :
        d = datetime.datetime.strftime(value,"%M %Y")
        return  d