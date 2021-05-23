from django import forms

from .models import Advert

class AdvertAddForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['name', 'price', 'phoneNumber', 'posterName', 'city']

class sortChoice(forms.Form):
	CHOICES = [('pubDate', 'Сортировать по дате'),
				('viewsAmount', 'Сортировать по популярности'),]
	choice = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect, label = 'Сортировка по', required = False)