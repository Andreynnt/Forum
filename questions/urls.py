from django.conf.urls import url

from questions.views import AboutView

urlpatterns = [
            url(r'^ask$', AboutView.as_view(), name='about'),
]
