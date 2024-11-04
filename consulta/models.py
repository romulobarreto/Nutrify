from django.db import models
from localflavor.br.models import BRCPFField
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

class Country(models.Model):
    name = CountryField()

    def __str__(self):
        return self.name

class Client(models.Model):
    SLEEP_CHOICES = [
        ('Ótimo', 'Ótimo'),
        ('Bom', 'Bom'),
        ('Ruim', 'Ruim'),
    ]

    MEMORY_CHOICES = [
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Péssimo', 'Péssimo'),
    ]

    HUNGRY_CHOICES = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
    ]

    MASTIGATE_CHOICES = [
        ('Rápida', 'Rápida'),
        ('Normal', 'Normal'),
        ('Lenta', 'Lenta'),
    ]

    FLAVOR_CHOICES = [
        ('Amargo','Amargo'),
        ('Azedo', 'Azedo'),
        ('Doce', 'Doce'),
        ('Salgado', 'Salgado'),        
    ]

    NUMBER_CHOICES = [
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Nome Completo')
    phone_number = PhoneNumberField(verbose_name='Telefone', region='BR')
    cpf = BRCPFField(verbose_name='CPF', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    street = models.CharField(max_length=255, verbose_name='Endereço')
    neighborhood = models.CharField(max_length=100, verbose_name='Bairro')
    country = CountryField(verbose_name='País')
    state = models.CharField(max_length=2, verbose_name='Estado')
    city = models.CharField(max_length=30, verbose_name='Cidade')
    objective = models.TextField(verbose_name='Objetivo do Paciente', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    height = models.IntegerField(verbose_name="Altura (cm)", null=True, blank=True)
    desired_weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso desejado (kg)", null=True, blank=True)
    work = models.BooleanField(default=True, verbose_name='Atividade física')
    what_work = models.CharField(max_length=200, verbose_name='Qual?', null=True, blank=True)
    start_time = models.CharField(max_length=100, verbose_name='Horário de Início', null=True, blank=True)
    sleep = models.CharField(max_length=10, choices=SLEEP_CHOICES, verbose_name='Qualidade do Sono', default='Ótimo')
    coment_sleep = models.TextField(verbose_name='Comentário', null=True, blank=True)
    memory = models.CharField(max_length=10, choices=MEMORY_CHOICES, verbose_name='Memória', default='Bom')
    coment_memory = models.TextField(verbose_name='Comentário', null=True, blank=True)
    study = models.BooleanField(default=True, verbose_name='Estuda')
    time_study = models.CharField(max_length=100, verbose_name='Horário', null=True, blank=True)
    job = models.BooleanField(default=True, verbose_name='Trabalha')
    time_job = models.CharField(max_length=100, verbose_name='Horário', null=True, blank=True)
    another_activity = models.CharField(max_length=40, verbose_name='Outra atividade', null=True, blank=True)
    time_another = models.CharField(max_length=100, verbose_name='Horário', null=True, blank=True)
    cook = models.CharField(max_length=40, verbose_name='Quem cozinha na sua casa?', null=True, blank=True)
    where_eat = models.CharField(max_length=40, verbose_name='Onde você come normalmente?', null=True, blank=True)
    smoke = models.BooleanField(default=False, verbose_name='Fumo')
    times_smoke = models.CharField(max_length=20, verbose_name='Quantidade por dia?', null=True, blank=True)
    sick = models.BooleanField(default=False, verbose_name='Doença')
    which_sick = models.CharField(max_length=100, verbose_name='Qual doença?', null=True, blank=True)
    family_sick = models.CharField(max_length=100, verbose_name='Doenças existentes na família?', null=True, blank=True)
    cirgury = models.BooleanField(default=False, verbose_name='Cirurgia')
    which_cirgury = models.CharField(max_length=100, verbose_name='Qual cirurgia?', null=True, blank=True) 
    diet = models.BooleanField(default=False, verbose_name='Hábito de fazer dieta')
    hungry = models.CharField(max_length=10, choices=HUNGRY_CHOICES, verbose_name='Horário de maior apetite', default='Noite')
    mastigate = models.CharField(max_length=10, choices=MASTIGATE_CHOICES, verbose_name='Mastigação', default='Normal')
    ih = models.CharField(max_length=20, verbose_name='Ingestão hídrica?', null=True, blank=True)
    drink_when_eat = models.BooleanField(default=True, verbose_name='Ingere líquidos com as refeições?')
    restaurant = models.BooleanField(default=True, verbose_name='Consumo de fast food ou restaurante?')
    frequency_rest = models.CharField(max_length=100, verbose_name='Frequência que come fora?', null=True, blank=True)
    flavor = models.CharField(max_length=10, choices=FLAVOR_CHOICES, verbose_name='Preferência de sabor', default='Salgado')
    love_eat = models.CharField(max_length=100, verbose_name='O que ama comer?', null=True, blank=True)
    hate_eat = models.CharField(max_length=100, verbose_name='Não come de jeito nenhum?', null=True, blank=True)
    what_hapened = models.TextField(verbose_name='O que aconteceu para você chegar no estado atual?', null=True, blank=True)
    food_behavior = models.TextField(verbose_name='Como é o seu comportamento em relação à comida?', null=True, blank=True)
    difficulty = models.TextField(verbose_name='Quais são suas maiores dificuldades?', null=True, blank=True)
    stress = models.TextField(verbose_name='Existe alguma situação de estresse que você esteja passando nesse momento?', null=True, blank=True)
    social = models.TextField(verbose_name='Como é a sua vida social?', null=True, blank=True)
    search = models.TextField(verbose_name='O que você veio buscar aqui exatamente?', null=True, blank=True)
    tryed_before = models.BooleanField(default=True, verbose_name='Você já tentou chegar nesse resultado outras vezes?')
    why_get_keep = models.TextField(verbose_name='por que até hoje não conseguiu chegar e se manter nele?', null=True, blank=True)
    motivation_number = models.CharField(max_length=2, choices=NUMBER_CHOICES, verbose_name='De 0 a 10, quanto você está comprometido(a) com o nosso tratamento?', default='10')
    nutritionist = models.TextField(verbose_name='O que você espera de mim como sua nutricionista?', null=True, blank=True)
    weak_nails = models.BooleanField(default=False, verbose_name='Unhas fracas e quebradiças')
    stained_nails = models.BooleanField(default=False, verbose_name='Unhas com manchas')
    ribbed_nails = models.BooleanField(default=False, verbose_name='Unhas estriadas')
    wavy_nails = models.BooleanField(default=False, verbose_name='Unhas onduladas')
    hair_loss = models.BooleanField(default=False, verbose_name='Queda de cabelo')
    dry_hair = models.BooleanField(default=False, verbose_name='Cabelo seco e quebradiço')
    dry_skin = models.BooleanField(default=False, verbose_name='Pele seca/descamando')
    dermatitis = models.BooleanField(default=False, verbose_name='Dermatite/urticária')
    oily_skin = models.BooleanField(default=False, verbose_name='Pele oleosa')
    acne = models.BooleanField(default=False, verbose_name='Acne')
    inflamed = models.BooleanField(default=False, verbose_name='Gengiva sangrando/inflamada')
    halitosis = models.BooleanField(default=False, verbose_name='Halitose')
    mouth_ulcer = models.BooleanField(default=False, verbose_name='Afta')
    cracked_tongue_middle = models.BooleanField(default=False, verbose_name='Língua rachada (meio)')
    cracked_tongue_sides = models.BooleanField(default=False, verbose_name='Língua rachada (laterais)')
    whitish_tongue = models.BooleanField(default=False, verbose_name='Língua esbranquiçada')
    gray_tongue = models.BooleanField(default=False, verbose_name='Língua acinzentada')
    labile_mood = models.BooleanField(default=False, verbose_name='Humor lábil')
    irregular_menstrual_cycle = models.BooleanField(default=False, verbose_name='Ciclo menstrual irregular')
    tpm = models.BooleanField(default=False, verbose_name='TPM')
    colic = models.BooleanField(default=False, verbose_name='Cólica')
    mastalgia = models.BooleanField(default=False, verbose_name='Mastalgia')
    swelling = models.BooleanField(default=False, verbose_name='Inchaço')
    desire_sweets = models.BooleanField(default=False, verbose_name='Vontade de comer doce')
    depression = models.BooleanField(default=False, verbose_name='Depressão')
    anxiety = models.BooleanField(default=False, verbose_name='Ansiedade')
    irritability = models.BooleanField(default=False, verbose_name='Irritabilidade')
    diuresis = models.CharField(max_length=100, verbose_name='Diurese', null=True, blank=True)
    intestine = models.CharField(max_length=100, verbose_name='Função intestinal', null=True, blank=True)
    breakfast = models.TextField(verbose_name='Desjejum', null=True, blank=True)
    collation = models.TextField(verbose_name='Colação', null=True, blank=True)
    lunch = models.TextField(verbose_name='Almoço', null=True, blank=True)
    snack = models.TextField(verbose_name='Lanche da tarde', null=True, blank=True)
    dinner = models.TextField(verbose_name='Jantar', null=True, blank=True)
    supper = models.TextField(verbose_name='Ceia', null=True, blank=True)
    eat_workout = models.TextField(verbose_name='Pré e pós treino', null=True, blank=True)
    nips = models.TextField(verbose_name='Beliscos', null=True, blank=True)
    favorite_place = models.TextField(verbose_name='Local favorito para comer', null=True, blank=True)
    alcohol = models.TextField(verbose_name='Consumo de álcool', null=True, blank=True)
    

    # Mudar nome da tabela de clientes
    class Meta:
        db_table = 'Paciente'
        verbose_name_plural = 'Pacientes'
        verbose_name = 'Paciente'

    def __str__(self):
        return self.name




class Medication(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100, verbose_name='Medicamento/Suplemento')
    dosage = models.CharField(max_length=50, verbose_name='Dosagem')

    def __str__(self):
        return f"{self.name} ({self.dosage}) - {self.schedule}"

    class Meta:
        verbose_name = "Medicamento/Suplemento"
        verbose_name_plural = "Medicamentos/Suplementos"



class Exam(models.Model):
    EXAM_CHOICES = [
        ('Ácido úrico', 'Ácido úrico'),
        ('Cálcio', 'Cálcio'),
        ('Colesterol', 'Colesterol'),
        ('Creatinina', 'Creatinina'),
        ('Eosinófilo', 'Eosinófilo'),
        ('Eritrócito', 'Eritrócito'),
        ('Ferritina', 'Ferritina'),
        ('Ferro', 'Ferro'),
        ('Filt. Glomerular', 'Filt. Glomerular'),
        ('Glicemia', 'Glicemia'),
        ('HB1AC', 'HB1AC'),
        ('HDL', 'HDL'),
        ('Hematócrito', 'Hematócrito'),
        ('Hemoglobina', 'Hemoglobina'),
        ('Insulina', 'Insulina'),
        ('LDL', 'LDL'),
        ('Plaquetas', 'Plaquetas'),
        ('Sódio', 'Sódio'),
        ('T3', 'T3'),
        ('T4', 'T4'),
        ('TGO', 'TGO'),
        ('TGP', 'TGP'),
        ('Transferrina', 'Transferrina'),
        ('Triglicérideos', 'Triglicérideos'),
        ('TSH', 'TSH'),
        ('Uréia', 'Uréia'),
        ('VCM', 'VCM'),
        ('Vitamina B12', 'Vitamina B12'),
        ('Vitamina B9', 'Vitamina B9'),
        ('Vitamina D', 'Vitamina D'),
        ('Vitamina K', 'Vitamina K'),
        ('Zinco', 'Zinco')
    ]


    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='exams')
    name = models.CharField(max_length=100, choices=EXAM_CHOICES, verbose_name='Exame')
    schedule = models.DateField(verbose_name='Data')
    result = models.CharField(max_length=50, verbose_name='Valor', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.schedule} - {self.result}"

    class Meta:
        verbose_name = "Exame"
        verbose_name_plural = "Exames"


class AnthropometricEvaluation(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='evaluations')
    date = models.DateField(verbose_name="Data da Avaliação")

    imc = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="IMC", null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)", null=True, blank=True)
    forearm = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Antebraço (cm)", null=True, blank=True)
    relaxed_arm = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Braço Relaxado (cm)", null=True, blank=True)
    bust = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Busto (cm)", null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Cintura (cm)", null=True, blank=True)
    abdomen = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Abdômen (cm)", null=True, blank=True)
    hips = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Quadril (cm)", null=True, blank=True)
    proximal_thigh = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Coxa Proximal (cm)", null=True, blank=True)
    calf = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Panturrilha (cm)", null=True, blank=True)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Percentual de Gordura (%)", null=True, blank=True)
    muscle_mass = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Massa Muscular (kg)", null=True, blank=True)
    body_water_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Água Corporal (%)", null=True, blank=True)
    visceral_fat = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Gordura Visceral (%)", null=True, blank=True)
    bone_mass = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Massa Óssea (kg)", null=True, blank=True)
    non_fat_mass = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Massa Não Adiposa (kg)", null=True, blank=True)
    metabolic_age = models.IntegerField(verbose_name="Idade Metabólica (anos)", null=True, blank=True)
    dc_triceps = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="DC Tríceps (mm)", null=True, blank=True)
    dc_biceps = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="DC Bíceps (mm)", null=True, blank=True)
    dc_subescapular = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="DC Subescapular (mm)", null=True, blank=True)
    dc_crista_iliaca = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="DC Crista Ilíaca (mm)", null=True, blank=True)
    dc_supraespinhal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="DC Supraespinhal (mm)", null=True, blank=True)
    dc_abdominal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="DC Abdominal (mm)", null=True, blank=True)
    dc_coxa_media = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="DC Coxa Média (mm)", null=True, blank=True)
    dc_panturrilha = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="DC Panturrilha (mm)", null=True, blank=True)
    conduct = models.TextField(verbose_name='Evolução', null=True, blank=True)
    goal = models.TextField(verbose_name='Meta', null=True, blank=True)

    class Meta:
        verbose_name = "Avaliação Antropométrica"
        verbose_name_plural = "Avaliações Antropométricas"

    def __str__(self):
        return f"Avaliação em {self.date} - {self.client.name}"