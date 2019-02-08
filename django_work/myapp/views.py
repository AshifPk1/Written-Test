from django.shortcuts import render
from . models import Tenant
from django.views.generic import DetailView,CreateView,UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from . filter import TenantFilter

def home(request):
    context = {
        'tenant' : Tenant.objects.all()
    }
    return render(request,'myapp/home.html',context)

class TenantDetailView(DetailView):
    model = Tenant

class TenantCreateView(CreateView):
    model = Tenant
    form = UserCreationForm
    fields = ['name','age','gender','mobile_1','mobile_2','mobile_3','address_1','city','country','location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TenantUpdateView(UpdateView):
    model = Tenant
    form = UserCreationForm
    fields = ['name','age','gender','mobile_1','mobile_2','mobile_3','address_1','city','country','location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TenantDeleteView(DeleteView):
    model = Tenant
    success_url = '/'


def search(request):
    tenant_list = Tenant.objects.all()
    tenant_filter = TenantFilter(request.GET,queryset = tenant_list)
    return render(request,'myapp/tenant_list.html',{'filter':tenant_filter})