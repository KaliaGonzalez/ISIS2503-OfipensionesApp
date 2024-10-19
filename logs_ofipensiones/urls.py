from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('logs_ofipensiones/', views.logs_list,name='logs_list'),
    path('logcreate/', csrf_exempt(views.log_create), name='logCreate'),
]