from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Default user for asistance."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), max_length=255)
   
    email = EmailField(
        _("Email Address"),
        max_length=254,
        unique=True
        )
    
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    
    is_teacher = BooleanField(
        _("Teacher status"), 
        default=False, 
        help_text=_("Determinates if the user is able to create classrooms")    
        )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name",]
    
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        """Returns the user's name"""
        return str(self.name)
