from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') #선택적으로 3번째 인자를 받아줄 수 있음

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']  #text에 문자열로 담김
    words = text.split()

    word_dictionary = {}
    for word in words :
        if word in word_dictionary :
            word_dictionary[word] += 1
        else : 
            word_dictionary[word] = 1
    
    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary' :word_dictionary.items()}) 
    #3번째 인자는 딕셔너리로 사용!! #{key : value}

