from django.urls import path
from .views import GradeAPI,ExcelToDatabase,DatabaseToExcel,UserRegister,getToken
urlpatterns=[
    path('listcreate/',GradeAPI.as_view()),
    path('exceltodatabase/',ExcelToDatabase.as_view()),
    path('ExcelToDatabase/',DatabaseToExcel.as_view()),
    path('Token/',UserRegister.as_view()),
    path('getToken/<int:id>/',getToken.as_view())
]