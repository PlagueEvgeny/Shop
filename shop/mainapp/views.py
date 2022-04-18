from django.shortcuts import render

from mainapp.models import Product, Order, Category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):

        if "search" in self.request.GET:
            search_title = self.request.GET["search"]
            queryset = Product.objects.all()
            return queryset.filter(title__icontains=search_title)
        else:
            queryset = Product.objects.all()
            
        return queryset

class ProductDetailView(DetailView):
    model = Product

