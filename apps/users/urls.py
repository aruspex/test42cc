from django.conf.urls import patterns, url


urlpatterns = patterns('apps.users.views',
    url(r'signup/', 'signup_view', name='users_signup'),
)

urlpatterns += patterns('',
    url(
        r'logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name='users_logout'
    ),
    url(
        r'login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'users/login.html'},
        name='users_login'
    ),
)
