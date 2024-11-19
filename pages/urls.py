from django.urls import path
from .views import home_page_view, about_page_views

urlpatterns = [
    path("", home_page_view),
    path("about/", about_page_views),
]