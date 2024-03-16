from django.urls import path
from measurement.views import CreateSensor, RetrieveUpdateSensor, AddMeasurement, MeasurementListCreate

urlpatterns = [
    #TODO: зарегистрируйте необходимые маршруты
    # path('sensors/', CreateSensor.as_view()),
    # path('measurements/', AddMeasurement.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensor.as_view()),
    # path('sensors/', ListCreateSensor.as_view()),
    path('measurements/', MeasurementListCreate.as_view())
]
