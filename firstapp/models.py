from django.db import models


class User(models.Model):
    guessed_cat_count = models.IntegerField(default=0, verbose_name='Сколько раз загадан кот')
    guessed_bread_count = models.IntegerField(default=0, verbose_name='Cколько раз загадан хлеб')
    current_stage = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь №{self.id}'


class Question(models.Model):
    text_question = models.CharField(max_length=512, unique=True, verbose_name='Текст вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'Вопрос {self.text_question}'


class QuestionStep(models.Model):
    ANSWER_TYPE = (
        ('yes', 'yes'),
        ('no', 'no'),
    )

    question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.SET_NULL)
    step = models.IntegerField(default=1, verbose_name='Номер этапа')
    answer_type = models.CharField(max_length=3, blank=True, null=True, choices=ANSWER_TYPE)

    def __str__(self):
        return f'Этап №{self.step} вопроса {self.question.text_question}'


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    affirmative_answer = models.ForeignKey(AffirmativeAnswer, blank=True, null=True, on_delete=models.CASCADE)
    negative_answer = models.ForeignKey(NegativeAnswer, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Диалог'
        verbose_name_plural = 'Диалоги'

    def __str__(self):
        return f'Диалог №{self.id} пользователя №{self.user.id}'
