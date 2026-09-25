from django.urls import path
from . import views

urlpatterns = [
    path("",views.FrontPage.as_view(),name="home"),
    path("list/",views.PostListView.as_view(),name="list")
]