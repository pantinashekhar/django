from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
import random
# Create your models here.
class Resume(models.Model):
 BLACK = 'Black'
 WHITE = 'White'
 COLOURED = 'Coloured'
 INDIAN = 'Indian'
 CHINESE = 'Chinese'
 MALE = 'Male'
 FEMALE = 'Female'
 OTHER = 'Other'
 MARRIED = 'Married'
 SINGLE = 'Single'
 WIDOWED = 'Widowed'
 DIVORCED = 'Divorced'
 GAUTENG = 'Gauteng'
 MPUMALANGA = 'Mpumalanga'
 FREE_STATE = 'Free-state'
 NORTH_WEST = 'North-west'
 LIMPOPO = 'Limpopo'
 WESTERN_CAPE = 'Western-cape'
 NOTHERN_CAPE = 'Nothern-cape'
 EASTERN_CAPE = 'Eastern-cape'
 KWAZULU_NATAL = 'Kwazulu-natal'
 ETHNIC_CHOICES = [
 (BLACK, 'Black'),
 (WHITE, 'White'),
 (COLOURED, 'Coloured'),
 (INDIAN, 'Indian'),
 (CHINESE, 'Chinese'),
 ]
 SEX_CHOICES = [
 (MALE, 'Male'),
 (FEMALE, 'Female'),
 (OTHER, 'Other'),
 ]
 MARITAL_CHOICES = [
 (MARRIED, 'Married'),
 (SINGLE, 'Single'),
 (WIDOWED, 'Widowed'),
 (DIVORCED, 'Divorced'),
 ]
 PROVINCE_CHOICES = [
 (GAUTENG, 'Gauteng'),
 (MPUMALANGA, 'Mpumalanga'),
 (FREE_STATE, 'Free-state'),
 (NORTH_WEST, 'North-west'),
 (LIMPOPO, 'Limpopo'),
 (WESTERN_CAPE, 'Western-cape'),
 (NOTHERN_CAPE, 'Nothern-cape'),
 (EASTERN_CAPE, 'Eastern-cape'),
 (KWAZULU_NATAL, 'Kwazulu-natal'),
  ]
 IMAGES = [
 'profile1.jpg', 'profile2.jpg', 'profile3.jpg', 'profile4.jpg', 'profile5.jpg',
 'profile6.jpg', 'profile7.jpg', 'profile8.jpg', 'profile9.jpg', 'profile10.jpg',
 ]
 user = models.OneToOneField(User, on_delete = models.CASCADE)
 uniqueId = models.CharField(null=True, blank=True, max_length=100)
 image = models.ImageField(default='default.jpg', upload_to='profile_images')
 email_confirmed = models.BooleanField(default=False)
 date_birth = models.DateField(blank=True, null=True)
 ethnicity = models.CharField(choices=ETHNIC_CHOICES, default=BLACK, max_length=100)
 sex = models.CharField(choices=SEX_CHOICES, default=OTHER, max_length=100)
 marital_status = models.CharField(choices=MARITAL_CHOICES, default=SINGLE, max_length=100)
 addressLine1 = models.CharField(null=True, blank=True, max_length=200)
 addressLine2 = models.CharField(null=True, blank=True, max_length=200)
 suburb = models.CharField(null=True, blank=True, max_length=100)
 city = models.CharField(null=True, blank=True, max_length=100)
 province = models.CharField(choices=PROVINCE_CHOICES, default=GAUTENG, max_length=100)
 phoneNumber = models.CharField(null=True, blank=True, max_length=100)
 slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
 date_created = models.DateTimeField(default = timezone.now)
 last_updated = models.DateTimeField(blank=True, null=True)
 cover_letter = models.FileField(upload_to='resumes', null=True, blank=True,)
 cv = models.FileField(upload_to='resumes', null=True, blank=True,)
def __str__(self):
 return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId)
def get_absolute_url(self):
 return reverse('resume-detail', kwargs={'slug': self.slug})
def save(self, *args, **kwargs):
#Creating a unique Identifier for the resume(useful for other things in future)
 if self.uniqueId is None:
    self.uniqueId = str(uuid4()).split('-')[0]
    self.slug = slugify('{} {} {}'.format(self.user.first_name,self.user.last_name, self.uniqueId))
#assign a default profile image
 if self.image == 'default.jpg':
        self.image = random.choice(self.IMAGES)
#keep track of everytime someone updates the resume, everytime the instance is saved - this should update
 self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))
 super(Resume, self).save(*args, **kwargs)
 
