from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.conf.urls import url
from .models import Pics

# Create your views here.
    
def todays_pic(request):
    date = dt.date.today()
    image = Pics.todays_pic()
    
    return render(request, 'welcome.html', {"date": date,"image":image})

def past_days_pics(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(pics_today)

    image = Pics.day_pic(date)
    return render(request, 'welcome.html',{"date": date,"image":image})

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def search(request):
    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        pictures = Pics.search_by_ciro(search_term)
        message = f"{search_term}"

        return render(request, 'everything/search.html',{"message":message,"pictures": pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'everything/search.html',{"message":message, "pictures": pictures})

def pictureDis(request,picture_id):
    try:
        picture = picture.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"everything/picture.html", {"picture":picture})