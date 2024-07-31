from django.shortcuts import render
from django.http import JsonResponse
from .utils import translate_text


def translate(request):
    languages = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('ta', 'Tamil'),
        ('hi', 'Hindi'),
        ('ja', 'Japanese'),
        # Add more languages as needed
    ]

    if request.method == 'POST':
        source_text = request.POST.get('source_text')
        source_language = request.POST.get('source_language')
        target_language = request.POST.get('target_language')

        translated_text = translate_text(source_text, source_language, target_language)

        if translated_text is None:
            return JsonResponse({'error': 'Translation failed'}, status=500)
        else:
            return JsonResponse({'translated_text': translated_text})

    return render(request, 'translator/index.html', {'languages': languages})
