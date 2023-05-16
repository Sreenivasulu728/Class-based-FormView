from django.shortcuts import render
from django.http import HttpResponse
#from app.models import *
from app.forms import *
from django.views.generic import FormView
# Create your views here.
class cbv(FormView):
    template_name='cbv.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('form is submitted successfully')