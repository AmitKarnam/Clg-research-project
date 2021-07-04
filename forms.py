from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

from account.models import Account,publication,research_grant,consultancy,patent

from django.forms import ModelForm

class RegistrationsForm(UserCreationForm):
    email = forms.EmailField(max_length=75,help_text="Required. Add a valid email address")

    class Meta:
        model = Account
        fields = ['email','username','PF_number','designation','mobile_number','department','password1','password2']


class AddPublicationForm(ModelForm):
    date_of_publication = forms.DateField(help_text=" 'YYYY/MM/DD' format only.")
    class Meta:
        model = publication
        fields = '__all__'

class AddResearchGrantForm(ModelForm):
    class Meta:
        model = research_grant
        fields = '__all__'

class AddConsultancyWorkForm(ModelForm):
    class Meta:
        model = consultancy
        fields = '__all__'

class AddPatentForm(ModelForm):
    class Meta:
        model = patent
        fields = '__all__'