from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver

import uuid

"""Funcao para gerar ids com a possibilidade quase 0 de serem iguais"""
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

"""Class base para todas as classes herdando de models.MODEL"""
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

"""classe que herda de Base e cria os Planos"""
class Plano(Base):
    nome = models.CharField('Nome', max_length=50)
    valor = models.IntegerField('Valor', null=True)
    qtd_max_telas = models.IntegerField('Quantidade maxima de telas', null=True)


"""classe responsavel pela criação das obras"""
class Obra(Base):
    titulo = models.CharField('Titulo', max_length=100)
    diretor = models.CharField('Diretor', max_length=100)
    genero = models.TextField('Genero', max_length=200)
    like = models.IntegerField('Like', default=0)
    deslike = models.IntegerField('Dislike', default=0)
    imagem = StdImageField('Imagem', upload_to=get_file_path, null=True)
    link = models.URLField('Link', max_length=500, null=True )
    slug = models.CharField(max_length=1000, null=True, blank=True, default=titulo)
    isfilme = models.BooleanField("É um filme?",default=True)
    download = models.IntegerField("Downloads", default=0)
    """metodo responsavel por criar as slugs"""
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)

"""classe responsavel pela criacao da obra - filme"""
class Filme(Obra):
    duracao = models.IntegerField('Duracao', default=0)
    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

"""classe responsavel por criar as obras- series"""
class Serie(Obra):
    qtd_temporadas = models.IntegerField('Quantidade de temporadas', default=1)
    qtd_episodios = models.IntegerField('Quantidade de episodios', default=1)
    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'

"""classe que cria os perfil- esse modelo serve de padrao para o cadastro de usuarios"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()