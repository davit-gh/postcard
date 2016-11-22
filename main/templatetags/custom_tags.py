from django import template
from main.forms import ContactusForm
register = template.Library()
@register.simple_tag
def get_contact_form(*args):
	return ContactusForm()