from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    # Add phone field manually (since it's not in model)
    phone = forms.CharField(
        required=False,  # Change to True if phone must be required
        label='Phone Number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ' ',
        }),
        error_messages={
            'required': 'Phone number is required.'
        }
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']  # phone is added manually
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'rows': 4,
                'required': True
            }),
        }
        labels = {
            'name': 'Full Name *',   # Add * for required fields visually
            'email': 'Email Address *',
            'subject': 'Subject *',
            'message': 'Message *',
        }
        error_messages = {
            'name': {'required': 'Name is required.'},
            'email': {'required': 'Email is required.'},
            'subject': {'required': 'Subject is required.'},
            'message': {'required': 'Message is required.'},
        }
