from django.core.exceptions import ValidationError
from django.http import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
import json

from ads.models import Ad, Category


def index(request):
    return JsonResponse(
        {
            "status": "ok"
        }, safe=False
    )


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        result = []
        for item in self.object_list:
            result.append({
                "id": item.id,
                "name": item.name,
                "author": item.author,
                "price": item.price
            })

        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        data = json.loads(request.body)
        ad = Ad()
        ad.name = data['name']
        ad.author = data['author']
        ad.price = data['price']
        ad.address = data['address']
        ad.description = data['description']
        ad.is_published = data['is_published']

        try:
            ad.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)
        ad.save()
        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "address": self.object.address,
            "is_published": self.object.is_published
        }, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        result = []
        for item in self.object_list:
            result.append({
                "id": item.id,
                "name": item.name
            })

        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        data = json.loads(request.body)
        category = Category()
        category.name = data['name']
        try:
            category.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)
        category.save()
        return JsonResponse({
            "id": category.pk,
            "name": category.name,
        }, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        }, safe=False, json_dumps_params={'ensure_ascii': False})
