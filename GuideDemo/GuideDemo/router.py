from rest_framework.routers import DefaultRouter

from request_and_response.api.views import RequestViewSet


router = DefaultRouter()

router.register('request', RequestViewSet, basename='api-request')
