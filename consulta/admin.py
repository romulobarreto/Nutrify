from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .models import Client, Medication, Exam, AnthropometricEvaluation


# Inline para Medicações
class MedicationInline(admin.TabularInline):  
    model = Medication
    extra = 1  

# Inline para Exames
class ExamInline(admin.TabularInline):  
    model = Exam
    extra = 1  

# Inline para Avaliações Antropométricas
class AnthropometricEvaluationInline(admin.StackedInline):  
    model = AnthropometricEvaluation
    extra = 1

# Função para adicionar texto com quebra automática para textos longos
def add_multiline_text(p, text, x, y, width):
    text_object = p.beginText(x, y)
    text_object.setFont("Helvetica", 11)

    # Define a altura da linha
    line_height = 14  # Ajuste esse valor conforme necessário
    total_lines = 0  # Contador de linhas

    for line in text.split('\n'):
        words = line.split(' ')
        current_line = ''
        
        for word in words:
            # Verifica se adicionar a palavra excede a largura permitida
            if text_object.getX() + p.stringWidth(current_line + ' ' + word, "Helvetica", 11) > x + width:
                text_object.textLine(current_line)  # Adiciona a linha atual
                total_lines += 1  # Incrementa o contador de linhas
                current_line = word  # Começa uma nova linha
            else:
                current_line += ' ' + word if current_line else word

        # Adiciona a última linha
        if current_line:
            text_object.textLine(current_line)
            total_lines += 1  # Incrementa para a última linha

    # Adiciona o texto ao canvas
    p.drawText(text_object)

    # Retorna a nova posição Y
    return y - (total_lines * line_height)

def check_new_page(p, y, height):
    if y <= 40:  # verifica se está próximo do fim da página
        p.showPage()  # cria uma nova página
        p.setFont("Helvetica", 11)  # redefine o tamanho da fonte para 11
        return height - 50  # redefine a altura inicial da nova página
    return y

# Função para exportar dados do cliente para PDF
def exportar_client_pdf(modeladmin, request, queryset):
    # Verifica se há clientes selecionados
    if not queryset.exists():
        return HttpResponse("Nenhum cliente selecionado.", status=400)

    response = HttpResponse(content_type='application/pdf')
    # Use o nome do primeiro cliente no queryset para o nome do arquivo
    client_name = queryset.first().name if queryset.exists() else "Paciente"
    response['Content-Disposition'] = f'attachment; filename="Resumo_Paciente_{client_name}.pdf"'

    # Gerar o PDF
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # Coordenada inicial Y
    y = height - 50

    # Título do PDF
    p.setFont("Helvetica-Bold", 16)
    p.drawString(25, y, "Resumo do Paciente")
    y -= 30  # Espaço abaixo do título

    for client in queryset:
        # Informações Pessoais
        p.setFont("Helvetica-Bold", 12)
        p.drawString(25, y, "Informações Pessoais:")
        y -= 20  # Espaço abaixo do título de informações pessoais
        p.setFont("Helvetica", 11)
        
        # Checa e imprime os atributos que não estão vazios e não são False
        info_pessoal = [
            ("Nome: ", client.name),
            ("Telefone: ", client.phone_number),
            ("Data de Nascimento: ", client.birth_date),
            ("Objetivo: ", client.objective)
        ]
        
        for label, value in info_pessoal:
            if value:  # Verifica se o valor não é vazio e não é False
                p.drawString(25, y, f"{label}{value}")
                y -= 20
                y = check_new_page(p, y, height)

        # Anamnese
        p.setFont("Helvetica-Bold", 12)
        y -= 10
        p.drawString(25, y, "Anamnese:")
        y -= 20
        p.setFont("Helvetica", 11)

        # Campos de Anamnese
        anamnese_fields = [
            ("Altura (cm): ", client.height),
            ("Peso desejado (kg): ", client.desired_weight),
            ("Atividade física: ", client.work),
            ("Qual atividade: ", client.what_work),
            ("Horário de Início: ", client.start_time),
            ("Qualidade do Sono: ", client.sleep),
            ("Comentário sobre o sono: ", client.coment_sleep),
            ("Memória: ", client.memory),
            ("Comentário sobre a memória: ", client.coment_memory),
            ("Estuda: ", client.study),
            ("Horário do estudo: ", client.time_study),
            ("Trabalho: ", client.job),
            ("Horário do trabalho: ", client.time_job),
            ("Outra atividade: ", client.another_activity),
            ("Horário em outra atividade: ", client.time_another),
            ("Quem cozinha na sua casa?: ", client.cook),
            ("Onde você come normalmente?: ", client.where_eat),
            ("Fuma: ", client.smoke),
            ("Quantidade por dia?: ", client.times_smoke),
            ("Doença: ", client.sick),
            ("Qual doença?: ", client.which_sick),
            ("Doenças existentes na família?: ", client.family_sick),
            ("Cirurgia: ", client.cirgury),
            ("Qual cirurgia?: ", client.which_cirgury),
            ("Hábito de fazer dieta: ", client.diet),
            ("Horário de maior apetite: ", client.hungry),
            ("Mastigação: ", client.mastigate),
            ("Ingestão hídrica?: ", client.ih),
            ("Ingere líquidos com as refeições?: ", client.drink_when_eat),
            ("Consumo de fast food ou restaurante?: ", client.restaurant),
            ("Frequência que come fora?: ", client.frequency_rest),
            ("Preferência de sabor: ", client.flavor),
            ("O que ama comer?: ", client.love_eat),
            ("Não come de jeito nenhum?: ", client.hate_eat),
            ("O que aconteceu para você chegar no estado atual?: ", client.what_hapened),
            ("Como é o seu comportamento em relação à comida?: ", client.food_behavior),
            ("Quais são suas maiores dificuldades?: ", client.difficulty),
            ("Existe alguma situação de estresse que você esteja passando nesse momento?: ", client.stress),
            ("Como é a sua vida social?: ", client.social),
            ("O que você veio buscar aqui exatamente?: ", client.search),
            ("Você já tentou chegar nesse resultado outras vezes?: ", client.tryed_before),
            ("Por que até hoje não conseguiu chegar e se manter nele?: ", client.why_get_keep),
            ("De 0 a 10, quanto você está comprometido(a) com o nosso tratamento?: ", client.motivation_number),
            ("O que você espera de mim como sua nutricionista?: ", client.nutritionist),
            ("Diurese: ", client.diuresis),
            ("Função intestinal: ", client.intestine),
        ]

        for label, value in anamnese_fields:
            if value:  # Verifica se o valor não é vazio e não é False
                p.drawString(25, y, f"{label}{value}")
                y -= 20
                y = check_new_page(p, y, height)

    p.showPage()  # Finaliza a página atual
    p.save()  # Salva o PDF
    return response


# Adicionando descrição para a ação
exportar_client_pdf.short_description = "Exportar cliente selecionado para PDF"

# Admin para o modelo Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'birth_date', 'country', 'city', 'objective','is_active',)
    search_fields = ('name', 'country', 'state', 'city', 'neighborhood',)
    ordering = ('name',)  # Ordenar por nome por padrão

    # Fieldsets para agrupar os campos no formulário de admin
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('name', 'cpf', 'birth_date', 'email','phone_number', 'street', 'neighborhood', 'country', 'state', 'city', 'is_active', 'objective')
        }),
        ('Anamnese', {
            'fields': ('height', 'desired_weight', 'work', 'what_work', 'start_time', 'sleep', 'coment_sleep', 'memory', 'coment_memory', 'study', 'time_study', 'job', 'time_job', 'another_activity', 'time_another', 'cook', 'where_eat', 'smoke', 'times_smoke', 'sick', 'which_sick', 'family_sick', 'cirgury', 'which_cirgury', 'diet', 'hungry', 'mastigate', 'ih', 'drink_when_eat', 'restaurant', 'frequency_rest', 'flavor', 'love_eat', 'hate_eat', 'what_hapened', 'food_behavior', 'difficulty', 'stress', 'social', 'search', 'tryed_before', 'why_get_keep', 'motivation_number', 'nutritionist', 'diuresis', 'intestine')
        }),
        ('Deficiências', {
            'fields': (
                'weak_nails', 'stained_nails', 'ribbed_nails', 'wavy_nails', 'hair_loss', 'dry_hair', 'dry_skin', 'dermatitis', 'oily_skin', 'acne', 'inflamed', 'halitosis', 'mouth_ulcer', 'cracked_tongue_middle', 'cracked_tongue_sides', 'whitish_tongue', 'gray_tongue', 'labile_mood', 'irregular_menstrual_cycle', 'tpm', 'colic', 'mastalgia', 'swelling', 'desire_sweets', 'depression', 'anxiety', 'irritability')
        }),
        ('Recordatório habitual', {
            'fields': ('breakfast', 'collation', 'lunch', 'snack', 'dinner', 'supper', 'eat_workout', 'nips', 'favorite_place', 'alcohol')
        }),
    )

    inlines = [MedicationInline, ExamInline, AnthropometricEvaluationInline]  # Relaciona os inlines

    # Adicionando a ação de exportar para PDF
    actions = [exportar_client_pdf]

    class Meta:
        model = Client
