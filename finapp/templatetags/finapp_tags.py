from django import template
from finapp.models import Category

register=template.Library()

@register.simple_tag()
def category():
 return Category.objects.filter(published=True)
