from django.conf import settings


def settings_to_context(request):
    settings_dict = {}
    # do not include special case methods and attributes
    for setting in filter(lambda x: x.isupper(), dir(settings)):
        settings_dict[setting] = getattr(settings, setting)
    return settings_dict
