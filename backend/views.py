from django.db.models import Q
from rest_framework import generics
from django.views.generic import ListView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import render
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

class AppointmentListPageView(View):
    template_name = 'appointments.html'

    def get(self, request):
        appointments_list = Appointment.objects.all()

        # Filtering
        doctor = request.GET.get('doctor')
        patient = request.GET.get('patient')
        appointment_date = request.GET.get('appointment_date')

        if doctor:
            appointments_list = appointments_list.filter(doctor__full_name__icontains=doctor)
        if patient:
            appointments_list = appointments_list.filter(patient__name__icontains=patient)
        if appointment_date:
            appointments_list = appointments_list.filter(appointment_date__date=appointment_date)

        # Pagination
        paginator = Paginator(appointments_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'appointments': page_obj,
            'page_obj': page_obj
        }

        return render(request, self.template_name, context)

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['doctor', 'patient', 'appointment_date', 'reason']
    template_name = 'appointment_edit.html'
    success_url = reverse_lazy('appointments-page')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('appointments-page')