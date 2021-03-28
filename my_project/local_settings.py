SECRET_KEY = '5qwj-)5_6s!%79a(r&$cn#v3u)@2sn&1&hshj(+_jz3v779_-_'
CLOUDINARY = {
    'cloud_name': 'heroku-image-genghiscode',
    'api_key': '198194936266624',
    'api_secret': 'Sufk2LuruqBR3NXljQ6fvCK6XUY'
}

# Zoho Email Settings ...
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'contato@genghiscode.com.br'
# EMAIL_HOST_PASSWORD = 'kurRrqPEcmpN' # Antiga
EMAIL_HOST_PASSWORD = 'b7G9jTj9wmqa'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'Equipe Genghiscode <contato@genghiscode.com.br>'