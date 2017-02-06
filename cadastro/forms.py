# -*- coding: utf-8 -*-
from django import forms
from cadastro.models import Inscricao

class InscricaoForm(forms.ModelForm):

        class Meta:
                model = Inscricao
                fields = '__all__' #('nome', 'email', 'text_contato')''
