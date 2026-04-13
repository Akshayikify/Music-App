from django.shortcuts import render
from .models import Song
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    paginator=paginator(Song.objects.all(),1)
    page_number=request.GET.get('page')
    try:
        page_obj=paginator.get_obj(page_number)
    except PageNotAnInteger:
        page_obj=paginator.page(1)
    except EmptyPage:
        page_obj=paginator.page(paginator.num_pages) 
    context={'page_obj':page_obj}
    return render(request,'index.html',context)  
    