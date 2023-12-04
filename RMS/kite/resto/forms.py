from django import forms
from .models import Booking
from .models import Contact

class userdetails(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class messageform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 60}),
        }