from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import User # The user model uses OneToOneField.
from django.utils.translation import gettext_lazy as _  # This is to get a better reading text.

# Create profile using the Django user's model.
class UserProfile(models.Model):
    ''' user_id, date_of_birth, date_joined'''
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(_('Date joined'))
    date_of_birth = models.DateField(_('Birth date'), help_text="Please use the following format: <em>YYYY-MM-DD</em>.") # Help the user enter date.
    # TODO: add another option here?
