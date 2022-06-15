from django.db import models


class Teacher(models.Model):
    last_name = models.CharField("Преподаватель", max_length=50)

    def __str__(self):
        return f"{self.last_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Group(models.Model):
    group_name = models.CharField("Группа", max_length=20)

    def __str__(self):
        return f"{self.group_name}"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Cabinet(models.Model):
    cabinet_name = models.CharField("Кабинет", max_length=20)

    def __str__(self):
        return f"{self.cabinet_name}"

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"


class Lesson(models.Model):
    lesson_name = models.CharField("Название пары", max_length=30)

    def __str__(self):
        return f"{self.lesson_name}"

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"


class Subgroups(models.Model):
    subgroups_name = models.CharField("Номер подгруппы", max_length=3, )

    def __str__(self):
        return f"{self.subgroups_name}"

    class Meta:
        verbose_name = "Подгруппа"
        verbose_name_plural = "Подгруппы"


class TimeTable(models.Model):
    number = models.PositiveSmallIntegerField("Номер пары", default=1)
    date = models.DateField("Дата пары")
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, verbose_name="Кабинет", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name="Занятие", on_delete=models.CASCADE)
    subgroups = models.ForeignKey(Subgroups, verbose_name="Подгруппы", on_delete=models.CASCADE)
    reduction = models.BooleanField("Сокращенный день?", default=False)

    def __str__(self):
        return f"{self.date} - {self.teacher.last_name} - {self.group} - {self.cabinet}"

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"