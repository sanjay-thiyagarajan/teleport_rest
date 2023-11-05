from django.http import HttpResponse
from .models import Person, Office


def loginApp(request):
    if request.method == "POST":
        email_address = request.POST.get("email_address")
        password = request.POST.get("password")
        try:
            person = Person.objects.get(email_address=email_address, password=password)

            if person is not None:
                return HttpResponse(str({
                    "name": person.name,
                    "gender": person.gender,
                    "home_location": person.home_location,
                    "work_pattern": person.work_pattern,
                    "office": person.office.office_name,
                    "profile_photo": person.profile_photo
                    }))
            else:
                return HttpResponse(str({
                    "message": "Invalid Credentials",
                    "status": "fail"
                    }))
        except:
            return HttpResponse(str({
                    "message": "Could not get Person Object",
                    "status": "fail"
                }))


def signUp(request):
    if request.method == "POST":
        try:
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
                profile_photo=profile_photo,
                office=office
                    )

            office.save()
            person.save()

            return HttpResponse(str({"Success": "Status"}))

        except:
            return HttpResponse(str({
                "Status": "Error",
                "error": "Unable to create person"
                }))


def getAllOffices(request):
    if request.method == "GET":
        resp = []

        for obj in Office.objects.all().values():
            resp.append(obj)
        return HttpResponse(str(resp))


def createOffice(request):
    if request.method == "POST":
        try:
            office_name = request.POST.get("office_name")
            office_location = request.POST.get("office_location")

            office = Office(
                office_name=office_name,
                office_location=office_location
                    )

            office.save()

            return HttpResponse(str({"Status": "Success"}))

        except:
            return HttpResponse(str({
                "Status": "Error",
                "error": "Unable to create office"
                }))
