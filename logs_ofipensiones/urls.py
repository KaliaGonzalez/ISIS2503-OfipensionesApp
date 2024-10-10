from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('logs/', views.logs_list),
    path('logcreate/', csrf_exempt(views.log_create), name='logCreate'),
]