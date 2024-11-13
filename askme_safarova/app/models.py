from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class QuestionManager(models.Manager):
    def best_question(self):
        return self.order_by('popularity')


class ProfileManager(models.Manager):
    pass


class AnswerManager(models.Manager):
    def best_question(self, question_id):
        return self.filter(question_id=question_id)

class TagManager(models.Manager):
    pass

class AnswerlikeManager(models.Manager):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    date_of_register = models.DateTimeField()
    objects = ProfileManager()


class Tag(models.Model):
    tags = models.CharField(max_length=10)
    objects = TagManager()


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField()
    author_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    popularity = models.IntegerField(default=0)
    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    author_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_of_register = models.DateTimeField()
    popularity = models.IntegerField(default=0)
    objects = AnswerManager()

    def __str__(self):
        a = f'Answer {self.question_id}'
        return a


class Like(models.Model):
    pass


class QuestionLike(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["author_id", "question_id"], name="compare_question"),
        ]


class AnswerLike(models.Model):
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    objects = AnswerlikeManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["author_id", "answer_id"], name="compare_answer"),
        ]