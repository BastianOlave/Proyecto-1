from django import template

register = template.Library()

@register.filter
def currency_cl(value):
    try:
        value = int(value)
        return "${:,.0f}".format(value).replace(",", ".")
    except:
        return value
