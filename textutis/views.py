# I have created this file - Aadarsh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def removepunc(request):
    djtxt = request.GET.get('text', 'default')
    print(djtxt)

    removepunc = request.GET.get('removepunc','default')

    fullcaps = request.GET.get('full_caps', 'off')

    newlinerem = request.GET.get('newline_remove', 'off')

    spacerem = request.GET.get('space_remover', 'off')

    charcount = request.GET.get('character_count', 'off')

    if removepunc == 'on':
        punc = ''' ,.';:'*%# '''

        analyzed_txt = ""

        for char in djtxt:
            if char not in punc:
                analyzed_txt += char


        params = {'purpose':'To Remove the Puctuation','analysed_text':analyzed_txt}

        return render(request, 'about.html', params)
        # return HttpResponse("<h1>GO to previous</h1> <a href='/'>Back</a>")

    elif fullcaps == 'on':
        captxt = ''

        for char in djtxt:
            captxt += char.upper()

        params = {'purpose': 'To Capitalize the text', 'analysed_text': captxt}
        return render(request, 'about.html', params)

    elif(newlinerem == 'on'):

        line_remove = ''
        for char in djtxt:
              if char != "\n":
                  line_remove += char

        params = {'purpose':'To Capitalize the text', 'analysed_text': line_remove}
        return render(request, 'about.html', params)

    elif (spacerem == 'on'):

        sremtxt = ''
        for index, char in enumerate(djtxt):
            if djtxt[index] == ' ' and djtxt[index+1] == ' ':
                pass
            else:
                sremtxt += char
        params = {'purpose': 'To Capitalize the text', 'analysed_text': sremtxt}
        return render(request, 'about.html', params)

    elif (charcount == 'on'):

        count = 0

        for char in djtxt:
            count += 1

        params = {'purpose': 'The Number of Charters are ', 'analysed_text': count}
        return render(request, 'about.html', params)

    else:
        return HttpResponse("Error")


def ex1(request):
    return render (request, "Navigator.html")
