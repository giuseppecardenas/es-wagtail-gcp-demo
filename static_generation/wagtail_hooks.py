from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from .urls import urlpatterns

@hooks.register('register_admin_urls')
def register_admin_urls():
    return urlpatterns

@hooks.register('register_settings_menu_item')
def register_static_generation_menu_item():
    return MenuItem(
        'Generate Site as Flat Files',
        reverse('static_generation:static_generation_admin_index'),
        classnames='icon icon-cog',
        order=901
    )