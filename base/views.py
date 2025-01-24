from django.shortcuts import render, redirect

# from .models import Student
from .forms import StudentForm


# def success_view(request):
#     students = Student.objects.all().order_by('id')
#     return render(request, 'base/success.html', {'students': students})




def class_list(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('class_list')  
    else:
        form = StudentForm()

    return render(request, 'base/class_list.html', {'form': form})
