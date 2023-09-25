from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
import json



def index(request):
    print('1')
    if request.method == "POST":
        print('2')
        data = json.loads(request.body.decode("utf-8"))
        user = data["user"]
        color = data["color"]
        count = data["count"]

        if Report.objects.filter(user=user).exists():
            r = Report.objects.get(user = user)
            r.count = count
            r.save()
        else:
            new_r = Report()
            new_r.user = user
            new_r.color = color
            new_r.count = count
            new_r.save()
        
        print(f'how many uers: {Report.objects.count()}')
        for report in Report.objects.all():
            print(f'user: {report.user}')
            print(f'color: {report.color}')
            print(f'count: {report.count}')
    return render(request, "ball2.html",{})

def getReport(request):
    report_list = []
    for report in Report.objects.all():
        report_list.append([report.user, report.color, report.count])
    return HttpResponse(json.dumps(report_list))

# Create your views here.
