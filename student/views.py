
from django.http import HttpResponse
from .models import grades
from .serializer import gradeserializer
from rest_framework import generics
from openpyxl import Workbook, load_workbook 
from openpyxl.utils import get_column_letter
import xlsxwriter
import xlrd
# Create your views here.
class GradeAPI(generics.ListCreateAPIView):
    queryset=grades.objects.all()
    serializer_class=gradeserializer

class ExcelToDatabase(generics.CreateAPIView):
    queryset=grades.objects.all()
    serializer_class=gradeserializer
    def get(self, request, *args, **kwargs):
        data=grades.objects.all()
        #print(data[0].name)
        #print()
        wb = load_workbook("grade.xlsx")
        ws = wb.active
        '''for row in range(2,data.count()): 
            for col in range(1,5):
                print(ws[str(get_column_letter(col))+str(row)].value)'''
        for row in range (2,ws.max_row+1):
                
                data=grades.objects.create(
                     name=ws['A'+str(row)].value,
                    maths=ws['B'+str(row)].value,
                    science=ws['C'+str(row)].value,
                    english=ws['D'+str(row)].value
                    )
        return HttpResponse('done',row)

class DatabaseToExcel(generics.ListAPIView):
    queryset=grades.objects.all()
    serializer_class=gradeserializer
    def get(self, request, *args, **kwargs):
        data=grades.objects.all()
        count=grades.objects.count()
        #print(count)
        wb=xlsxwriter.Workbook('grade.xlsx')
        ws=wb.add_worksheet()
        ws.write('A1','NAME')
        ws.write('B1','MATHS')
        ws.write('C1','SCIENCE')
        ws.write('D1','ENGLISH')
        for i in range(2,count+2):
            ws.write('A'+str(i),data[i-2].name)
            ws.write('B'+str(i),data[i-2].maths)
            ws.write('C'+str(i),data[i-2].science)
            ws.write('D'+str(i),data[i-2].english)
        wb.close()
        return HttpResponse('done')