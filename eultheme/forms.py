'''
Helper classes for forms and widgets.
'''

from django import forms

class TelephoneInput(forms.TextInput):
    'HTML5 telephone input (prompt for numeric entry)'
    input_type = 'tel'
