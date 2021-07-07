from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .serializers import CreditoDetailSerializer, CreditosListSerializer, CreditoDecisionSerializer
from .models import Credito
import random


# Create your views here.
class CreditosList(generics.ListAPIView):
    serializer_class = CreditosListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset       = Credito.objects.all()
        queryset       = queryset.filter(aprobado=False, denegado=False)
        queryset       = queryset.filter(monto__range=(0, 50000))

        return queryset


class CreditoDetail(generics.RetrieveAPIView):
    queryset = Credito.objects.all()
    serializer_class = CreditoDetailSerializer
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.puntuacionSentinel == 'mala' and obj.deudaSBS > 1000:
            obj.puntuacionIA = random.randint(0, 5)
        else:
            obj.puntuacionIA = random.randint(5, 10)
        obj.save(update_fields=("puntuacionIA", ))
        return super().retrieve(request, *args, **kwargs)


class CreditoDecision(generics.UpdateAPIView):
    queryset = Credito.objects.all()
    serializer_class = CreditoDecisionSerializer
    permission_classes = [IsAdminUser]


class CreditosAprobadosList(generics.ListAPIView):
    serializer_class = CreditosListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset       = Credito.objects.all()
        queryset       = queryset.filter(aprobado=True)

        return queryset