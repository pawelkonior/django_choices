from django import views
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from . import forms
from . import models


class HomeView(generic.ListView):
    queryset = models.Product.objects.all()
    template_name = 'products/home.html'
    context_object_name = 'products'


class AddProductView(views.View):
    def get(self, request):
        form = forms.ProductForm()
        return render(request, 'products/product_create.html', {'form': form})

    def post(self, request):
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('products:home'))
        return render(request, 'products/product_create.html', {'form': form})


class AddProductCustomFormView(views.View):
    categories = [(cat.id, cat.name) for cat in models.Category.objects.all()]
    subcategories = [(scat.id, scat.name) for scat in models.SubCategory.objects.all()]

    def get(self, request):
        form = forms.ProductFormCustom()
        form.fields['category'].choices = self.categories
        form.fields['subcategory'].choices = self.subcategories
        return render(request, 'products/product_create.html', {'form': form})

    def post(self, request):
        form = forms.ProductFormCustom(request.POST)
        form.fields['category'].choices = self.categories
        form.fields['subcategory'].choices = self.subcategories

        if form.is_valid():
            name, prize, description, category, subcategories, *rest = [*form.cleaned_data.values()]

            ct = models.Category.objects.get(pk=category)
            sb = models.SubCategory.objects.filter(pk__in=subcategories)

            product = models.Product(name=name, prize=prize, description=description, category=ct)
            product.save()
            for s in sb:
                product.subcategory.add(s)

            product.save()

            return redirect(reverse('products:home'))
        return render(request, 'products/product_create.html', {'form': form})
