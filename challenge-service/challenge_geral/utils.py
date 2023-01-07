from datetime import date, datetime, timedelta, timezone



"""
Método: default_message_request

Objetivo: retornar uma mensagem padrão conforme código do
			status retornado da requisição.

Parâmetros:
	status_code => código do status retornado da requisição
	msg => mensagem
"""
def default_message_request(status_code=None, msg=None):
	default_message = {
		200: 'OK',
		201: 'Criado com sucesso.',
		202: 'Aceito',
		204: 'Deletado.',
		400: 'Ops, ocorreu um problema. Revise seus dados!',
		401: 'Ops, não autorizado.',
		403: 'Ops, negação no acesso.',
		404: 'Informação não encontrada.',
		405: 'Operação desconhecida.',
		409: 'Ops, conflito das informações.',
		412: 'Ops, pré-condições não atendidas.',
		500: 'Ops, ocorreu um problema na operação.'
	}

	if msg:
		return {'message': msg}

	return {'message': default_message[status_code]}

"""
Método: check_list_len

Objetivo: checar o tamanho do array.

Parâmetros:
	list_field => lista
"""
def check_list_len(list_field):
	result = False
	if list_field:
		if len(list_field) > 0:
			result = True
	return result

"""
Método: str_upper_or_low

Objetivo: converter string em maiúsculo ou minúsculo.

Parâmetros:
	type_convert => tipo maiúsculo (up) ou minúsculo (low)
	value => valor da string
"""
def str_upper_or_low(type_convert=None, value=None):
	str_formatted = ''
	if value:
		if type_convert == 'up':
			str_formatted = str(value).upper()
		elif type_convert == 'low':
			str_formatted = str(value).lower()
	return str_formatted

"""
Método: show_message_errors

Objetivo: retornar uma mensagem padrão para um atributo do model
			no serializer. Ocorrido no retorno da requisição em
			que o código de status é 400 (bad request).

Parâmetros:
	description_field => nome do atributo
	max_length_field => comprimento máximo da string
	max_digit_field => comprimento máximo de dígitos
	max_decimal_place => comprimento máximo de casas decimais
"""
def show_message_errors(description_field=None, max_length_field=None, max_digit_field=None, max_decimal_place=None):
	dict_messages = {
		'error_messages': {
			'required': 'O campo {} é obrigatório.'.format(description_field),
			'null': 'O campo {} não pode ser nulo.'.format(description_field),
			'blank': 'O campo {} não pode estar em branco.'.format(description_field),
			'does_not_exist': 'O campo {} possui um valor inválido.'.format(description_field),
			'incorrect_type': 'O campo {} possui um tipo incorreto de dado.'.format(description_field),
			'invalid': 'O campo {} possui um valor inválido.'.format(description_field)
		}
	}

	if max_length_field:
		dict_messages['error_messages']['max_length'] = 'O campo {} não pode ter mais que {} caracteres.'.format(description_field, max_length_field)

	if max_digit_field:
		dict_messages['error_messages']['max_digits'] = 'O campo {} não pode ter mais que {} dígitos.'.format(description_field, max_digit_field)

	if max_decimal_place:
		dict_messages['error_messages']['max_decimal_places'] = 'O campo {} não pode ter mais que {} casas decimais.'.format(description_field, max_decimal_place)

	return dict_messages

"""
Método: show_message_to_unique_error

Objetivo: retornar uma mensagem padrão para um atributo do model
			no serializer que é único no banco de dados.
			Ocorrido no retorno da requisição em que o código de
			status é 400 (bad request).

Parâmetros:
	description_field => nome do atributo
"""
def show_message_to_unique_error(description_field):
	return {'unique': 'O campo {} é único e já existe no banco de dados.'.format(description_field)}

"""
Método: show_message_to_boolean_field

Objetivo: retornar uma string padrão conforme variável do tipo
			boolean.

Parâmetros:
	value_field => valor da variável
"""
def show_message_to_boolean_field(value_field=None):
	str_formatted = {
		True: 'SIM',
		False: 'NÃO',
		'true': 'SIM',
		'false': 'NÃO',
		None: None
	}
	return str_formatted.get(value_field)

"""
Método: check_filtered_params_exists

Objetivo: verificação na requisição de remoção de múltiplos objetos =>
			- se existe parâmetros (key/value)
			- se os nomes dos parâmetros são iguais aos nomes dos filtros

Parâmetros:
	params => parâmetros da requisição
	filters => conjunto de filtros
	filtered => queryset(consulta) que foi filtrada
"""
def check_filtered_params_exists(params=None, filters=None, filtered=None):
	if is_empty_dict_params(params) or len([i for i in list(params.keys()) if i in filters]) == 0:
		return []
	return filtered

"""
Método: is_empty_dict_params

Objetivo: verificação do objeto de parâmetros da requisição =>
			- se objeto existe
			- se existe valor (value) no parâmetro (key)

Parâmetros:
	dict_params => objeto de parâmetros
"""
def is_empty_dict_params(dict_params):
	if not dict_params:
		return True
	else:
		for value in dict_params.values():
			if not value:
				return True
		return False

"""
Método: mount_list_ids

Objetivo: montar uma lista de id's

Parâmetros:
	data => objeto da requisição 'request.data' (Objeto)
"""
def mount_list_ids(data):
	lst_ids = []
	for item in data:
		lst_ids.append(item.get('id'))
	return lst_ids

"""
Método: remove_duplicados_in_list

Objetivo: remover duplicidades.

Parâmetros:
	list_to_change => array
"""
def remove_duplicados_in_list(list_to_change=None):
	if list_to_change:
		return list(set(list_to_change))
	return list_to_change

"""
Método: data_mapping_to_serializer

Objetivo: mapeamento id -> instância e id -> data item (request).
	*utilizado para atualização de múltiplos objetos na base de dados.

Parâmetros:
	pkey => nome da coluna chave primária do model (String)
	validated_data => objeto com os valores a serem validados pelo serializers (Objeto)
"""
def data_mapping_to_serializer(pkey, validated_data):
	return {item[pkey]: item for item in validated_data}

"""
Método: data_perform_update

Objetivo: array de itens dos ids mapeados dos objetos.
	*utilizado para atualização de múltiplos objetos na base de dados.

Parâmetros:
	self => instância atual da classe
	instance => objetos da base de dados
	data_mapping => objeto de dicionário ou de classe com atributos (payload)
"""
def data_perform_update(self, instance, data_mapping):
	ret = []
	for obj_id, data in data_mapping.items():
		obj = instance.get(obj_id, None)
		if obj is not None:
			ret.append(self.child.update(obj, data))
	return ret

"""
Método: get_datetime_now

Objetivo: retornar data hora, data ou hora atual.

Parâmetros:
	type_datetime => tipo data hora, data ou hora
"""
def get_datetime_now(type_datetime=None):
	types_datetime = {
		'datetime': datetime.now(),
		'date': datetime.now().date(),
		'time': datetime.now().time(),
		'datetime-utc': datetime.now(timezone.utc)
	}

	return types_datetime.get(type_datetime)