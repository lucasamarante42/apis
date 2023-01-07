from django import template
from challenge_geral.utils import show_message_to_boolean_field

register = template.Library()

@register.filter
def bool_to_str(value):
	if isinstance(value, bool):
		return show_message_to_boolean_field(value)
	return '-'

@register.filter
def percent(value):
	if value:
		return '{} %'.format(value)
	return '-'

@register.filter
def money(value):
	if value:
		return 'R$ {}'.format(value)
	return '-'

@register.filter
def keyvalue(dict, key):
	return dict[key]

@register.filter
def to_int(value):
	if value:
		return int(float(value or 0))
	return '-'