from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta, MO, TU
from django.db.models import Q
from config.settings import USER_RANGE_START, USER_RANGE_END
from django import views
from .models import TimeTable, Teacher, Group, Cabinet
from django.shortcuts import render


def main_page(request):
    teach = Teacher.objects.all().order_by('last_name')
    group = Group.objects.all().order_by('group_name')
    cabinet = Cabinet.objects.all().order_by('cabinet_name')
    search = request.GET.get('search')
    today = date.today()
    previous = today + relativedelta(weekday=MO(-2))
    current = today + relativedelta(weekday=MO(-1))
    next = today + relativedelta(weekday=MO(1))
    if not search == None:
        timetable = TimeTable.objects.filter(
            Q(teacher__last_name=search) | Q(cabinet__cabinet_name=search) | Q(group__group_name__startswith=search), date__range=[datetime.now() - timedelta(days=USER_RANGE_START), datetime.now() + timedelta(days=USER_RANGE_END)]).order_by('-date')

        return render(request, 'lessons_list.html', {
            'search': search,
            'today': today,
            'previous': previous,
            'current': current,
            'next': next,
            'teacher_name': teach,
            'group_name': group,
            'cabinet_name': cabinet,
            'timetable': timetable})
    else:
        return render(request, 'lessons_list.html', {
            'teacher_name': teach,
            'group_name': group,
            'cabinet_name': cabinet})


# class LessonsDetail(views.generic.ListView):
#     model = TimeTable
#     template_name = 'lessons_list.html'
#
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return TimeTable.objects.all().order_by('-date')
#         else:
#             return TimeTable.objects.filter(date__range=[datetime.now() - timedelta(days=USER_RANGE_START),
#                                                          datetime.now() + timedelta(days=USER_RANGE_END)]).order_by('-date')

# def filter_page(request):
#     teach = Teacher.objects.all().order_by('last_name')
#     group = Group.objects.all().order_by('group_name')
#     cabinet = Cabinet.objects.all().order_by('cabinet_name')
#     response_data = {
#         'teacher_name': teach,
#         'group_name': group,
#         'cabinet_name': cabinet,
#     }
#     return render(request, 'lessons_list.html', response_data)


class LessonFilterView(views.generic.ListView):
    model = TimeTable
    template_name = 'lessons_list.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        start_date = self.request.GET.get("date_start")
        end_date = self.request.GET.get("date_end")
        if not self.request.user.is_superuser:
            start_date = ''
            end_date = ''
        if start_date == '' and end_date == '':
            if self.request.user.is_superuser:
                return TimeTable.objects.filter(
                    Q(teacher__last_name=search) | Q(cabinet__cabinet_name=search) | Q(
                        group__group_name__startswith=search
                    )).order_by('-number').order_by('-date')
            else:
                return TimeTable.objects.filter(
                    Q(teacher__last_name=search) | Q(cabinet__cabinet_name=search) | Q(
                        group__group_name__startswith=search
                    ), date__range=[datetime.now() - timedelta(days=USER_RANGE_START),
                                    datetime.now() + timedelta(days=USER_RANGE_END)]).order_by('-date')
        if end_date == '':
            end_date = f'{datetime.now():%Y-%m-%d}'
            return TimeTable.objects.filter(
                Q(teacher__last_name=search) | Q(cabinet__cabinet_name=search) |
                Q(date__range=[start_date, end_date]) | Q(
                    group__group_name__startswith=search
                )).order_by('-number').order_by('-date')
        if start_date == '':
            return TimeTable.objects.filter(
                Q(teacher__last_name=search) | Q(cabinet__cabinet_name=search) | Q(
                    group__group_name__startswith=search
                )).order_by('-number').order_by('-date')
        else:
            if self.request.user.is_superuser:
                return TimeTable.objects.filter(
                    Q(teacher__last_name=search) | Q(cabinet__cabinet_name=search) |
                    Q(date__range=[start_date, end_date]) | Q(
                        group__group_name__startswith=search
                    )).order_by('-number').order_by('-date')
            else:
                return TimeTable.objects.filter(
                    Q(teacher__last_name=search) | Q(cabinet__cabinet_name=search) | Q(
                        group__group_name__startswith=search
                    ), date__range=[datetime.now() - timedelta(days=USER_RANGE_START),
                                    datetime.now() + timedelta(days=USER_RANGE_END)]).order_by('-number').order_by(
                    '-date')
