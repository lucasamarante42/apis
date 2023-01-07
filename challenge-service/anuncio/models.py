from django.db import models
from imovel.models import Imovel

class Anuncio(models.Model):
	id = models.AutoField(db_column='id',
						primary_key=True)

	id_imovel = models.ForeignKey(Imovel,
								db_column='id_imovel',
								related_name='anuncio',
								null=False,
								blank=False,
								on_delete=models.PROTECT)

	plataforma_publicada = models.CharField(db_column='plataforma_publicada',
								max_length=100,
								null=True,
								blank=True)

	taxa_plataforma = models.DecimalField(db_column='taxa_plataforma',
								null=True,
								blank=True,
								max_digits=12,
								decimal_places=2)

	data_criacao = models.DateTimeField(db_column='data_criacao',
								null=True,
								blank=True,
								auto_now=False,
								auto_now_add=True)

	data_atualizacao = models.DateTimeField(db_column='data_atualizacao',
								null=True,
								blank=True,
								auto_now=True,
								auto_now_add=False)

	data_remocao = models.DateTimeField(db_column='data_remocao',
								null=True,
								blank=True,
								auto_now=False,
								auto_now_add=False)

	class Meta:
		db_table = 'anuncio'

	def __str__(self):
		return '%s' % (self.id)
