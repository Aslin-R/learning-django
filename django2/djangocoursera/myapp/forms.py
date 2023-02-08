# myapp/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(widget=forms.Textarea,label='Enter something')
    dob=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    gender=forms.ChoiceField(choices=[('M','Male'),('F','Female')],label='Gender')

shifts=(('1','Morning'),('2',"Afternoon"),('3','Evening'))
class InputForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100,required=False)
    shift=forms.ChoiceField(choices=shifts)
    time_log=forms.TimeField(help_text='Enter the time')
