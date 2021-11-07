from rest_framework import viewsets
from rest_framework.response import Response
from snippet.models import Snippets, Tags
from .serializer import SnippetsSerializer, TagsSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
class SnippetsViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetsSerializer
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'destroy':[IsAuthenticated],
                                    }
    def get_queryset(self):
        snippet = Snippets.objects.all()
        return snippet
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return self.list(request, *args, **kwargs)
    def get_permissions(self):
        try:
            # return permission_classes depending on action 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # when exception occure jump to default permission_classes
            return [permission() for permission in self.permission_classes]
class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = TagsSerializer

    def get_queryset(self):
        tag = Tags.objects.all()
        return tag
