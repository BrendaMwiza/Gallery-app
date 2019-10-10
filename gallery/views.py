from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
    
def todays_pic(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>            
            </body>
        </html>
            '''
    return HttpResponse(html)

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

    photo = Category.days_photo(date)
    return render(request, 'all-photos/past-phots.html',{"date": date,"photo":photo})

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Photos for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)