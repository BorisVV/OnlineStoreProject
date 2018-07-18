from django.db import models
from django.contrib.auth.models import User # Import django user model
from django.utils.translation import gettext_lazy as _  # This is to get a better reading text.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(_('Birth date'), help_text="Please use the following format: <em>YYYY-MM-DD</em>.") # Help the user enter date.
