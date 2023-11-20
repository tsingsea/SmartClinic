import xlwt
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clinic
from .forms import ClinicForm

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinic/clinic_list.html', {'clinics': clinics})

def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    return render(request, 'clinic/clinic_detail.html', {'clinic': clinic})

def clinic_new(request):
    if request.method == "POST":
        form = ClinicForm(request.POST)
        if form.is_valid():
            clinic = form.save()
            return redirect('clinic_detail', pk=clinic.pk)
    else:
        form = ClinicForm()
    return render(request, 'clinic/clinic_edit.html', {'form': form})

def clinic_edit(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == "POST":
        form = ClinicForm(request.POST, instance=clinic)
        if form.is_valid():
            clinic = form.save()
            return redirect('clinic_detail', pk=clinic.pk)
    else:
        form = ClinicForm(instance=clinic)
    return render(request, 'clinic/clinic_edit.html', {'form': form})

def clinic_delete(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    clinic.delete()
    return redirect('clinic_list')

def export_clinics_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="clinic_data.xls"'

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Clinic Data')

    # Write header row
    header_row = ['名称', '地址', '法定代表人', '主要负责人', '诊疗科目', '服务方式', '备案编号', '所有制形式',
                  '经营性质', '行政审批机关', '备案日期', '备案有效期（月）', '备案到期']
    for col_num, header in enumerate(header_row):
        worksheet.write(0, col_num, header)

    # Write data rows
    clinics = Clinic.objects.all()
    for row_num, clinic in enumerate(clinics, 1):
        worksheet.write(row_num, 0, clinic.name)
        worksheet.write(row_num, 1, clinic.address)
        worksheet.write(row_num, 2, clinic.legal_representative)
        worksheet.write(row_num, 3, clinic.principal)
        worksheet.write(row_num, 4, clinic.medical_subjects)
        worksheet.write(row_num, 5, clinic.service_mode)
        worksheet.write(row_num, 6, clinic.record_number)
        worksheet.write(row_num, 7, clinic.ownership_form)
        worksheet.write(row_num, 8, clinic.business_nature)
        worksheet.write(row_num, 9, clinic.administrative_approval)
        worksheet.write(row_num, 10, clinic.record_date.strftime('%Y-%m-%d'))
        worksheet.write(row_num, 11, clinic.record_validity_period)
        worksheet.write(row_num, 12, clinic.record_expiry_date.strftime('%Y-%m-%d'))

    workbook.save(response)
    return response