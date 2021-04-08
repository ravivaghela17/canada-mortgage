from django.shortcuts import render
import requests
from calc_app.models import Rate
from blog_app.models import Blog
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
import re


def index(request):
    rates = Rate.objects.order_by('rate')[:3]
    blogs = Blog.objects.order_by('created_date_time')[:2]
    return render(request, "index.html", context={"rates": rates, "blogs": blogs})


def calculateAmount(request):

    if request.is_ajax():
        amt = request.POST.get('amount')
        print(amt)
        if(amt.isdigit()):
            if(int(amt) < 0):
                return JsonResponse({"success": False, "err": "Please Valid Amount"}, safe=False)
            year = int(request.POST.get('year'))
            rate = float(request.POST.get('rate'))
            p = float(amt)
            r = (rate/12)/100
            months = year*12
            b = r*pow(1+r, months)
            c = pow(1+r, months)-1
            answer = (p*b/c)
            return JsonResponse({"success": True, "result": round(answer, 2)}, safe=False)
    else:
        return JsonResponse({"success": False, "err": "Not valid request"}, safe=False)
