from django import forms
from django.contrib.auth.models import User
from .models import Resume
class DateInput(forms.DateInput):
 input_type = 'date'
class ResumeForm(forms.ModelForm):
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
 image = forms.ImageField(
  required=False,
  widget=forms.FileInput(attrs={'class': 'form-control'})
  )
 date_birth = forms.DateField(
  required = True,
  # input_formats=['%d-%m-%Y'],
  widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter a date: '}),
  )
 ethnicity = forms.ChoiceField(
  choices = ETHNIC_CHOICES,
  widget=forms.Select(attrs={'class': 'nice-select rounded'}),
 )
 sex = forms.ChoiceField(
  choices = SEX_CHOICES,
  widget=forms.Select(attrs={'class': 'nice-select rounded'}),
 )
 marital_status = forms.ChoiceField(
  choices = MARITAL_CHOICES,
  widget=forms.Select(attrs={'class': 'nice-select rounded'}),
 )
 addressLine1 = forms.CharField(
 required = True,
 widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Address Line 1'}),
 )
 addressLine2 = forms.CharField(
 required=False,
 widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Address Line 2'}),
 )
 suburb = forms.CharField(
 required=True,
 widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Suburb'}),
)
 city = forms.CharField(
 required = True,
 widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter City'}),
 )
 province = forms.ChoiceField(
 choices = PROVINCE_CHOICES,
 widget=forms.Select(attrs={'class': 'nice-select rounded'}),
 )
 phoneNumber = forms.CharField(
 required = True,
 widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Phone Number'}),
 )
 cover_letter = forms.FileField(
 required=False,
 widget=forms.FileInput(attrs={'class': 'form-control'})
 )
 cv = forms.FileField(
 required=False,
 widget=forms.FileInput(attrs={'class': 'form-control'})
 )
class Meta:
 model = Resume
 fields = [
 'image',
 'date_birth',
 'ethnicity',
 'sex',
 'marital_status',
 'addressLine1',
 'addressLine2',
 'suburb',
 'city',
 'province',
 'phoneNumber',
 'cover_letter',
 'cv',
 ]
