from django.urls import path 
from .views import CvFormView, index,FormPdf 
urlpatterns = [
    path('index/', index, name = 'index'),
    path('CvForm/', CvFormView, name='form-fill'), 
    path('Cv/', FormPdf.as_view(), name='cv-pdf'), 

]