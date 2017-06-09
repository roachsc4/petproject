from django.db import models
from django_mysql.models import JSONField
from users.models import User


class SpecType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Spec(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    type = models.ForeignKey(SpecType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    trainee = models.ManyToManyField(User, through='TraineeLesson')
    name = models.CharField(max_length=50)
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
    dsc = models.TextField(max_length=500)
    created_date = models.DateTimeField()
    update_date = models.DateTimeField()

    def __str__(self):
        return self.name


class TraineeLesson(models.Model):
    NOT_PASSED = 1
    PASSED = 2
    STATUS_CHOICES = ((NOT_PASSED, 'Not passed'),
                      (PASSED, 'Passed'))

    trainee = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    pass_date = models.DateTimeField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES)


class Attachment(models.Model):
    TEXT = 1
    IMAGE = 2
    PRES = 3
    VIDEO = 4
    TYPE_CHOICES = ((TEXT, 'Text'),
                    (IMAGE, 'Image'),
                    (PRES, 'Presentation'),
                    (VIDEO, 'Video'))

    name = models.CharField(max_length=50)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    created_date = models.DateTimeField()
    #Как правильно хранить видео, презентации и т д в БД?

    def __str__(self):
        return self.name


class Test(models.Model):
    trainee = models.ManyToManyField(User, through='TraineeTest')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    min_score = models.SmallIntegerField()
    max_score = models.SmallIntegerField()
    created_date = models.DateTimeField()
    update_date = models.DateTimeField()

    def __str__(self):
        return self.name


class TraineeTest(models.Model):
    NOT_FINISHED = 1
    PASSED = 2
    FAILED = 3
    STATUS_CHOICES = ((NOT_FINISHED, ' Not finished'),
                      (PASSED, 'Passed'),
                      (FAILED, 'Failed'))

    trainee = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES)
    pass_date = models.DateTimeField()


class Question(models.Model):
    ONE_ANSWER = 1
    MULTI_ANSWER = 2
    FREE_TEXT = 3
    TYPE_CHOICES = ((ONE_ANSWER, 'One answer'),
                    (MULTI_ANSWER, 'Multiple answers'),
                    (FREE_TEXT, 'Free text answer'))

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=2000, blank=True, null=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    additional_params = JSONField()
    created_date = models.DateTimeField()
    update_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_right = models.BooleanField()
    score = models.SmallIntegerField()
    created_date = models.DateTimeField()
    update_date = models.DateTimeField()

    def __str__(self):
        return self.name


class TraineeAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    trainee_test = models.ForeignKey(TraineeTest, on_delete=models.CASCADE)
    additional_params = JSONField()
    is_right = models.BooleanField()

    def __str__(self):
        return 'Answer to: ' + self.question.name








