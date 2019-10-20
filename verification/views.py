import json

from rest_framework.response import Response
from rest_framework import status
from .ml_util_src import ml_main

from .models import CustomerData,DOBMatch,NameMatch
from .serializers import CustomerDataSerializer,AccuracySerializer,DOBMatchSerializer,NameMatchSerializer

from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView



# Create your views here.
def index(request):
    context={}
    return JsonResponse({'foo': 'bar'})

class CustomerDetail(APIView):
    """
    Retrieve, update or delete a customer data instance.
    """
    def get_object(self, pk):
        try:
            return CustomerData.objects.get(pk=pk)
        except CustomerData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerDataSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerDataSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerList(APIView):
    """
        List all customer data, or create a new customer data.
        """


    def get(self, request, format=None):
        snippets = CustomerData.objects.all()
        serializer = CustomerDataSerializer(snippets, many=True)
        # print(serializer.data)
        return_data = []
        person_ids = {}
        accuracy={}

        for i in serializer.data:
            if i['cust_id'] in person_ids:
                person_ids[i['cust_id']].append(i)
            else:
                person_ids[i['cust_id']] = [i]

        for k, v in person_ids.items():

            name = NameMatch.objects.get(cust_id=k)
            name=NameMatchSerializer(name).data
            accuracy['name_match']=name
            do_match=DOBMatch.objects.get(cust_id=k)
            do_match=DOBMatchSerializer(do_match).data

            accuracy['dob_match']=do_match

            return_data.append({'cust_id': k, 'docs': v,'accuracy':accuracy})

        # print(person_ids)
        return Response(return_data)



def update_db(request):
    context={}

    data=ml_main.main()
    data=json.loads(data)
    a_data=data['aadhar_data']
    cust_id=data['cust_id']
    name=a_data['name']
    dob=a_data['dob']
    address=a_data['address']
    doc_type='AADHAR'

    customer_data=CustomerData(cust_id=cust_id,name=name,dob=dob,address=address,doc_type=doc_type)
    customer_data.save()

    p_data = data['pan_data']
    name = p_data['name']
    dob = p_data['dob']
    doc_type = 'PAN'



    customer_data = CustomerData(cust_id=cust_id, name=name, dob=dob, doc_type=doc_type)
    customer_data.save()

    n_data=data['name_match']
    cosine_percentage=n_data['cosine_flag']
    reorder_flg=n_data['reorder_flag']

    name_match=NameMatch(cust_id=cust_id,cosine_percentage=cosine_percentage,reorder_flg=reorder_flg)
    name_match.save()
    dob_data = data['dob_match']
    dob_flag = dob_data['dob_flag']
    yob_flag = dob_data['yob_flag']

    dob_match=DOBMatch(cust_id=cust_id,dob_flg=dob_flag,year_flg=yob_flag)
    dob_match.save()



    #print("**")
    #print(data)

    return JsonResponse(data,safe=False)




