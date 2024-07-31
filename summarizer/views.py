from django.shortcuts import render
from django.http import JsonResponse
from .utils import getTextSummary

# Create your views here.

def summarize(request):
    if request.method == 'POST':
        source_text = request.POST.get('source_text')
        summary = getTextSummary(source_text)

        if summary is None:
            return JsonResponse({'error': 'Translation failed'}, status=500)
        else:
            return JsonResponse(summary)

    return render(request, 'summarizer/index.html')