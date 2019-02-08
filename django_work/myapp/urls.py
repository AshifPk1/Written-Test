
from django.urls import path
from . import views
from . views import TenantDetailView,TenantCreateView,TenantUpdateView,TenantDeleteView

urlpatterns = [
    path('',views.home,name='home'),
    path('tenant/<int:pk>/',TenantDetailView.as_view(),name='tenant_detail'),
    path('tenant/new/',TenantCreateView.as_view(),name='tenant_creat'),
    path('tenant/<int:pk>/update/',TenantUpdateView.as_view(),name='tenant_update'),
    path('tenant/<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),
    path('tenant/search/',views.search,name='search'),

]
