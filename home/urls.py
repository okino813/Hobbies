from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<str:slug>", views.single_article, name="single_article"),
    # path("add/", views.add_article, name="add_article"),
    # path("add/validate", views.validate_add_article, name="validate_add_article"),
    path("search", views.search, name="search"),
    path("contact", views.contact, name="contact"),
    path("a-propos", views.apropos, name="apropos"),

]
