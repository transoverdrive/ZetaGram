from django.contrib.auth.models import AbstractUser
# from django.core.urlresolvers import reverse
from django.db import models
#from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# from zetagram.images import models as Images_image

class User(AbstractUser):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )
#test msg
    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.TextField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)
    

    def __str__(self):
        return self.username

    @property
    def post_count(self):
        return self.images.all().count()
    
    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def follwing_count(self):
        return self.following.all().count()


