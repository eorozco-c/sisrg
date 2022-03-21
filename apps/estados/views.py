from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Nombre_estado

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ListaEstados(ListView):
    model = Nombre_estado
    template_name = 'estados/estados_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListaEstados, self).get_context_data(**kwargs)
        context['appname'] = "estados"
        return context
    
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().get(*args, **kwargs)
        return redirect("master:index")