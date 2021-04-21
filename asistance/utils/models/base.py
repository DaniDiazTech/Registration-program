"""Asistance base models"""

# Import models
from django.db import models

from django.utils.translation import gettext_lazy as _

class AsistanceModel(models.Model):
    """
    Base model for the Asistance app
    """
    created = models.DateTimeField(
        _("Created at"),

        # Adds the date only when the object is created
        auto_now_add=True,
        help_text=_("Date time in wich the object was modified")
    )

    modified = models.DateTimeField(
        _("Modified at"),

        # Records the date each time the model hits "save()"
        auto_now=True,
        help_text=_("Date time in which the object was modified")
    )

    class Meta:
        """Meta class: Abstract class"""

        abstract = True

        # Latest by =  last object that has been created
        get_latest_by = "created" 

        # Last created will be the latest
        # Also applies for modified
        ordering = ["-created", "-modified"]