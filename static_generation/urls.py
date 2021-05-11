from .admin import urls
from django.conf.urls import url, include

urlpatterns = [
    url(r'^static-generation/', include((urls, 'static_generation'), namespace='static_generation'))
]
