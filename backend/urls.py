from django.urls import path
from .views import DoctorListCreateView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
]