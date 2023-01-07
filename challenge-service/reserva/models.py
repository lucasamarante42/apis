from django.db import models
from anuncio.models import Anuncio
import uuid

class Reserva(models.Model):
	id = models.AutoField(db_column='id',
						primary_key=True)

	codigo_reserva = models.CharField(db_column='codigo_reserva',
								max_length=100,
								null=False,
								blank=False,
								default=uuid.uuid4)

	id_anuncio = models.ForeignKey(Anuncio,
								db_column='id_anuncio',
								related_name='reserva',
								null=False,
								blank=False,
								on_delete=models.PROTECT)

	data_check_in = models.DateField(db_column='data_check_in',
								null=False,
								blank=False,
								auto_now=False,
								auto_now_add=False)

	data_check_out = models.DateField(db_column='data_check_out',
								null=False,
								blank=False,
								auto_now=False,
								auto_now_add=False)

	preco_total = models.DecimalField(db_column='preco_total',
								null=True,
								blank=True,
								max_digits=12,
								decimal_places=2)

	comentario = models.CharField(db_column='comentario',
								max_length=500,
								null=True,
								blank=True)

	quantidade_hospede = models.IntegerField(db_column='quantidade_hospede',
								null=False,
								blank=False)

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
		db_table = 'reserva'

	def __str__(self):
		return '%s' % (self.id)