from django.urls import path
from .views import DoctorListCreateView, PatientListCreateView, AppointmentListCreateView, AppointmentListPageView, AppointmentUpdateView, AppointmentDeleteView, DoctorListPageView, DoctorUpdateView, DoctorDeleteView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('appointments-page/', AppointmentListPageView.as_view(), name='appointments-page'),
    path('appointments/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment-edit'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment-delete'),
    path('doctors-page/', DoctorListPageView.as_view(), name='doctors-page'),
    path('doctors/<int:pk>/edit/', DoctorUpdateView.as_view(), name='doctor-edit'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor-delete'),
]