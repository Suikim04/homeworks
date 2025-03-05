from django.shortcuts import render
from django.http import JsonResponse
from .models import Table


def table_list(request):
    if request.method == "GET":
        tables = Table.objects.all()
        return render(request, "tables/tables_list.html", {"tables": tables})

    elif request.method == "POST":
        number = request.POST.get("number")
        seats = request.POST.get("seats")

        if not number or not seats:
            return JsonResponse({"error": "Номер и количество мест обязательны"}, status=400)

        table = Table.objects.create(number=number, seats=seats, is_available=True)
        return JsonResponse(
            {"id": table.id, "number": table.number, "seats": table.seats, "is_available": table.is_available})


def available_tables(request):
    if request.method == "GET":
        available_tables = Table.objects.filter(is_available=True)
        return render(request, "tables/available_tables.html", {"tables": available_tables})

    return JsonResponse({"error": "Метод не поддерживается"}, status=400)
