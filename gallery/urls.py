from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('^today/$',views.todays_pic,name='picToday')
]