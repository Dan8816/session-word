from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
# the index function is called when root is visited
def index(request):
    if "list" not in request.session:
        request.session['list']=[]
    context = {
        list:request.session['list']
    }
    return render(request, 'session_words/index.html', context)

def add(request):
        request.session['word'] = request.POST['word']
        request.session['time'] = strftime("%Y-%m-%d %H:%M %p", localtime())
        if 'color' not in request.POST:
            request.session['color'] = 'black'       
        else:
            request.session['color'] = request.POST['color']

        temp_list = request.session['list']

        temp_list.append({'words': request.session['word'], 'color': request.session['color'], 'time': 
        
        request.session['time']})

        request.session['list'] = temp_list

        print(request.session['list'])
        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')

# Create your views here.