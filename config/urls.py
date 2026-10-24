from django.urls import path

from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    # Share link for LinkedIn: preview card, then the EMAA Expo live demo.
    path("emaa-expo/", views.emaa_expo, name="emaa_expo"),
    # Direct link to preview the "page not found" design.
    path("404/", views.not_found, name="not_found"),
]

handler404 = "pages.views.not_found"
