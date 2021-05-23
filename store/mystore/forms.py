from django import forms
from django.forms.fields import EmailField
from .models import Advert
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AdvertAddForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['name', 'price', 'phoneNumber', 'posterName', 'city']

class sortChoice(forms.Form):
	CHOICES = [('pubDate', 'Сортировать по дате'),
				('viewsAmount', 'Сортировать по популярности'),]
	choice = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect, label = 'Сортировка по', required = False)

class RegisterForm(UserCreationForm):
    email = EmailField(label='email')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user