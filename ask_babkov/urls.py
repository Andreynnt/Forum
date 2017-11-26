"""ask_babkov URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from questions import views

urlpatterns = [
    url(r'^question(?P<number>\d+)', views.oneQuestion, name="question_page"),
    url(r'^ask/?', views.ask, name="ask_page"),
    url(r'^login/?', views.login, name="login_page"),
    url(r'^register/?', views.register, name="register_page"),
    url(r'^settings/?', views.settings, name="settings_page"),
    url(r'^admin/', admin.site.urls),
    url(r'^page(\d+)/?', views.index, name="page_page"),
    url(r'^', views.index, name="index_page"),
]
