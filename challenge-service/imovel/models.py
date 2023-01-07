from django.db import models
from challenge_geral.utils import show_message_to_unique_error

class Imovel(models.Model):
	id = models.AutoField(db_column='id',
						primary_key=True)

	codigo_imovel = models.CharField(db_column='codigo_imovel',
								max_length=100,
								unique=True,
								null=False,
								blank=False,
								error_messages=show_message_to_unique_error('codigo_imovel'))

	limite_hospede = models.IntegerField(db_column='limite_hospede',
								null=False,
								blank=False)

	quantidade_banheiro = models.IntegerField(db_column='quantidade_banheiro',
								null=False,
								blank=False)

	aceita_pet = models.BooleanField(db_column='aceita_pet',
								null=True,
								blank=True)

	valor_limpeza = models.DecimalField(db_column='valor_limpeza',
								null=True,
								blank=True,
								max_digits=12,
								decimal_places=2)

	data_ativacao = models.DateField(db_column='data_ativacao',
								null=True,
								blank=True,
								auto_now=False,
								auto_now_add=False)

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
		db_table = 'imovel'

	def __str__(self):
		return '%s' % (self.id)
