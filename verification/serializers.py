from rest_framework import serializers

from .models import CustomerData,NameMatch,DOBMatch

class CustomerDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerData
        fields = ['cust_id','name', 'father_name', 'dob', 'address', 'doc_type','doc_id','created']

class NameMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameMatch
        fields = ['cust_id','cosine_percentage','reorder_flg']

class DOBMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOBMatch
        fields = ['cust_id','dob_flg','year_flg']


class AccuracySerializer(serializers.Serializer):


    name_match=serializers.SerializerMethodField('get_name_match')
    dob_match=serializers.SerializerMethodField('get_dob_match')

    #print(customers)

    def __init__(self, *args, **kwargs):
        context = kwargs.pop("context")
        self.cust_id = context.get('cust_id')
        super(AccuracySerializer, self).__init__(*args, **kwargs)

    def get_name_match(self, obj):
        print(NameMatchSerializer(
            NameMatch.objects.filter(cust_id=self.cust_id),
            many=True
        ).data)
        return NameMatchSerializer(
            NameMatch.objects.filter(cust_id=self.cust_id),
            many=True
        ).data

    def get_dob_match(self, obj):
        return DOBMatchSerializer(
            DOBMatch.objects.filter(cust_id=self.cust_id),
            many=True
        ).data
