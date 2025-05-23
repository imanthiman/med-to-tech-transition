from django.test import TestCase
from .models import Doctor, Patient, Appointment
from django.utils import timezone

class AppointmentModelTest(TestCase):

    def setUp(self):
        self.doctor = Doctor.objects.create(name="Dr. Iman", specialty="Cardiology", email="iman@clinic.com")
        self.patient = Patient.objects.create(name="John Doe", email="john@example.com", date_of_birth="1990-01-01")
        self.appointment = Appointment.objects.create(
            doctor=self.doctor,
            patient=self.patient,
            appointment_date=timezone.now(),
            reason="Regular checkup"
        )

    def test_appointment_str(self):
        self.assertIn("John Doe", str(self.appointment))