from rest_framework.response import Response
from .models import DialogItem, AffirmativeAnswer, NegativeAnswer, QuestionStep, User
from .serializers import DialogSerializer, QuestionSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import status


class DialogAPIViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    """
    ## API распознавания объекта.
    ### ``Допустимые варианты сообщения в запросе: “конечно”, “ага”, “пожалуй”, “нет, конечно”, “ноуп”, “найн”``

    **Пример тела запроса:**

        {
            "user_id": "1",
            "message": "конечно"
        }

    **Пример тела ответа:**

        {
            "text_question": "У него есть уши?"
        }
    """
    queryset = DialogItem.objects.all()
    serializer_class = DialogSerializer

    def list(self, request):
        data = QuestionStep.objects.first()
        serailizer = QuestionSerializer(data.question)
        return Response(serailizer.data)

    def create(self, request):
        user, created = User.objects.get_or_create(pk=request.data.get('user_id'))
        data_response = dict()
        user_response = request.data.get('message')
        user_response = user_response.lower()
        affirmative_answers = [i[1] for i in AffirmativeAnswer.answer.field.choices]
        negative_answers = [i[1] for i in NegativeAnswer.answer.field.choices]
        if user_response not in affirmative_answers and user_response not in negative_answers:
            data_response["text_question"] = "Введен неверный ответ"
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user_response in negative_answers:
            if user.current_stage == 1:
                user.guessed_cat_count += 1
                data = QuestionStep.objects.get(step=user.current_stage+1, answer_type='no')
            elif user.current_stage == 2:
                data = QuestionStep.objects.get(step=user.current_stage+1, answer_type='no')
                user.current_stage = 1
                user.guessed_bread_count += 1

            answer_obj, created = NegativeAnswer.objects.get_or_create(answer=negative_answers.index(user_response))
            DialogItem.objects.create(user_id=user.id, question_id=data.question.id, negative_answer=answer_obj)

        if user_response in affirmative_answers:
            if user.current_stage == 1:
                user.current_stage += 1
                data = QuestionStep.objects.get(step=user.current_stage, answer_type='yes')
            elif user.current_stage == 2:
                data = QuestionStep.objects.get(step=user.current_stage + 1, answer_type='yes')
                user.current_stage = 1
                user.guessed_cat_count += 1
            answer_obj, created = AffirmativeAnswer.objects.get_or_create(answer=affirmative_answers.index(user_response))
            DialogItem.objects.create(user_id=user.id, question_id=data.question.id, affirmative_answer=answer_obj)

        user.save()
        data_response["text_question"] = data.question.text_question
        return Response(data_response)
