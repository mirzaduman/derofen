from django.shortcuts import render
from .models import Produkt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .serializers import ProduktSerializer


def home(request):
    produkte = Produkt.objects.filter(kategorie__iexact='Brot')
    kategorie = 'Brot'

    if 'Süßwaren' in request.POST:
        produkte = Produkt.objects.filter(kategorie__iexact='Süßwaren')
        kategorie = 'Süßwaren'
    elif 'Kleingebäck' in request.POST:
        produkte = Produkt.objects.filter(kategorie__iexact='Kleingebäck')
        kategorie = 'Kleingebäck'
    elif 'Brot' in request.POST:
        produkte = Produkt.objects.filter(kategorie__iexact='Brot')
        kategorie = 'Brot'

    context = {
        'produkte': produkte,
        'kategorie': kategorie
    }

    return render(request, 'index.html', context)


class ProdukteAPI(APIView):
    def get(self, request, *args, **kwargs):
        produkte = Produkt.objects.all().order_by('-id')
        serializer = ProduktSerializer(produkte, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProduktAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, produkt_id, format=None):
        try:
            produkt = Produkt.objects.get(id=produkt_id)
            serializer = ProduktSerializer(produkt)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(
                {'res': 'Produkt existiert nicht!'},
                status=status.HTTP_404_NOT_FOUND
            )

