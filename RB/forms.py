from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import ResumeData, CoverLetter


# class UserForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']


class TemplateForm(forms.ModelForm):
    class Meta:
        model = ResumeData
        fields = "__all__"


class CoverForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = "__all__"
