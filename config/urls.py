from django.urls import path

from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    # Direct link to preview the "page not found" design.
    path("404/", views.not_found, name="not_found"),
]

handler404 = "pages.views.not_found"
