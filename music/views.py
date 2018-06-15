from django.http import HttpResponse
from django.template import loader
from .models import Album
from django.shortcuts import render_to_response


def create(request):
    if request.method == "GET":
       form = ArtistForm();
       return render(request,'music/create.html',{'form':form});
    elif request.method=="POST":
       form=ArtistForm(request.POST); 
       form.save();
       return HttpResponseRedirect('/albums');



def index(request):
    all_albums = Album.objects.all()
    template=loader.get_template('music/index.html')
    context={
        'all_albums':all_albums,
    }
    print(request.COOKIES.get("UserName"))
    return HttpResponse(template.render(context))    

def detail(request, album_id) :
    return HttpResponse("<h2> Details of Album Id:" + str(album_id)+"</h2>")

