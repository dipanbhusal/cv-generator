import os 
from django.conf import settings 
from django.http import HttpResponse
from django.template.loader import get_template   
import pdfkit

class Render:
    @staticmethod
    def cvRender(path: str, params: dict):  
        template  =get_template(path)
        html = template.render(params)
        options = {
         'dpi': 365,
         'page-size': 'A4',
         'margin-top': '0.25in',
         'margin-right': '0.25in',
         'margin-bottom': '0.25in',
         'margin-left': '0.25in',
         'encoding': "UTF-8",
         'custom-header' : [
            ('Accept-Encoding', 'gzip')
         ],
         'no-outline': None,
        } 
        cv_pdf = pdfkit.from_string(html, False, options=options ) 
        response = HttpResponse(cv_pdf, content_type ='application/pdf')
        return response 