import datetime

def current_year_processor(request):
    current_year = datetime.datetime.now().year
    return {
        'year': current_year
    }