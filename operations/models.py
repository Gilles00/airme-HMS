# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from core.models import TimeStampedModel
from reception.models import Patient
from hospital.models import Diagnose
from staff.models import Doctor, Nurse


# Create your models here.
class Diagnose(TimeStampedModel):
    name = models.CharField(max_length=200)
    code = models.IntegerField(default=0, unique=True)
    description = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.code, self.name)


class Treatment(TimeStampedModel):
    date = models.DateField(default=timezone.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    symptoms = models.TextField()
    diagnosis = models.ForeignKey(Diagnose, null=True, on_delete=models.SET_NULL)
    doctors_comments = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.patient, self.diagnosis)


class Vaccine(TimeStampedModel):
    name = models.CharField(max_length=100)
    live = models.BooleanField(blank=True)
    absorved = models.BooleanField(null=True)
    inactivated = models.BooleanField(null=True,)
    oral = models.BooleanField(null=True)

    def __str__(self):
        return self.name

class VaccineApplied(TimeStampedModel):
    date = models.DateField(default=timezone.now)
    vaccine = models.ForeignKey(Vaccine, null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    nurse = models.ForeignKey(Nurse, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s | by  %s (%s)' % (self.patient, self.nurse, self.date)

    class Meta:
        verbose_name = 'Vaccine Applied'
        verbose_name_plural = 'Vaccines usage'


class Test(TimeStampedModel):
    mame = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MedicalTest(TimeStampedModel):
    date = models.DateField(default=timezone.now)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    test = models.ForeignKey(Test, null=True, on_delete=models.SET_NULL)
    results = models.CharField(max_length=500)
    status = models.BooleanField()

    def __str__(self):
        return '{}-{}'.format(self.patient, self.test.name)
