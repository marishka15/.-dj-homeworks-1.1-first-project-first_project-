from django.urls import path
from measurement.views import RetrieveUpdateSensor

urlpatterns = [
    #TODO: зарегистрируйте необходимые маршруты
    # path('sensors/<pk>/', ListCreateSensor.as_view()),
    # path('sensors/', CreateSensor.as_view()),
    # path('measurements/', ListCreateMeasurement.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensor.as_view()),
]
