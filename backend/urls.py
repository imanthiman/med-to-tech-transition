from django.urls import path
from .views import DoctorListCreateView, PatientListCreateView, AppointmentListCreateView, AppointmentListPageView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('appointments-page/', AppointmentListPageView.as_view(), name='appointment-page'),
]