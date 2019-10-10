from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('^today/$',views.todays_pic,name='picToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pics,name = 'pastPics') 
]