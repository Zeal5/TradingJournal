from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

#profile manager
class ProfileManager(BaseUserManager):
    def create(self, email, username, tc, status, password2=None, password=None,):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            tc=tc,
            status=status,
            
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, tc, email,  password=None):
        user = self.create(
            email=email,
            username=username,
            tc=tc,
            password=password,
            status="subscriber",
        )
        user.is_staff = True
        user.save(using=self.db)
        return user
# Create your models here.
class Profile(AbstractUser):

    status = (
        ("regular", "regular"),
        ("subscriber", "subscriber"),
    )
    username = models.CharField(unique=False, max_length=25)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, default="regular")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tc = models.BooleanField(default=False)

    objects = ProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "tc"]

    def __str__(self):
        return self.email



