from rest_framework import viewsets
from rest_framework.request import Request


class RequestViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwarg):
        pass