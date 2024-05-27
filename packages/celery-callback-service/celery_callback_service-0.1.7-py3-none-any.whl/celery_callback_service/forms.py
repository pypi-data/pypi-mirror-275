from django.forms import Form
from django.forms.fields import CharField


class CallbackInput(Form):
    uid = CharField(max_length=64, required=True)
