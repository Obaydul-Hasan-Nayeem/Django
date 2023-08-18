from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# cookie =======================================
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim') # key value pair hishebe cookie er moddhe set hoye jabe
    # response.set_cookie('name', 'karim', max_age=5) # 5 sec pore remove hoye jabe
    # response.set_cookie('name', 'karim', max_age=60*3) 3 min pore...
    response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7)) # 7 din pore...
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name' : name})

def delete_cookie(request):
    response = render(request, 'del.html')
    response.delete_cookie('name')
    return response

# Django session ======================
def set_session(request):
    data = {
        'name' : 'Nayeem',
        'age' : 23,
        'language' : 'English'
    }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    request.session.update(data)
    # request.session.update('name', 'rahim') # akta data dite hole
    return render(request, 'home.html') # home page jokhon render hobe tokhon session ta set hobe


# def get_session(request):
#     name = request.session.get('name', 'Guest')
#     age = request.session.get('age')
#     return render(request, 'get_session.html', {'name' : name, 'age': age})

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')
        request.session.modified = True # 10 sec er moddhe abr req korle next 10 sec er jonno autometically abr name ta set hoye jabe
        return render(request, 'get_session.html', {'name' : name})
    else:
        return HttpResponse("Your session has been expired.")



def delete_session(request):
    # del request.session['name'] # akta data delete korte
    request.session.flush()
    return render(request, 'del.html')