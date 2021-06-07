from .local import *
import django_heroku

ALLOWED_HOSTS = ['explore-naija.herokuapp.com',"www.explore-naija.herokuapp.com"]

SECRET_KEY =  "johndidthis-07-06-2021)h^+_i5s^h$6bim2)p%5we=!3@ob*958o)ttkc$$pdll8=%-t)"

DEBUG = True

STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')

django_heroku.settings(locals())