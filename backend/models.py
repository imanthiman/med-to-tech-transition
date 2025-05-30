from django.db import models

class CosmeticDoctor(models.Model):
    name = models.CharField(max_length=100)
    clinic = models.CharField(max_length=200)
    specialty = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    contact_number = models.IntegerField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.specialty}"