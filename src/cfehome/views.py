from django.shortcuts import render
from visits.models import PageVisit

def home_page(request, *args, **kwargs):    
    
    queryset = PageVisit.objects.all()
    PageVisit.objects.create()
    
    context = {
        "title": "My Page",
        "visit_count": queryset.count()
    }
    
    return render(request, 'home.html', context)