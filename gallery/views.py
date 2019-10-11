from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.conf.urls import url
from .models import Pics

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
    
def todays_pic(request):
    date = dt.date.today()
    image = Pics.todays_pic()
    
    return render(request, 'everything/todays_pic.html', {"date": date,})

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
    return render(request, 'everything/past_pic.html',{"date": date})

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

# def search(request):
#     if 'picture' in request.GET and request.GET["article"]:
#         search_term = request.GET.get("article")
#         searched_articles = Article.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-news/search.html',{"message":message})