from django import template
from django.urls import reverse, resolve
from django.utils.html import format_html
from menu.models import MenuItem

register = template.Library()


def get_current_url_name(request):
    """
    Получает имя текущего URL-адреса из запроса.
    """
    url_name = resolve(request.path_info).url_name
    return url_name


def render_menu(menu_item, current_url_name, level=1):
    """
    Рекурсивно отрисовывает элементы меню и их дочерние элементы.

    Где:
        menu_item:
        Экземпляр модели MenuItem, представляющий текущий элемент меню.
        current_url_name: Имя текущего URL-адреса.
        level: Уровень вложенности элемента меню.
    """
    html = f"<li>{'    ' * (level-1)}"
    if menu_item.url:
        if menu_item.url == current_url_name:
            html += format_html(
                "<a href='{0}' class='active'>{1}</a>",
                menu_item.url, menu_item.title
            )
        else:
            html += format_html(
                "<a href='{0}'>{1}</a>", menu_item.url,
                menu_item.title
            )
    elif menu_item.named_url:
        if menu_item.named_url == current_url_name:
            html += format_html(
                "<a href='{0}' class='active'>{1}</a>",
                reverse(menu_item.named_url), menu_item.title
            )
        else:
            html += format_html(
                "<a href='{0}'>{1}</a>",
                reverse(menu_item.named_url), menu_item.title
            )
    else:
        html += format_html("{0}", menu_item.title)
    if menu_item.children.exists():
        html += format_html("\n{0}<ul>", '    ' * level)
        for child in menu_item.children.all():
            html += render_menu(child, current_url_name, level + 1)
        html += format_html("\n{0}</ul>", '    ' * level)
    html += "</li>\n"
    return html


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Создаёт HTML-код для отображения меню.
    """
    request = context['request']
    current_url_name = get_current_url_name(request)
    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name)
    html = '<ul>'
    for item in menu_items:
        html += render_menu(item, current_url_name)
    html += '</ul>'
    return format_html(html)
