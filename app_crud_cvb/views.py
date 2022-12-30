from django.shortcuts import render
from app_crud_cvb import models as md
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone


# Create your views here.

# CREATE
class Create(CreateView):
    template_name = "App/candidate_form.html"
    model = md.MO_candidates
    fields = '__all__'
    success_url = reverse_lazy('URL_read')

# READ
'''
class Read(ListView):
    model = md.MO_candidates
    paginate_by = 2  # if pagination is desired
    template_name = "App/candidate_list.html"

    # queryset = md.MO_candidates.objects.all()
    # print('XXXXXXXXX')
    # print(queryset)
    # extra_content = {'object_list': 'queryset'}
    # fields = '__all__'
    # success_url = reverse_lazy('URL_read')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        context['object_list'] = md.MO_candidates.objects.all()
        # print(context)
        return context
'''

class Read(ListView):
    context_object_name = 'object_list'
    # queryset = Book.objects.filter(publisher__name='ACME Publishing')
    queryset = md.MO_candidates.objects.all()
    template_name = 'App/candidate_list.html'
    

# UPDATE 
class Update(UpdateView):
    model = md.MO_candidates
    fields = '__all__'
    template_name = "App/candidate_form.html"
    success_url = reverse_lazy('URL_read')

# DELETE 
class Delete(DeleteView):
    model = md.MO_candidates
    context_object_name = 'candidate'
    template_name = "App/candidate_confirm_delete.html"
    success_url = reverse_lazy('URL_read')
