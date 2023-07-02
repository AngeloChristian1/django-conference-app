
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conference
# Create your views here.



def conference(request):
    return render(request,'conference.html')

def create_conference(request):
    if request.method == 'POST':
        conf = request.POST
        title = request.POST["title"]
        organiser = request.POST["organiser"]
        location = request.POST["location"]
        date = request.POST["date"]
        time = request.POST["time"]
        topic = request.POST["topic"]
        print(conf)

        if len(title) <0 or len(organiser)< 0 or len(location) < 0 :
            return HttpResponse('Error, Please inputs are non-existing or null')
        else:
            new_conference = Conference(title=title, organiser=organiser, location=location, date=date, time=time,
                                        about=topic)
            new_conference.save()
            return redirect('/conference/read_all/')

    return render(request,'create_conference.html')
def read_one_conference(request, id):
    conference = Conference.objects.get(id=id)
    return render(request, 'read_one_conference.html', {"conference": conference})

def read_all_conference(request):
    conferences = Conference.objects.all()
    return render(request, 'read_all_conference.html', {"conferences": conferences})

def delete_conference(request, id):
    conference = Conference.objects.get(id=id)
    if request.method == 'POST':
        Conference.objects.get(id=id).delete()
        return redirect("/conference/read_all")
    return render(request, 'delete_conference.html', context={"conference" : conference})

def update_conference(request, id):
    conference = Conference.objects.get(id=id)
    if request.method == 'POST':
        conf = request.POST
        title = request.POST["title"]
        organiser = request.POST["organiser"]
        location = request.POST["location"]
        date = request.POST["date"]
        time = request.POST["time"]
        topic = request.POST["topic"]
        print(conf)

        if len(title) < 0 or len(organiser) < 0 or len(location) < 0:
            return HttpResponse('Error, Please inputs are non-existing or null')
        else:
            updated_conference = Conference(title=title, organiser=organiser, location=location, date=date, time=time,
                                        about=topic)

            Conference.objects.filter(id=id).update(title=title, organiser=organiser, location=location, date=date, time=time,
                                        about=topic)
            return redirect("./")
    return render(request, 'update_conference.html', context={"conference": conference})

