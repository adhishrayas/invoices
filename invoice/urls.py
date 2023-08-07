from django.urls import path
from .views import CreateInvoiceView,InvoiceListView,InvoiceDetailView,InvoiceOnlyView

app_name = 'invoices'

urlpatterns = [
    path('create_invoice',CreateInvoiceView.as_view(),name = "Invoice creation"),
    path('',InvoiceListView.as_view(),name = "Invoice List"),
    path('<uuid:pk>/',InvoiceDetailView.as_view(),name = "Invoice Details"),
    path('<uuid:pk>/delete_invoice/',InvoiceOnlyView.as_view(),name = "Invoice Deletion")
]
