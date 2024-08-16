from django import template

register = template.Library()
# registeration using decorators
@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all various of "arg" from the string!
    """
    return value.replace(arg,'')

register.filter('cut',cut)