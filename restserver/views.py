from django.http import HttpResponse
from .models import Person


def loginApp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        person = Person.objects.get(email=email, password=password)

        if person is not None:
            return HttpResponse({
                "name": person.name,
                "gender": person.gender,
                "home_location": person.home_location,
                "work_pattern": person.work_pattern,
                "office": person.office.office_name,
                "profile_photo": person.profile_photo,
                "status": "success"
                })
        else:
            return HttpResponse({"status": "fail", "message": "Invalid Credentials"})
