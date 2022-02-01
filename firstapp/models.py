from django.db import models


class User(models.Model):
    guessed_cat_count = models.IntegerField(default=0, verbose_name='Сколько раз загадан кот')
    guessed_bread_count = models.IntegerField(default=0, verbose_name='Cколько раз загадан хлеб')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь №{self.id}'


class Question(models.Model):
    text_question = models.CharField(max_length=512, verbose_name='Текст вопроса')


class AffirmativeAnswer(models.Model):
    ANSWERS = (
        (0, 'да'),
        (1, 'конечно'),
        (2, 'ага'),
        (3, 'пожалуй')
    )
    answer = models.IntegerField(choices=ANSWERS, verbose_name='Вариант утвердительного ответа')


class NegativeAnswer(models.Model):
    ANSWERS = (
        (0, 'нет'),
        (1, 'нет, конечно'),
        (2, 'ноуп'),
        (3, 'найн')
    )
    answer = models.IntegerField(choices=ANSWERS, verbose_name='Вариант отрицательного ответа')


class DialogItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    affirmative_answer = models.ForeignKey(AffirmativeAnswer, blank=True, null=True, on_delete=models.CASCADE)
    negative_answer = models.ForeignKey(NegativeAnswer, blank=True, null=True, on_delete=models.CASCADE)


# class Dialog(models.Model):
#
#     dialog_item_id = models.ForeignKey(DialogItem, on_delete=models.CASCADE)