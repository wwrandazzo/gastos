from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.db.models import Sum, Count
from .models import Gasto
from .forms import GastoForm

# Create your views here.
class GastoCreateView(CreateView):
    model = Gasto
    form_class = GastoForm
    success_url = reverse_lazy('create')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias']= Gasto.objects.values('categoria').annotate(con_cat=Count('categoria')).filter(con_cat__gte=1).order_by('-con_cat')[0:3]
        context['categoriasdos']= Gasto.objects.values('categoria').annotate(con_catdos=Count('categoria')).filter(con_catdos__gte=1).order_by('-con_catdos')[3:]
        context['categoriastres']= Gasto.objects.values('categoria').annotate(con_cattres=Count('categoria')).filter(con_cattres__gte=1).order_by('-con_cattres')[7:]
        return context

class GastoListView(ListView):
    model = Gasto
    ordering = '-fecha'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mes = datetime.now().month
        ano = datetime.now().year
        context['total'] = Gasto.objects.filter(fecha__month=mes, fecha__year=ano).aggregate(total=Sum('importe'))['total']
        context['gasto'] = Gasto.objects.filter(fecha__month=mes, fecha__year=ano)
        meslista= {1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
        context['mes'] = meslista[mes]
        context['ano'] = ano
        return context
 

class BuscaGastoListView (ListView):
    model = Gasto
    ordering = '-fecha'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nromes={'Enero':'01','Febrero':'02','Marzo':'03','Abril':'04','Mayo':'05','Junio':'06',
        'Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'}
        context['total'] = Gasto.objects.filter(fecha__month=nromes[self.kwargs['mes']], fecha__year=self.kwargs['ano']).aggregate(total=Sum('importe'))['total']
        context['gasto'] = Gasto.objects.filter(fecha__month=nromes[self.kwargs['mes']], fecha__year=self.kwargs['ano'])
        context['mes']= self.kwargs['mes']
        context['ano']= self.kwargs['ano']
        return context
