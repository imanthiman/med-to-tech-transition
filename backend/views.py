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

class DoctorListPageView(View):
    template_name = 'doctors.html'

    def get(self, request):
        doctors_list = Doctor.objects.all()

        doctor = request.GET.get('doctor')

        if doctor:
            doctors_list = doctors_list.filter(full_name__icontains=doctor)

        paginator = Paginator(doctors_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'doctors': page_obj,
            'page_obj': page_obj
        }

        return render(request, self.template_name, context)

class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ['full_name', 'clinic', 'specialty', 'years_of_experience', 'contact_number']
    template_name = 'doctor_edit.html'
    success_url = reverse_lazy('doctors-page')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor_confirm_delete.html'
    success_url = reverse_lazy('doctors-page')

class AppointmentListPageView(View):
    template_name = 'appointments.html'

    def get(self, request):
        appointments_list = Appointment.objects.all()

        doctor = request.GET.get('doctor')
        patient = request.GET.get('patient')
        appointment_date = request.GET.get('appointment_date')

        if doctor:
            appointments_list = appointments_list.filter(doctor__full_name__icontains=doctor)
        if patient:
            appointments_list = appointments_list.filter(patient__name__icontains=patient)
        if appointment_date:
            appointments_list = appointments_list.filter(appointment_date__date=appointment_date)

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