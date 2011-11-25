# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError


class CesarForm(forms.Form):
    
    mensagem = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    chave = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'input-text'}))
    
    def clean_chave(self):
        if self.cleaned_data['chave']:
            if not str(self.cleaned_data['chave']).isdigit():
                raise ValidationError(u"A chave deve ser um número inteiro")
        return self.cleaned_data['chave']
    

class RsaForm(forms.Form):
    
    mensagem = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    p = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'input-text small'}))
    q = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'input-text small'}))
    