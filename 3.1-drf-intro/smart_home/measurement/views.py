# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView


from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


# class CreateSensor(CreateAPIView):
#     def post(self, request):
#         return Response({
#             "name": "ESP32",
#             "description": "Датчик на кухне за холодильником"
#         })

class RetrieveUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def patch(self, request, *args, **kwargs):
        return Response({"description": "Перенес датчик на балкон"})

# class ListCreateSensor(ListCreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer

#     def post(self, request, *args, **kwargs):
#         return Response({
#             "name": "ESP32",
#             "description": "Датчик на кухне за холодильником"
#         })

# class ListCreateMeasurement(ListCreateAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer
#     def post(self, request, *args, **kwargs):
#         return Response({"sensor": 1, "temperature": 22.3})


