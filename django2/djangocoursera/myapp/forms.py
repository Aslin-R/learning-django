# myapp/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(widget=forms.Textarea,label='Enter something')
    dob=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    gender=forms.ChoiceField(choices=[('M','Male'),('F','Female')],label='Gender')


from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        
