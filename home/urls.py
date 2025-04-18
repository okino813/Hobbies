from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<str:slug>", views.single_article, name="single_article"),
    path("search", views.search, name="search"),
    path("contact", views.contact, name="contact"),
    path("a-propos", views.apropos, name="apropos"),

]
