"""
Student model
"""

# Custom base model
from asistance.utils.models import AsistanceModel

from django.db import models

from django.utils.text import gettext_lazy as _

class Student(AsistanceModel):
    """Student model

    Args:
        AsistanceModel (object): Parent model -> created, modified
    
    Attrs:
        name: CharField
    """
    
    name = models.CharField(
        _("Student name"),
        max_length=120 
    )
    