from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from django.views.generic import View, UpdateView, FormView
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import urllib.request
from .models import OrchestraMIDI
from .serializers import GetHummingMIDISerializer
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator

from random import sample

HEADER = {
    'Content-Type': 'application/json',
}

# @csrf_exempt
class GetHummingMIDI(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        orchestraMIDI_num = OrchestraMIDI.objects.all().count()
        return Response({"orchestraMIDI_num": orchestraMIDI_num})
    
    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request, *args, **kwargs):
        queryset = OrchestraMIDI.objects.filter(id=request.data['id'])
        serializer = GetHummingMIDISerializer(queryset[0])
        return Response(data=serializer.data)

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(GetHummingMIDI, self).dispatch(request, *args, **kwargs)

class GetHummingMIDIRandom(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        queryset = OrchestraMIDI.objects.all()
        random_num = request.data['random_num']
        if random_num > queryset.count():
            random_num = queryset.count()
        random_idx = sample(range(queryset.count()), random_num)
        random_queryset = [queryset[i] for i in random_idx]
        serializer = GetHummingMIDISerializer(random_queryset, many = True)
        return Response(data=serializer.data)

class GetMyOrche(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        queryset = OrchestraMIDI.objects.filter(owner=request.data['user_id'])
        serializer = GetHummingMIDISerializer(queryset, many = True)
        return Response(data=serializer.data)