from django.conf.urls import url
from .views import AuthorAndBookView

urlpatterns = [
    url(r'^author/$', AuthorAndBookView.as_view(), name='author'),
]