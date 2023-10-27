from django import template
from Menu.models import *

register = template.Library()


@register.inclusion_tag('Menu/menu_teg.html')
def get_menu_teg(SelectedItem, SelectedCategory):
    itemsMenu = Items.objects.all()
    categoryList = []

    for category in itemsMenu:
        if category.cat not in categoryList:
            categoryList.append(category.cat)

    context = {
        'itemsMenu': itemsMenu,
        'categoryList': categoryList,
        'SelectedItem': SelectedItem,
        'SelectedCategory': SelectedCategory
    }

    return context
