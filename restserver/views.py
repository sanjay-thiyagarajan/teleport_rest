from django.http import HttpResponse
from .models import Person, Office


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
            return HttpResponse({
                "status": "fail",
                "message": "Invalid Credentials"
                })


def signUp(request):
    if request.method == "POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        home_location = request.POST.get("home_location")
        work_pattern = request.POST.get("work_pattern")
        email_address = request.POST.get("email_address")
        password = request.POST.get("password")
        profile_photo = request.POST.get("profile_photo")

        office_name = request.POST.get("office_name")
        office = Office.objects.get(office_name=office_name)

        person = Person(
            name=name,
            gender=gender,
            home_location=home_location,
            work_pattern=work_pattern,
            email_address=email_address,
            password=password,
            office=office,                  # this is a foreign key
            profile_photo=profile_photo
                )

        office.save()
        person.save()


def createOffice(request):
    if request.method == "POST":
        office_name = request.POST.get("office_name")
        office_location = request.POST.get("office_location")

    office = Office(
        office_name=office_name,
        office_location=office_location
            )

    office.save()
