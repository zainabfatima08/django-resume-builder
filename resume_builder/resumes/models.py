from django.db import models
from core.models import Resume
from colorfield.fields import ColorField

#--------------SECTION MODEL--------------

class Section(models.Model):

    resume = models.ForeignKey(Resume, on_delete = models.CASCADE)
    title  = models.CharField(max_length = 100)
    order  = models.PositiveIntegerField(default = 0)

    class Meta:
        ordering = ['order']
#----------------THEME MODEL-------------------

class ResumeTheme(models.Model):
    name = models.CharField(max_length = 50)
    primary_color = ColorField(default = '#000000')

