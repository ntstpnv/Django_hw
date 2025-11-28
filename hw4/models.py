from random import randint, sample

from django.db import models, transaction
from faker import Faker


class Student(models.Model):
    name = models.CharField(max_length=80, unique=True)

    courses = models.ManyToManyField(
        "Course", through="StudentCourse", related_name="students"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=80, unique=True)

    lecturers = models.ManyToManyField(
        "Lecturer", through="CourseLecturer", related_name="courses"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["student_id", "course_id"]


class CourseLecturer(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer_id = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["course_id", "lecturer_id"]


class Article(models.Model):
    title = models.CharField("Название", max_length=256, unique=True)
    text = models.TextField("Текст", unique=True)
    image = models.ImageField("Изображение")
    published_at = models.DateTimeField("Дата публикации")

    tag_names = models.ManyToManyField("Tag", "articles", through="ArticleTag")

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField("Название раздела", max_length=32, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    article_id = models.ForeignKey("Article", models.CASCADE, "tag_ids")
    tag_id = models.ForeignKey("Tag", models.CASCADE, "tag_ids")
    is_main = models.BooleanField("Основной раздел", default=False)

    class Meta:
        ordering = ["-is_main", "tag_id__name"]
        unique_together = ["article_id", "tag_id"]


class DBManager:
    def __init__(self):
        self.fake = Faker("ru_RU")
        self.students = [Student(name=self.fake.name()) for _ in range(16)]
        self.courses = [Course(name=self.fake.bs()) for _ in range(4)]
        self.lecturers = [Lecturer(name=self.fake.name()) for _ in range(8)]

    def generate(self) -> None:
        with transaction.atomic():
            Student.objects.all().delete()
            Course.objects.all().delete()
            Lecturer.objects.all().delete()

            Student.objects.bulk_create(self.students)
            Course.objects.bulk_create(self.courses)
            Lecturer.objects.bulk_create(self.lecturers)

            [
                student.courses.add(*sample(self.courses, randint(1, 4)))
                for student in self.students
            ]
            [
                course.lecturers.add(*self.lecturers[i * 2 : (i + 1) * 2])
                for i, course in enumerate(self.courses)
            ]

    @staticmethod
    def get_courses():
        return Course.objects.prefetch_related("lecturers", "students")

    @staticmethod
    def get_articles():
        return Article.objects.prefetch_related("tag_ids__tag_id")
