"""
Classroom models
"""
# Import models
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

from django.urls import reverse_lazy

# Slugify the name
from django.utils.text import slugify

# Import custom base model
from asistance.utils.models import AsistanceModel

class Classroom(AsistanceModel):
    """Classroom Model, where students register

    Args:
        AsistanceModel (Parent model): inherence -> created, modified

    Attrs:
        name (Charfield)
        slug (Slugfield)
        teacher (ForeignKey)

    Returns:
        [Classroom object]: Model
    """

    name = models.CharField(
        _("A classroom is the way students check their asistance"),
        max_length=75,
        # Specifies that the name must be unique
        unique=True
    )

    slug = models.SlugField(null=False, unique=True) # slug

    teacher = models.ForeignKey(
        # Relation with teacher
        get_user_model(),
        # If the teacher is deleted its classrooms too
        on_delete=models.CASCADE
    )

    # Saves the model and creates the slug
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        """Returns the classroom name"""
        return str(self.name)

    def get_absolute_url(self):
        """Returns the detail object"""
        return reverse_lazy('classroom:detail', kwargs={'slug': self.slug}) # new