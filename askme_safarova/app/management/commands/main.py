from datetime import datetime
from random import randint, choice

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from app.models import Question, Answer

from app.models import QuestionLike

from app.models import Profile, Tag, AnswerLike


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("ratio", nargs="+", type=int)

    def handle(self, *args, **options):
        ratio = options['ratio'][0]

        # Создаем таблицу зарегистрированных пользователей
        # users = [User(username=f'User name {i}', password=f"No_password") for i in range(1, ratio)]
        # User.objects.bulk_create(users)
        # users = User.objects.all()
        # Profile.objects.bulk_create([Profile(user=u, date_of_register=datetime.now()) for u in users])
        random_users = Profile.objects.all()
        # print(random_users)
        # User.objects.all().delete()

        #tags
        # tag = [Tag(tags=f"Tag {randint(1, 5)}") for i in range(ratio)]
        # Tag.objects.bulk_create(tag)

        #Создаем данные с вопросами
        # new_question = [Question(title=f'Question {i}',
        #                          text=f"Is {i} your favorite number?",
        #                          date=datetime.now(),
        #                          author_id=choice(random_users),
        #                          popularity=randint(1, 1000))
        #                 for i in range(1, ratio)]
        # Question.objects.bulk_create(new_question)

        questions = Question.objects.all()

        # Создаем данные с лайками question
        # like_question = [QuestionLike(question_id=choice(questions), author_id=choice(random_users)) for i in range(ratio)]
        # QuestionLike.objects.bulk_create(like_question)


        #Создаем данные с ответами
        # for i in questions:
        #     new_answers = [Answer(question_id=i,
        #                           text=f'Answer random text Number {j}',
        #                           date_of_register=datetime.now(),
        #                           author_id=choice(random_users),
        #                           popularity=randint(1, 1000)
        #                           ) for j in range(10)]
        #     Answer.objects.bulk_create(new_answers)
        answers = Answer.objects.all()

        # Создаем данные с лайками answer
        like_answer = [AnswerLike(answer_id=choice(answers), author_id=choice(random_users)) for i in range(ratio)]
        AnswerLike.objects.bulk_create(like_answer)