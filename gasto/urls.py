from django.urls import path
from .views import GastoCreateView, GastoListView, BuscaGastoListView, ExportarGastoView


gasto_urlpatterns = ([
    path('create',GastoCreateView.as_view(),name='create'),
    path('list',GastoListView.as_view(),name='list'),
    path('buscalist/<slug:mes>/<slug:ano>/',BuscaGastoListView.as_view(),name='buscalist'),
    path('gastolistado/<slug:mes>/<slug:ano>/',ExportarGastoView.as_view(),name='gastolistado'),
],'gasto')
