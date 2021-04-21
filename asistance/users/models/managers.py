from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """
    Manage the blog user, email is the login identifier and first name and last name are mandatory
    """

    def create_user(self, email, name, password=None):
        """
        Create and save an User with the given EMAIL, NAME and Password.
        """
        if not email:
            raise ValueError("Cada estudiante debe tener un email valido")
        if not name:
            raise ValueError("Cada estudiante debe tener nombre completo")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Create and save an Super User with the given EMAIL, FIRST_NAME, LAST_NAME and Password.
        """

        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_teacher = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
