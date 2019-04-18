"""DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register("authors",views.AuthorsView)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/$', views.BooksView.as_view()),
    url(r'^books/(\d+)/', views.SBookView.as_view()),
    url(r'^publishes/$', views.PublishView.as_view()),
    url(r'^publishes/(?P<pk>\d+)/', views.SPublishView.as_view()),
    # url(r'^authors/$', views.AuthorsView.as_view()),
    # url(r'^authors/(?P<pk>\d+)/', views.SAuthorsView.as_view()),
    # url(r'^authors/$', views.AuthorsView.as_view({"get":"list","post":"create"})),
    # url(r'^authors/(?P<pk>\d+)/', views.AuthorsView.as_view({"get":"retrieve","delete":"destroy","put":"update"})),
    # login
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^',include(router.urls))
]
