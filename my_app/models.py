from django.db import models

class Info(models.Model):
    student_id = models.CharField(max_length=20, default="N/A")
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    class_code = models.CharField(max_length=50, default="BSIT-BT2-101")

    def __str__(self):
        return f"{self.student_id} - {self.name}"
