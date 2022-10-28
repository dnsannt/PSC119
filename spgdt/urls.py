from unicodedata import name
from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from spgdt.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pbfree', PbfreeViewset)
router.register('spgdt', SpgdtViewset)
router.register('giat', GiatViewset)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.chart_pb, name='chart-pb'),

    path('spgdt/', views.spgdt, name="spgdt"),
    path('addspgdt/', views.addspgdt, name="addspgdt"),
    path('pb/', views.pb, name="pb"),
    path('tab/', views.tab, name="tab"),
    path('giat/', views.giat, name="giat"),
    path('chart_giat/', views.chart_giat, name="chart_giat"),
    path('chart-pb/', views.chart_pb, name="chart-pb"),
    path('get-pb/', views.getpb, name="chart_pb"),
    path('get-giat/', views.getgiat, name="chart_giat"),
    path('get-telp/', views.gettelp, name="chart_telp"),
    path('video/', views.video, name="video"),
    path('video-giat/', views.videogiat, name="video-giat")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
