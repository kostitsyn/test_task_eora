from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Question, QuestionStep
from .serializers import QuestionSerializer


class TestViewSet(APITestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/'
        self.user = User.objects.create()

    def test_check_first_answer(self):
        response = self.client.get(self.url)
        answer_text = 'Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?'
        self.assertEqual(response.data.get('text_question'), answer_text)

    def test_check_first_negative_answer(self):
        data = {'user_id': self.user.id, 'message': 'нет'}
        response = self.client.post(self.url, data, format='json')
        answer_text = 'Это кот, а не хлеб! Не ешь его!'
        self.assertEqual(response.data.get('text_question'), answer_text)

    def test_check_second_negative_answer(self):
        data = {'user_id': self.user.id, 'message': 'да'}
        self.client.post(self.url, data, format='json')
        data = {'user_id': self.user.id, 'message': 'нет'}
        response = self.client.post(self.url, data, format='json')
        answer_text = 'Это хлеб, а не кот! Ешь его!'
        self.assertEqual(response.data.get('text_question'), answer_text)

    def test_check_first_positive_answer(self):
        data = {'user_id': self.user.id, 'message': 'да'}
        response = self.client.post(self.url, data, format='json')
        answer_text = 'У него есть уши?'
        self.assertEqual(response.data.get('text_question'), answer_text)

    def test_check_second_positive_answer(self):
        data = {'user_id': self.user.id, 'message': 'да'}
        self.client.post(self.url, data, format='json')
        data = {'user_id': self.user.id, 'message': 'да'}
        response = self.client.post(self.url, data, format='json')
        answer_text = 'Это кот, а не хлеб! Не ешь его!'
        self.assertEqual(response.data.get('text_question'), answer_text)

    def test_check_wrong_answer(self):
        data = {'user_id': self.user.id, 'message': 'spam'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_similar_positive_answers(self):
        similar_answers = ('конечно', 'ага', 'пожалуй')
        for answer in similar_answers:
            data = {'user_id': self.user.id, 'message': answer}
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_similar_negative_answers(self):
        similar_answers = ('нет, конечно', 'ноуп', 'найн')
        for answer in similar_answers:
            data = {'user_id': self.user.id, 'message': answer}
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
