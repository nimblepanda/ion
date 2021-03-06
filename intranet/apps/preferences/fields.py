# -*- coding: utf-8 -*-
from django import forms
from django.core import validators
from django.utils.encoding import force_text


class PhoneField(forms.Field):
    widget = forms.TextInput
    default_error_messages = {'incomplete': 'Please enter a phone number.', 'invalid': 'Please enter a valid phone number.'}

    def __init__(self, *args, **kwargs):
        super(PhoneField, self).__init__(*args, **kwargs)
        self.validators.append(validators.RegexValidator(r'^[\dA-Z]{3}-?[\dA-Z]{3}-?[\dA-Z]{4}$', 'Please enter a valid phone number.'))

    def to_python(self, value):
        """Returns a Unicode object."""
        if value in self.empty_values:
            return ""
        value = force_text(value).strip()
        return value

    @staticmethod
    def prepare_value(value):
        return "" if value == "None" else value

    @staticmethod
    def widget_attrs(_):
        # Max phone number is 15, and US numbers can start with +1, so max length is 17
        return {"maxlength": "17"}
