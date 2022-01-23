from django.urls import path
from .views import GradeAPI,ExcelToDatabase,DatabaseToExcel
urlpatterns=[
    path('listcreate/',GradeAPI.as_view()),
    path('exceltodatabase/',ExcelToDatabase.as_view()),
    path('ExcelToDatabase/',DatabaseToExcel.as_view())
]