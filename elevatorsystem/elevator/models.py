from django.db import models

# Create your models here.
class Elevator(models.Model):
    STATUS_CHOICES = [
        ('UP', 'Moving Up'),
        ('DOWN', 'Moving Down'),
        ('STOPPED', 'Stopped'),
        ('OPEN', 'Door Open'),
        ('CLOSED', 'Door Closed'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='STOPPED')
    current_floor = models.IntegerField(default=0)

class Request(models.Model):
    DIRECTION_CHOICES = [
        ('UP', 'Up'),
        ('DOWN', 'Down'),
    ]

    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    direction = models.CharField(max_length=4, choices=DIRECTION_CHOICES)
    target_floor = models.IntegerField()
    processed = models.BooleanField(default=False)
