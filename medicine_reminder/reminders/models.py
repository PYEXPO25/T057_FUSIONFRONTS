from django.db import models

class MedicineReminder(models.Model):
    medicine_name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    frequency = models.CharField(max_length=50, choices=[
        ('OD', 'Once Daily'),
        ('BD', 'Twice Daily'),
        ('TDS', 'Thrice Daily'),
        ('QID', 'Four times a day'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.medicine_name} - {self.date} {self.time}"
