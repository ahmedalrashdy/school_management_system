from django.shortcuts import render, redirect
from .models import Section, Attendance,AcademicDay
from students.models import *
from school.models import ClassLevel
from django.http import JsonResponse
from . import forms
from django.contrib import messages
from django.shortcuts import get_object_or_404




def load_classes(request):
    academic_year_id = request.GET.get('academic_year_id')
    print("Academic Year ID:", academic_year_id)  # تحقق من القيم الواردة
    # classes = ClassLevel.objects.filter(id=academic_year_id)
    classes = ClassLevel.objects.all()
    classes_list = list(classes.values('id', 'name'))
    print("Classes:", classes_list)  # تحقق من البيانات المرسلة
    return JsonResponse(classes_list, safe=False)

def load_sections(request):
    academic_year_id = request.GET.get('academic_year_id') 
    class_id = request.GET.get('class_id')  
    sections = Section.objects.filter(
        academic_year_id=academic_year_id,
        class_level_id=class_id
    )
    # تحويل البيانات إلى JSON
    sections_list = list(sections.values('id', 'name'))
    print("Filtered Sections:", sections_list)
    return JsonResponse(sections_list, safe=False)

def add_attendance(request):
    section_id = request.POST.get('section_id')
    section = get_object_or_404(Section, id=section_id)
    # جلب آخر يوم أكاديمي
    last_academic_day = AcademicDay.objects.order_by('-date').first()

    if not last_academic_day:
        messages.error(request, "لا يوجد أيام أكاديمية متاحة.")
        return redirect('prepare_attendance')

    if request.method == "POST":
        # معالجة بيانات الحضور
        for key, value in request.POST.items():
            if key.startswith('status_'):
                student_id = key.split('_')[1]
                status = value
                try:
                    student = Student.objects.get(id=student_id, student_section__section=section)
                    # إنشاء أو تحديث سجل الحضور
                    attendance, created = Attendance.objects.get_or_create(
                        student=student,
                        academic_day=last_academic_day,
                        section=section,
                        defaults={'status': status}
                    )
                    if not created:
                        attendance.status = status
                        attendance.save()
                except Student.DoesNotExist:
                    messages.warning(request, f"الطالب بمعرف {student_id} غير موجود في الشعبة المحددة.")
                    continue
        messages.success(request, "تم حفظ الحضور بنجاح.")
        return redirect('prepare_attendance')  # يمكن توجيه المستخدم إلى صفحة أخرى بعد الحفظ

    else:
        # عرض النموذج مع قائمة الطلاب
        students = Student.objects.filter(section=section)
        return render(request, 'attendance_list.html', {
            'students': students,
            'section': section,
            'academic_day': last_academic_day
        })

def prepare_attendance(request):
    students = []  # قائمة الطلاب التي سيتم تعبئتها
    if request.method == "POST":
        academic_year = request.POST.get('academic_year')
        class_ = request.POST.get('class_')
        section = request.POST.get('section')
        students = Student.objects.filter(
            student_section__section=section,
        )
        return render(
                request,
                'attendance_list.html',
                {'students': students, 'section': section}
            )    
    else:
        academic_years = AcademicYear.objects.all()
        form = forms.AttendancePreparationForm()

    return render(request, 'attendance_preparation.html', {'form': form, 'students': students,'academic_years': academic_years})

# def attendance_list(request, section_id):
#     section = Section.objects.get(id=section_id)
#     students = Student.objects.filter(section=section)

#     if request.method == "POST":
#         for student in students:
#             status = request.POST.get(f"status_{student.id}")
#             # حفظ الحضور في قاعدة البيانات
#             forms.Attendance.objects.update_or_create(
#                 student=student,
#                 academic_day=request.POST.get('academic_day'),
#                 defaults={'status': status},
#             )
#         return redirect('attendance_success')

#     return render(request, 'attendance_list.html', {'section': section, 'students': students})

def get_sections_by_class(request):
    """عرض فصل الشعبة بناءً على الاختيار"""
    
    class_id = request.GET.get('class_id')
    if class_id:
        sections = Section.objects.filter(class_obj_id=class_id)
    else:
        sections = Section.objects.none()  # لا يوجد شعبة إذا لم يتم اختيار فصل
    return render(request, 'attendance_form.html', {'sections': sections})



