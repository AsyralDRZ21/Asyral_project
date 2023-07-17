from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Hall, Lecturer, Event, Program
from datetime import datetime
from django.contrib import messages

def homepage(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'homepage.html', context)

def login(request):
    if request.method == 'POST':
        LecturerID = request.POST.get('LecturerID')
        LecturerPass = request.POST.get('LecturerPass')
        lecturer = Lecturer.objects.filter(LecturerID=LecturerID).first()

        if lecturer and lecturer.LecturerPass == LecturerPass:
            return redirect('/LectView/{}/'.format(LecturerID))
        else:
            error_message = "Invalid ID or password"
            return render(request, 'login.html', {'l': LecturerID, 'p': LecturerPass, 'error_message': error_message})
    else:
        return render(request, 'login.html')

from django.contrib.auth.decorators import login_required

def update(request, LecturerID, event_id):
    event = get_object_or_404(Event, pk=event_id)
    halls = Hall.objects.all()
    programs = Program.objects.all()

    if request.method == 'POST':
        # Retrieve the updated values from the request.POST dictionary
        event.EventID = request.POST.get('EventID')
        event.EventDate = request.POST.get('EventDate')

        event_time = request.POST.get('EventTime').replace('.', '').upper()

        try:
            event.EventTime = datetime.strptime(event_time, '%I:%M %p').time()
        except ValueError:
            event.EventTime = datetime.now().time()

        HallID = request.POST.get('HallID')
        ProgramID = request.POST.get('ProgramID')

        hall = get_object_or_404(Hall, HallID=HallID)
        program = get_object_or_404(Program, ProgramID=ProgramID)

        event.HallID = hall
        event.ProgramID = program

        event.save()

        return redirect('LectView', LecturerID=LecturerID)

    context = {
        'event': event,
        'halls': halls,
        'programs': programs,
        'LecturerID': LecturerID,  # Pass LecturerID to the template context
        'event_id': event_id,
    }

    return render(request, 'update.html', context)



def add_event(request, lecturer_id):
    halls = Hall.objects.all()
    programs = Program.objects.all()

    if request.method == 'POST':
        # Retrieve form data
        EventID = request.POST.get('EventID', '')
        EventDate = request.POST.get('EventDate', '')
        EventTime = request.POST.get('EventTime', '')
        HallID = request.POST.get('HallID', '')
        ProgramID = request.POST.get('ProgramID', '')

        hall = get_object_or_404(Hall, HallID=HallID)
        program = get_object_or_404(Program, ProgramID=ProgramID)

        # Retrieve the Lecturer object based on the LecturerID from the logged-in user
        lecturer = get_object_or_404(Lecturer, LecturerID=lecturer_id)

        # Save the event
        data = Event(
            EventID=EventID,
            EventDate=EventDate,
            EventTime=EventTime,
            HallID=hall,
            ProgramID=program,
            LecturerID=lecturer
        )
        data.save()

        return redirect('LectView', LecturerID=lecturer.LecturerID)
    else:
        return render(request, 'add_event.html', {'halls': halls, 'programs': programs, 'lecturer_id': lecturer_id})



def hall_list(request):
    hall = Hall.objects.all()
    return render(request, 'student_list.html', {'hall': hall})

def lecturer_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'lecturer_list.html', {'lecturers': lecturers})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def LectView(request, LecturerID):
    lecturer = get_object_or_404(Lecturer, LecturerID=LecturerID)
    events = Event.objects.filter(LecturerID=lecturer)

    context = {
        'lecturer': lecturer,
        'events': events,
        'LecturerID': LecturerID,  # Pass LecturerID to the template context
    }

    return render(request, 'LectView.html', context)

def registerLect(request):
    return render(request, 'registerLect.html')

def tryreg(request):
    if request.method == 'POST':
        i = request.POST.get('LecturerID')
        LecturerName=request.POST.get('LecturerName')
        LecturerPass=request.POST.get('LecturerPass')

        if Lecturer.objects.filter(LecturerID=i).exists() == True:
            return render(request,'registerLect.html',{'error_message':'Email already exists'})
        else:
            lecturer = Lecturer(
                LecturerID=i,
                LecturerName=LecturerName,
                LecturerPass=LecturerPass
            )

            lecturer.save()

            return redirect('/login/')

def delete_event(request, LecturerID, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('LectView', LecturerID=LecturerID)



from django.shortcuts import redirect, get_object_or_404
def delete_profile(request, lecturer_id):
    # Retrieve the lecturer object
    lecturer = get_object_or_404(Lecturer, LecturerID=lecturer_id)

    if request.method == 'POST':
        # Delete the lecturer profile
        lecturer.delete()
        # You can also perform any additional cleanup or redirect logic here
        return redirect('homepage')  # Redirect to the homepage after deletion

    return render(request, 'delete_profile.html', {'lecturer': lecturer})

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '12345678':
            return redirect('admin_view')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login_admin.html')

def update_profile(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, LecturerID=lecturer_id)

    if request.method == 'POST':
        # Retrieve form data
        LecturerID = request.POST.get('LecturerID', '')
        LecturerName = request.POST.get('LecturerName', '')
        LecturerPass = request.POST.get('LecturerPass', '')

        # Update the lecturer object
        lecturer.LecturerID = LecturerID
        lecturer.LecturerName = LecturerName
        lecturer.LecturerPass = LecturerPass
        lecturer.save()

        return redirect('LectView', LecturerID=lecturer.LecturerID)
    
    return render(request, 'update_profile.html', {'lecturer': lecturer})

def update_admin(request, event_id):
    event = get_object_or_404(Event, EventID=event_id)
    halls = Hall.objects.all()
    programs = Program.objects.all()

    if request.method == 'POST':
        # Retrieve the updated values from the request.POST dictionary
        event.EventID = request.POST.get('event_id')
        event.EventDate = request.POST.get('event_date')

        event_time = request.POST.get('event_time')
        if event_time is not None:
            event_time = event_time.replace('.', '').upper()
        else:
            event_time = ''

        try:
            event.EventTime = datetime.strptime(event_time, '%I:%M %p').time()
        except ValueError:
            event.EventTime = datetime.now().time()

        HallID = request.POST.get('hall_id')
        ProgramID = request.POST.get('program_id')

        hall = get_object_or_404(Hall, HallID=HallID)
        program = get_object_or_404(Program, ProgramID=ProgramID)

        event.HallID = hall
        event.ProgramID = program

        event.save()

        return redirect('/AdminView/')

    context = {
        'event': event,
        'halls': halls,
        'programs': programs,
        'event_id': event_id,
    }

    return render(request, 'update_admin.html', context)




def delete_Event(request, event_id):
    event = get_object_or_404(Event, EventID=event_id)

    if request.method == 'POST':
        # Delete the event
        event.delete()
        return redirect('admin_view')

    return render(request, 'delete_event.html', {'event': event})

def admin_view(request):
    events = Event.objects.all()
    lecturers = Lecturer.objects.all()
    halls = Hall.objects.all()
    programs = Program.objects.all()

    context = {
        'events': events,
        'lecturers': lecturers,
        'halls': halls,
        'programs': programs,
    }

    return render(request, 'AdminView.html', context)


def delete_record(request):
    # Get the record based on the primary key
    record = Event.objects.get(EventDate='2023-06-28')
    record.delete()
    return redirect (request,'login')

