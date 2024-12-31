
GENDER_CHOICES =[('male','ذكر'),('female','أنثى')]
RELATIONSHIP_CHOICES = [
        ('father', 'أب'),
        ('mother', 'أم'),
        ('grandfather', 'جد'),
        ('grandmother', 'جدة'),
        ('uncle', 'عم'),
        ('aunt', 'عمة'),
        ('brother', 'أخ'),
        ('sister', 'أخت'),
        ('other', 'أخرى'),
    ]

STAGE_CHOICES = [
        ('kindergarten', 'رياض الأطفال'),
        ('primary', 'المرحلة الابتدائية'),
        ('middle', 'المرحلة الإعدادية'),
        ('secondary', 'المرحلة الثانوية'),
    ]


SEMESTER_CHOICES=[
    ("first_semester","الفصل الاول"),
    ("second_semester","الفصل الثاني")
]


ATTENDANCE_CHOICES = [
        ('present', 'حاضر'),
        ('absent', 'غائب'),
        ('late', 'متأخر'),
        ('excused', 'معذور'),
    ]

FEES_TYPE_CHOICES = [
        ('tuition', 'رسوم دراسية'),
        ('registration', 'رسوم تسجيل'),
        ('books', 'رسوم كتب'),
        ('transportation', 'رسوم مواصلات'),
        ('activities', 'رسوم أنشطة'),
        ('uniform', 'رسوم زي موحد'),
        ('exam', 'رسوم امتحان'),
        ('other', 'رسوم أخرى'),
    ]



STUDENT_ACADEMIC_RECORD_CHOICES=[
    ("")
]