import re
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

EG_PHONE_REGEX = re.compile(r"^01[0125][0-9]{8}$")

def validate_egypt_phone(value):
    if not EG_PHONE_REGEX.match(value):
        raise ValidationError("Invalid Egyptian phone number format. It should start with 01 and be followed by 9 digits (e.g., 01012345678).")

class User(AbstractUser):
    phone = models.CharField(
        max_length=11,
        unique=True,
        validators=[validate_egypt_phone],
        verbose_name="Phone Number",
    )

    REQUIRED_FIELDS = ["email", "phone", "first_name", "last_name"]



class Project(models.Model):
    owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title       = models.CharField(max_length=120)
    details     = models.TextField()
    target      = models.DecimalField(max_digits=12, decimal_places=2, help_text="EGP")
    start_date  = models.DateField()
    end_date    = models.DateField()

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("Date error: The end date must be after the start date.")
        if self.start_date < timezone.now().date():
            raise ValidationError("Date error: The start date must be today or in the future.")

    def __str__(self):
        return self.title