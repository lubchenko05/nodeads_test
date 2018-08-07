from rest_framework import status, pagination
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from groups.paginations import StandartPagination
from .serializers import ElementSerializer, GroupDetailSerializer, GroupSerializer
from .models import Element, Group


class ElementByGroupView(ListCreateAPIView):
    model = Element
    permission_classes = [AllowAny]  # TODO: CHANGE IT ON PROD
    serializer_class = ElementSerializer
    queryset = Element.objects.filter(verified=True)
    pagination_class = StandartPagination


class ElementView(ListCreateAPIView):
    model = Element
    permission_classes = [AllowAny]  # TODO: CHANGE IT ON PROD
    serializer_class = ElementSerializer
    queryset = Element.objects.filter(verified=True)
    pagination_class = StandartPagination


class ElementDetailView(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]  # TODO: CHANGE IT ON PROD

    def get(self, request, pk):
        queryset = Element.objects.filter(pk=pk).first()
        serializer_context = {
            'request': request,
        }
        if queryset:
            return Response(ElementSerializer(queryset, context=serializer_context).data)
        else:
            return Response(data={'error': 'Not Found (404)'}, status=status.HTTP_404_NOT_FOUND)


class GroupView(ListCreateAPIView):
    model = Group
    permission_classes = [AllowAny]  # TODO: CHANGE IT ON PROD
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    pagination_class = StandartPagination


class GroupDetailView(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]  # TODO: CHANGE IT ON PROD

    def get(self, request, pk):
        serializer_context = {
            'request': request,
        }
        queryset = Group.objects.filter(pk=pk).first()
        if queryset:
            return Response(GroupDetailSerializer(queryset, context=serializer_context).data)
        else:
            return Response(data={'error': 'Not Found (404)'}, status=status.HTTP_404_NOT_FOUND)
