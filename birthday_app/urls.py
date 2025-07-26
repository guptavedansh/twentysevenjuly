from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('vuvu', views.vuvu_note, name="vuvu"),
    path('chhawi', views.chhawi_note, name="chhawi"),
    path('vandu', views.vandu_note, name="vandu"),
    path('gifts', views.gifts, name="gifts"),
]
