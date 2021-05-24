
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'ativo', views.AtivoViewSet)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'deposito', views.DepositoViewSet)
router.register(r'retirada', views.RetiradaViewSet)
router.register(r'saldo', views.SaldoViewSet)
router.register(r'transferencia', views.TransferenciaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]