from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import truthTable
from .serializers import truthTableSerializer
from django.http import QueryDict

from api.TruthTable.syntacticAnalyzer import *


class solveTruthTable(APIView):

    def get(self, request):

        return Response({'answer':solveTable(request.GET.get('operation'))})

    def post(self):
        pass

