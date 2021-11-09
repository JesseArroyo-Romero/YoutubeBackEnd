SECRET_KEY = 'django-insecure-g*43$fyu5*r8$m0!wfkuv*39jt1dq)49n7g_xd$m5$)ulv08&$'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_database',
        'USER': 'root',
        'PASSWORD': 'Projects4949*',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
