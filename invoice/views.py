from django.shortcuts import render
from rest_framework.views import APIView
from .models import Invoice
from .models import Invoice,Invoice_Detail
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .serializers import invoice_Serializer,invoice_Details_Serializer
# Create your views here.


class CreateInvoiceView(CreateAPIView):
    serializer_class = invoice_Details_Serializer
    queryset = Invoice_Detail.objects.all()
    
class InvoiceListView(ListAPIView):
    serializer_class = invoice_Serializer
    queryset = Invoice.objects.all()

class InvoiceDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = invoice_Details_Serializer
    queryset = Invoice_Detail.objects.all()

class InvoiceOnlyView(RetrieveUpdateDestroyAPIView):
    serializer_class = invoice_Serializer
    queryset = Invoice.objects.all()