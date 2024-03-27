from django.core.exceptions import ValidationError
import phonenumbers
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    num = phonenumbers.parse(str(value))
    if not phonenumbers.is_valid_number(num):
        raise ValidationError('The phone number is not correct ! Please try again.')


def full_name(value):
    words = value.split()
    if len(words) != 3:
        raise ValidationError("To'liq ism 3ta so'zdan tashkil topishi kerak !")

    for word in words:
        if not word[0].isupper():
            raise ValidationError("Har bir ismning bosh harfi kattada bo'lishi kerak !")

        if len(word) < 3:
            raise ValidationError("To'liq ism 3ta so'zdan tashkil topishi kerak !")

        if len(set(word[:2].lower())) != 2:
            raise ValidationError("Ismlarning boshidagi 2ta harfi bir-biriga o'xshamasligi kerak !")


def address(value):
    x = value.split(" ")
    if len(x) < 3:
        raise ValidationError(_('The address must be 3 words !'), code='invalid_location')
