SECRET_KEY = '5qwj-)5_6s!%79a(r&$cn#v3u)@2sn&1&hshj(+_jz3v779_-_'
CLOUDINARY = {
    'cloud_name': 'heroku-image-genghiscode',
    'api_key': '198194936266624',
    'api_secret': 'Sufk2LuruqBR3NXljQ6fvCK6XUY'
}
# Zoho Email Settings ...
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'contato@genghiscode.com.br'
EMAIL_HOST_PASSWORD = 'n7Sk8V1w07yx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'Equipe Genghiscode <contato@genghiscode.com.br>'

# EMAIL_HOST_PASSWORD = 'kurRrqPEcmpN' # Antiga
# EMAIL_HOST_PASSWORD = 'b7G9jTj9wmqa'

RECAPTCHA_PUBLIC_KEY = '6LdWrZIaAAAAAAAaj3zTkbd7z9ct2TAXR-OErZ8X'
RECAPTCHA_PRIVATE_KEY = '6LdWrZIaAAAAAHlj7Rnj7YY3FquBmEoPHY-gPegb'

# 'rest_framework.authentication.SessionAuthentication',
# "rest_framework.authentication.TokenAuthentication",
# "rest_framework.authentication.BasicAuthentication",
# 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',


# urlpatterns = [

# path('habilidades/', HabilidadesApiViews.as_view(), name='habilidades'),
# path('habilidades/<int:pk>/', HabilidadesApiViews.as_view(), name='habilidade'),
# path('formaPagamentos/', FormaPagamentosAPIView.as_view(), name='forma_pagamentos'),
# path('formaPagamentos/<int:pk>/', FormaPagamentoAPIView.as_view(), name='forma_pagamento'),
# path('tipoPrestadores/', TipoPrestadoresAPIView.as_view(), name='tipo_prestadores'),
# path('tipoPrestadores/<int:pk>/', TipoPrestadorAPIView.as_view(), name='forma_pagamento'),
# path('prestadores/', PrestadoresAPIView.as_view(), name='prestadores'),
# path('prestadores/<int:pk>/', PrestadorAPIView.as_view(), name='prestador'),
# path('clientes/', ClientesAPIView.as_view(), name='clientes'),
# path('clientes/<int:pk>/', ClienteAPIView.as_view(), name='cliente'),
# path('statusServicos/', StatusServicosAPIView.as_view(), name='status_servicos'),
# path('statusServicos/<int:pk>/', StatusServicoAPIView.as_view(), name='status_servico'),
# path('agendaServicos/', AgendaServicosAPIView.as_view(), name='agenda_servicos'),
# path('agendaServicos/<int:pk>/', AgendaServicoAPIView.as_view(), name='agenda_servico'),

# ]
