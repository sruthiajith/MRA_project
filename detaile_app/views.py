from django.shortcuts import render
from MovieRecommender.models import Movie
from django.db.models import Q
# Create your views here.
def movieDetail(request,movie_id):
        detail = Movie.objects.get(id=movie_id)
        return render(request, 'detailes.html', {'detail': detail})

def SearchResult(request):
    movie=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movie=Movie.objects.all().filter(Q(title__contains=query) | Q(genres__contains=query) | Q(movieduration__contains=query))
        return render(request,'search.html',{'query':query,'movies':movie})
