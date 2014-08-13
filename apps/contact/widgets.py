from django.forms import Widget
from django.utils.safestring import mark_safe
from django.utils import datetime_safe


class CalendarWidget(Widget):

    def render(self, name, value, attrs=None):
        if value is None:
            vstr = ''
        elif hasattr(value, 'strftime'):
            vstr = datetime_safe.new_datetime(value).strftime('%m/%d/%y')
        else:
            vstr = value
        id = "id_{0}".format(name)
        inp = '<input type="text" value="{0}" name="{1}" id="{2}" />'.format(
            vstr, name, id)
        scr = '<script type="text/javascript">$(document).ready(function() {$("#%s").datepicker();});</script>' % id

        args = [inp, scr]
        return mark_safe('\n'.join(args))
