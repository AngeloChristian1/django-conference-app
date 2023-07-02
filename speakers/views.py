
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Speaker
from .forms import speakerForm
# Create your views here.


def speaker(request):
    return render(request,'speaker.html')

def create_speaker(request):
    if request.method == 'POST':
        print(request.method)
        speak = request.POST
        name = request.POST["name"]
        organisation = request.POST["organisation"]
        topic = request.POST["topic"]
        address = request.POST["address"]
        biography = request.POST["biography"]
        print(speak)

        new_speaker = Speaker(name = name, organisation = organisation, topic= topic, address= address, biography = biography)
        new_speaker.save()
        return redirect('/speaker/read_all/')

    return render(request,'create_speaker.html')
def read_one_speaker(request, id):
    speaker = Speaker.objects.get(id=id)
    return render(request, 'read_one_speaker.html', {"speaker": speaker})

def read_all_speaker(request):
    speakers = Speaker.objects.all()
    return render(request, 'read_all_speaker.html', {"speakers": speakers})

def delete_speaker(request, id):
    speaker = Speaker.objects.get(id=id)
    if request.method == 'POST':
        Speaker.objects.get(id=id).delete()
        return redirect("/speaker/read_all")
    return render(request, 'delete_speaker.html', context={"speaker": speaker})

def update_speaker(request, id):
    speaker = Speaker.objects.get(id=id)

    if request.method == 'POST':
        print(request.method)
        speak = request.POST
        name = request.POST["name"]
        organisation = request.POST["organisation"]
        topic = request.POST["topic"]
        address = request.POST["address"]
        biography = request.POST["biography"]
        print(speak)

        if len(name) < 0 or len(organisation) < 0 or len(topic) < 0:
            return HttpResponse('Error, Please inputs are non-existing or null')
        else:
            updated_speaker = Speaker(name = name, organisation = organisation, topic= topic, address= address, biography = biography)

            Speaker.objects.filter(id=id).update(name = name, organisation = organisation, topic= topic, address= address, biography = biography)
            return redirect("/speaker/read_all")
    return render(request, 'update_speaker.html', context={"speaker": speaker})

def speaker_form(request):
    form = speakerForm()
    if request.method == 'POST':
        print('Printing POST', request.POST)
        form = speakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/speaker/read_all")
    return render(request, 'speaker_form.html', context={"form": form})

# def speaker_form(request):
#     form = speaker_form()
#     context = {'form', form}
#     return render(request, 'speaker_form.html', context)

def delete_speaker_from_all(request):
    speakers = Speaker.objects.all()

    return render(request, 'read_all_speaker.html', context={"speaker": speakers})
