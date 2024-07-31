from django.shortcuts import render
from django.http import JsonResponse
from .utils import getSentimentAnalysis

# Create your views here.

def analyze(request):
    if request.method == 'POST':
        source_text = request.POST.get('source_text')
        analysis = getSentimentAnalysis(source_text)

        if analysis is None:
            return JsonResponse({'error': 'Translation failed'}, status=500)
        else:
            return JsonResponse(analysis)

    return render(request, 'sentimentAnalyzer/index.html')
