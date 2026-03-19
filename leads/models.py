from django.db import models

# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    bhk = models.CharField(max_length=10)
    timeline = models.CharField(max_length=20)
    budget = models.CharField(max_length=20)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.phone}"

    class Meta:
        ordering = ['-submitted_at']


# python manage.py makemigrations
# python manage.py migrate