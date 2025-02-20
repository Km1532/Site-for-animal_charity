from django import forms
from .models import AdoptionRequest

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['adopter_name', 'adopter_email', 'message']
        labels = {
            'adopter_name': 'Ваше ім’я',
            'adopter_email': 'Ваш Email',
            'message': 'Повідомлення',
        }
        help_texts = {
            'message': 'Напишіть, чому ви хочете забрати цю тварину',
        }
