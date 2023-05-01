import json
from .views import translate
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TranslateTestCase(TestCase):
    def test_translate_word(self):
        url = reverse('translate')
        data = {'text': 'Hello', 'source_lang': 'en', 'target_lang': 'fr'}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_translate_sentence(self):
        url = reverse('translate')
        data = {'text': 'How are you?', 'source_lang': 'en', 'target_lang': 'fr'}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_translate_para(self):
        para = "The best way to win a short-term game is to bet it all on one strategy. Someone is going to get lucky and it might be you. But we rarely thrive in the long run if we persist in playing a series of short-term games."
        url = reverse('translate')
        data = {'text': para, 'source_lang': 'en', 'target_lang': 'fr'}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

