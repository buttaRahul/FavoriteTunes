from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Artist,Song
from django.http import HttpResponse
# Create your views here.


def helloTemplate(request):
    return TemplateResponse(request,'hello.html',{})


def hellExtTemplate(request):
    return TemplateResponse(request,'helloext.html',{
        "title": "TOm",
        "name" : "Tom Cat",
    })

def songsView(request):

    songsQuerySet = Song.objects.all()
    songsList = [{"title":song.title, "artist": song.artist.name} for song in songsQuerySet ]
    return TemplateResponse(request,'songs.html',{
        "songs": songsList
    })



def artistsView(request):

    artist_id = request.GET.get("id")
    if artist_id:
        artist = Artist.objects.get(id = artist_id)
        songsList = artist.songs.all()
        songsList = [song.title for song in songsList]
        context = {
            "artist": artist.name,
            "songs": songsList,
        }

        return TemplateResponse(request,"artistDetails.html",context)
    artistsQuerySet = Artist.objects.all()
    artistList = [{"name":artist.name, "url":f"{request.build_absolute_uri()}?id={artist.id}" }for artist in artistsQuerySet]

    return TemplateResponse(request,"artists.html",{
        "artists":artistList,

    })

def newArtistView(request):
    context = {
        "errors": [],
        "message": "",
    }

    
    if request.method == "POST":
        print("DICT",request.POST)
        name = request.POST.get("name")
        if name == "":
            context["errors"].append("Name Cannot Be Blank")
        else:
         
            print("NAME",name)
            newArtist = Artist.objects.create(name = name)
            context["message"] = f"New Artist Created With ID {newArtist.id}"
        #  return HttpResponse(f"<h1>  </h1>")
    return TemplateResponse(request,'artistNew.html',context)

def newSongView(request):
    

    artists = Artist.objects.all()
    artistList = [ {"id":artist.id, "name":artist.name} for artist in artists]

    context = {
        "errors": {},
        "message" : "",
        "artists" : artistList
    }

    
    if request.method == "POST":

        
        title = request.POST.get("title")
        artist_id = request.POST.get("artist")

        print("ARTIST: ",artist_id)
        if title == "":
            context["errors"]["title"] = "Name Cannot Be Blank"
        elif artist_id == "":
            context["errors"]["artist"] = "Artist Not Selected"
            print("Artist is empty")
        
        else:
            artist = Artist.objects.get(id = artist_id)
            newSong = Song.objects.create(title = title,artist = artist)
            context['message'] = f"New Song Added with ID {newSong.id}"

    

    return TemplateResponse(request,"songNew.html",context)

def catalogView(request):

    artists = Artist.objects.all()
    artistList = [ {"id":artist.id, "name":artist.name, "total":artist.songs.count() } for artist in artists]
    context = {
        "artists" : artistList,
    }
    return TemplateResponse(request,"catalog.html",context)