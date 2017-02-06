from django.db import models

# Create your models here.
class Contact(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
        text_area = models.TextField()

        class Meta:
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __str__(self):
                return self.nome
