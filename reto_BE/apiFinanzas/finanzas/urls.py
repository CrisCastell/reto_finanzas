from django.urls import path
from . import views

urlpatterns = [
    path('creditos' , views.CreditosList.as_view(), name="creditos"),
    path('credito/decision/<int:pk>', views.CreditoDecision.as_view(), name="credito-decision"),
    path('credito/<int:pk>', views.CreditoDetail.as_view(), name="credito-detail"),
    path('creditos/aprobados' , views.CreditosAprobadosList.as_view(), name="creditos"),

]