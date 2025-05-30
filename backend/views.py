from rest_framework import generics
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentListPageView(ListView):
    model = Appointment
    template_name = 'appointments.html'
    context_object_name = 'appointments'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['doctor', 'patient', 'appointment_date', 'reason']
    template_name = 'appointment_edit.html'
    success_url = reverse_lazy('appointments-page')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('appointments-page')