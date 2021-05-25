from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from .models import Advert
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
class AdvertAddForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['name', 'price', 'phoneNumber', 'posterName', 'city']
        labels = {'name':_('Имя'),'price':_('Цена'), 'phoneNumber':_('Номер телефона'),'posterName':_('Автор'),'city':_('Город')}

class sortChoice(forms.Form):
	CHOICES = [('pubDate', 'Сортировать по дате'),
				('viewsAmount', 'Сортировать по популярности'),]
	choice = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect, label = 'Сортировка по', required = False)

class RegisterForm(UserCreationForm):
    email = EmailField(label='email')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username':_('Логин'),'first_name':_('Имя'),'last_name':_('Фамилия'),'email':_('Email'), 'password1':_('Пароль')}
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'