from decimal import Decimal as D
from decimal import InvalidOperation

from babel.numbers import format_currency
from django import template
from django.conf import settings
from django.utils.translation import get_language, to_locale

register = template.Library()


@register.filter(name='currency')
def currency(value, currency=None):
    """
    Format decimal value as currency
    """
    if currency is None:
        currency = ''

    try:
        value = int(value)
    except (TypeError, InvalidOperation):
        return ""
    # Using Babel's currency formatting
    # http://babel.pocoo.org/en/latest/api/numbers.html#babel.numbers.format_currency
    OSCAR_CURRENCY_FORMAT = "x"
    kwargs = {
        'currency': currency,
        'locale': to_locale(get_language() or settings.LANGUAGE_CODE)
    }
    if isinstance(OSCAR_CURRENCY_FORMAT, dict):
        kwargs.update(OSCAR_CURRENCY_FORMAT.get(currency, {}))
    else:
        kwargs['format'] = OSCAR_CURRENCY_FORMAT
    return format_currency(value, **kwargs)
