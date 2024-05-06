from django.urls import path
from .views import *

urlpatterns = [
    
    path('', TaskView.as_view()),
    path('<int:pk>/', TaskManageView.as_view()),
]
