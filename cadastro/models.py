# -*- coding: utf-8 -*-
from django.db import models

class Inscricao(models.Model):
        nome = models.CharField(max_length=200)
        email = models.EmailField(unique=True)
        text_contato = models.TextField()

        class Meta:
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __str__(self):
                return self.nome
