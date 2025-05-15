from django.urls import path
from . import views

urlpatterns = [
    path('', views.salom),
    path('<str:category>/<str:name>/', views.info)
]

