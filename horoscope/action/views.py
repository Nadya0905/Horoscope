from django.shortcuts import render, HttpResponse
from . import action


def input_request(request):
    if request.method == 'POST':
        horo = request.POST.get("horo")
        period = request.POST.get("period")
        description = ""

        if period == "today":
            description = action.get_today_horo(horo=horo)

        if period == "tomorrow":
            description = action.get_tomorrow_horo(horo=horo)

        if period == "week":
            description = action.get_week_horo(horo=horo)

        if period == "month":
            description = action.get_month_horo(horo=horo)

        if period == "year":
            description = action.get_year_horo(horo=horo)


        return render(request, 'output.html', {"horo": horo, "period": period, "description": description})

    return render(request, 'input.html')


