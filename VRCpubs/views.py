from django.shortcuts import render
from .models import VRCPubs


# Create your views here.

def index(request):
    lst=[]
    years=[]
    CMPN_object=VRCPubs.objects.order_by('-publishedAt')
    for CMPN in CMPN_object:
        if str(CMPN.category).upper() not in lst:
            lst.append(str(CMPN.category))
        print(lst)

        if CMPN.yearpublished() not in years:
            years.append(CMPN.yearpublished())
        
        print(years)
    years=sorted(years, reverse=True)
    print(years)
    print(CMPN_object)
    return render(request,"CMPN/index.html", {'CMPN': CMPN_object, 'Categories':lst, 'years':years})