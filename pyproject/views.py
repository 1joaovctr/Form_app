from django.shortcuts import render
from form_app.forms import FormularioDados
from openpyxl import Workbook
from form_app.models import FormData

def formulario(request):
    if request.method == 'POST':
        form = FormularioDados(request.POST)
        if form.is_valid():
            form.save()
            
            #Armazenar os dados no excel 
            workbook = Workbook()
            sheet = workbook.active
            dados = FormData.objects.all()
            for dado in dados:
                sheet.append([dado.nome, dado.email, dado.idade])
            workbook.save('dados_formulario.xlsx')
            
            return render(request, 'sucesso.html')
    else:
        form = FormularioDados()
    return render(request, 'formulario.html', {'form': form})

    
