from django.urls import path
import mainapp.views as mainapp
from django.views.generic import TemplateView

app_name = 'mainapp'

urlpatterns = [
    path('product', mainapp.ProductListView.as_view(), name='product'),
    path('product/<int:pk>', mainapp.ProductListView.as_view(), name='detail_product'),
    path('about', TemplateView.as_view(template_name="about.html")),
    path('', TemplateView.as_view(template_name="index.html")),
]