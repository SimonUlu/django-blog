# Entry points for extra webserver

- wsgi.py
- asgi.py

for further information check docs under: https://docs.djangoproject.com/en/5.0/howto/deployment/

## By default django does not static files (has to be solved by us)

reason = bad performance when serving it like in dev environment

### Configure django so serve such files via urls.py

- okay for smaller sites


### Configure web server to serve static files and django app

- same server but separate processes are being used (better for performance)

### use a dedicated service for serving uploaded files 

- initial setup is the most complex but offers the best performance

## Settings:

```sh
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_uhqj4vt++cv9oka0+7rw2tb(+c%k_e4fb6x$txqn1)7^p0g=p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["https://your-domain.com"]
```