from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download_cv/<int:cv_id>/', views.download_cv, name='download_cv'),
]