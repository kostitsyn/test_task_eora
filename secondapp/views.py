import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MainSerializer

from numpy import percentile, average
from .constants import ANSWER_TYPE_OPERATOR, ANSWER_TYPE_CORRECT, ANSWER_TYPE_REASK, \
    ANSWER_TEXT, REASK_TEXT, SWITCH_TO_OPERATOR


class MainAPIView(APIView):
    """
    ## API бота.
    ### ``Принимает на вход число от 0 до 100``

    **Пример тела запроса:**

        {
            "score": 50
        }

    **Пример тела ответа:**

        {
            "action": "переключаю на оператора"
        }

    ### ``Возможные варианты ответа: 'переключаю на оператора', 'пожалуйста, повторите еще раз', 'ответ'``

    """
    serializer_class = MainSerializer

    def post(self, request):
        score = request.data.get('score')
        with open('table.csv') as f:
            operator_list = []
            reask_list = []
            correct_list = []
            for i in csv.DictReader(f):
                if i['Action'] == ANSWER_TYPE_OPERATOR:
                    operator_list.append(float(i['Score']))
                elif i['Action'] == ANSWER_TYPE_REASK:
                    reask_list.append(float(i['Score']))
                else:
                    correct_list.append(float(i['Score']))

            data_dict = dict(zip((ANSWER_TYPE_OPERATOR, ANSWER_TYPE_REASK, ANSWER_TYPE_CORRECT),
                                 (operator_list, reask_list, correct_list)))

            for key, list_values in data_dict.items():
                q25, q75 = percentile(list_values, 25), percentile(list_values, 75)
                iqr = q75 - q25
                cut_off = iqr * 1.5
                lower, upper = q25 - cut_off, q75 + cut_off

                if key == ANSWER_TYPE_OPERATOR:
                    operator_list = list([x for x in list_values if x >= lower and x <= upper])
                elif key == ANSWER_TYPE_REASK:
                    reask_list = list([x for x in list_values if x >= lower and x <= upper])
                else:
                    correct_list = list([x for x in list_values if x >= lower and x <= upper])
            operator_average = average(operator_list)
            reask_average = average(reask_list)
            correct_average = average(correct_list)
            if score:
                score = float(score)
                if (score > min(operator_list) and score < max(operator_list)) and \
                        (score > min(reask_list) and score < max(reask_list)):
                    if abs(score - operator_average) < abs(score - reask_average):
                        answer = SWITCH_TO_OPERATOR
                    else:
                        answer = REASK_TEXT
                elif score > min(operator_list) and score < max(operator_list):
                    answer = SWITCH_TO_OPERATOR
                else:
                    if (score > min(reask_list) and score < max(reask_list)) and \
                            (score > min(correct_list) and score < max(correct_list)):
                        if abs(score - reask_average) < abs(score - correct_average):
                            answer = REASK_TEXT
                        else:
                            answer = ANSWER_TEXT
                    elif score > min(reask_list) and score < max(reask_list):
                        answer = REASK_TEXT
                    else:
                        answer = ANSWER_TEXT
                response_dict = {'action': answer}
                return Response(response_dict)
            return Response(status=status.HTTP_400_BAD_REQUEST)
