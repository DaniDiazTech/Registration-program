"""
Student model
"""

# Custom base model
from asistance.utils.models import AsistanceModel

from asistance.classrooms.models import Classroom

from django.db import models

from django.utils.text import gettext_lazy as _

class Student(AsistanceModel):
    """Student model

    Args:
        AsistanceModel (object): Parent model -> created, modified
    
    Attrs:
        name: CharField
        assigned_class: Foreign Key
    """
    
    name = models.CharField(
        _("Student name"),
        max_length=120 
    )

    assigned_class = models.ForeignKey(
        Classroom,    
        on_delete=models.CASCADE,
        verbose_name=_("Assigned classroom"),
    )
    