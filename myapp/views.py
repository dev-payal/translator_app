from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator
from .cache import TranslationCache
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

translator = Translator()

@csrf_exempt
def translate(request):
    if request.method == 'POST':
        # handle POST requests
        translate_data = JSONParser().parse(request)
        if translate_data is not None:
            text = translate_data["text"]
            source_lang = translate_data["source_lang"]
            target_lang = translate_data["target_lang"]
            
            print(text, source_lang, target_lang)

            # Check if the translation exists in cache
            cache = TranslationCache()
            translation = cache.get_translation(text, source_lang, target_lang)
            if translation:
                print("Found in cache!")
                return JsonResponse({'translation': translation})

            print("Not found in cache!")

            try:
                # If not in cache, translate the text using Google Translate API
                translation = translator.translate(text, dest=target_lang).text
                print("translation", translation)
                # Add the translation to cache for future use
                cache.add_translation(text, source_lang, target_lang, translation)
                return JsonResponse({'translation': translation})
            except Exception as e:
                print(e)
                return JsonResponse({'error': "Translation failed. Something went wrong!."})

        else:
            return JsonResponse({'error': "No data found!!"})

    return JsonResponse({'error': 'Invalid request method.'})
