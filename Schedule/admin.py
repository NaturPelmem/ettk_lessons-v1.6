from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Teacher, Group, Cabinet, TimeTable, Lesson, Subgroups


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'teacher', 'date', 'group', 'cabinet', 'lesson', 'reduction']
    list_editable = ['number', 'teacher', 'date', 'group', 'cabinet', 'lesson', 'reduction']
    ordering = ['date', 'teacher', 'number']
    search_fields = ['teacher__last_name', 'date', 'group', 'lesson']
    list_filter = (('date', DateRangeFilter),)
    save_as = True


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['last_name__startswith']
    ordering = ['last_name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ['group_name__startswith']
    ordering = ['group_name']


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    search_fields = ['cabinet_name__startswith']
    ordering = ['cabinet_name']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    search_fields = ['lesson_name__startswith']
    ordering = ['lesson_name']


@admin.register(Subgroups)
class SubgroupsAdmin(admin.ModelAdmin):
    search_fields = ['subgroups_name__startswith']
    ordering = ['subgroups_name']


admin.site.site_header = 'ЕЭТК'
admin.site.index_title = 'Админка сайта'
