from django.shortcuts import render, get_object_or_404
from .forms import StudentForm
from .models import Student
from difflib import SequenceMatcher
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import docx2txt


def index(request):
    return render(request, 'student/index.html')


@login_required
def student(request):
    if request.method == 'POST':
        student_form = StudentForm(data=request.POST, files=request.FILES)
        if student_form.is_valid():
            new_form = student_form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, "Assignment submitted successfully")
        else:
            messages.error(request, "Error submitting")
    else:
        student_form = StudentForm()
    return render(request, 'student/upload.html', {'student_form': student_form})


def perform_plagiarism(request, id):
    student = get_object_or_404(Student, id=id)
    current_doc = student.document
    read_current_doc = docx2txt.process(current_doc)
    percentage = 0
    student_name = ""
    result = ""
    my_list = []
    all_students = Student.objects.all()
    document_list = []
    for stud in all_students:
        read_doc = docx2txt.process(stud.document)
        document_list.append(read_doc)

    text = docx2txt.process(current_doc)
    for file in range(len(document_list)):
        similarity_ratio = SequenceMatcher(None, text, document_list[file]).ratio()
        for lop in all_students:
            if docx2txt.process(lop.document) == document_list[file]:
                student_name = lop.user

        percentage = similarity_ratio * 100
        rounded_pec = round(percentage, 2)
        result = "The ratio of similarity between {} and {} is {}% ".format(student.user, student_name, rounded_pec)
        my_list.append(result)

    return render(request, 'student/admin.html', {'percentage': percentage,
                                                  'student': student,
                                                  'student_name': student_name,
                                                  'my_list': my_list})
