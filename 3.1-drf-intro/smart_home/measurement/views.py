# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView


from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, MeasurementsSerializer, SensorSerializer

class CreateSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RetrieveUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
# #
class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# class SensorListCreate(ListCreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer(queryset)


