from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url(r'^$',views.welcome,name = 'welcome'),
    url(r'^$',views.todays_pic,name='welcome'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pics,name = 'pastPics'),
    url(r'^picture/(\d+)',views.pictureDis,name ='picture'),
    url(r'^search/', views.search, name='search')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)