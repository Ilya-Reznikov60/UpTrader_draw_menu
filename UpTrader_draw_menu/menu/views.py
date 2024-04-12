from django.shortcuts import render
from urllib.parse import unquote

from menu.models import MenuItem


def index(request):
    """
    Отображение главной страницы.
    """
    return render(request, 'menu/index.html')


def draw_menu(request, menu_url):
    """
    Отображение меню на основе переданного URL-адреса меню.
    """
    decoded_menu_url = unquote(menu_url)
    menu_items = MenuItem.objects.filter(
        url=decoded_menu_url
    ).select_related('parent')
    return render(
        request, 'menu/draw_menu.html',
        {'menu_items': menu_items, 'menu_name': decoded_menu_url}
    )
