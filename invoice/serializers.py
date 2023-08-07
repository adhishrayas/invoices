from rest_framework import serializers
from .models import Invoice,Invoice_Detail
from django.shortcuts import get_object_or_404

class invoice_Serializer(serializers.ModelSerializer):
 
    class Meta:
        model = Invoice
        fields = ('id','date','invoice_no','customer_name',)

 

class invoice_Details_Serializer(serializers.ModelSerializer):
    invoice = invoice_Serializer()
    class Meta:
        model = Invoice_Detail
        fields = ('description','quantity','unit_price','price','invoice',)

    def create(self, validated_data):
        inv_data = validated_data.pop('invoice')
        inv_ob = invoice_Serializer.create(invoice_Serializer(),validated_data=inv_data)
        invoice_details,create = Invoice_Detail.objects.update_or_create(invoice = inv_ob,**validated_data)
        return invoice_details
    
    def update(self,instance,validated_data):
        if 'invoice' in validated_data:
            nested_serializer = self.fields['invoice']
            nested_instance = instance.invoice
            nested_data  = validated_data.pop('invoice')
            nested_serializer.update(nested_instance,nested_data)

        return super(invoice_Details_Serializer,self).update(instance,validated_data)
    
    def delete(self,instance,validated_data):
       if 'invoice' in validated_data:
           nested_data = validated_data.pop('invoice')
           id_ = nested_data.id
           inv_obj = get_object_or_404(Invoice,id = id_)
           inv_obj.delete()
      

 
    
    