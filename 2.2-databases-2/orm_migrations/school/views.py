from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    students = Student.objects.order_by('group')
    # ordering = 'group'
    # if ordering:
    #     students = Student.objects.order_by([ordering])

    context = {'object_list': students}
    return render(request, template, context)
