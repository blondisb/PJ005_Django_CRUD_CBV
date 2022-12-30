from django.db import models

# Create your models here.

# TABLE CANDIDATES
genders = (
    ('M', 'M'),
    ('F', 'F')
)

positions = (
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('Fullstack', 'Fullstack'),
    ('Ux Ui', 'Ux Ui')
)

class MO_candidates(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=genders, null=True)
    position = models.CharField(max_length=50, choices=positions, null=True)

    def __str__(self):
        return self.name