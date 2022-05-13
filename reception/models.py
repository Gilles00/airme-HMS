# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import truncatechars
from django.utils import timezone
from django.db import models

# project imports
from core.models import TimeStampedModel
from hospital.models import Person, Room, Diagnose
from staff.models import Doctor


class Patient(Person):
    preferred_hospital = models.CharField(max_length=50, blank=True, null=True)
    primary_physician = models.CharField(max_length=50, blank=True, null=True)
    last_physical = models.CharField(max_length=50)
    health_history = models.CharField(max_length=600)
    status = models.CharField(max_length=10)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class In_patient(TimeStampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_adm = models.DateField(default=timezone.now)
    date_of_discarge = models.DateField()
    diagnosis = models.ForeignKey(Diagnose, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}-{}'.format(self.patient, self.room)


class Out_patient(TimeStampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    diagnosis = models.ForeignKey(Diagnose,  null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor,  null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}'.format(self.patient)


class MedicalHistory(TimeStampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    textHistory = models.CharField(max_length=500)

    @property
    def brief_history(self):
        if len(self.textHistory) <= 20:
            return self.textHistory
        else:
            return '{}'.format(truncatechars(self.textHistory, 20))

    def __str__(self):
        return '{}-{}'.format(self.patient, self.brief_history)
