from django.db import models

class Turnos(models.Model):
    TIPOS_DE_SERVICIO = (
        ('peluqueria', 'Peluquería'),
        ('cirugia', 'Cirugía'),
        ('atencion_veterinaria', 'Atención Veterinaria'),
    )

    TIPOS_DE_TURNOS = (
        ('baño', 'Baño'),
        ('corte_o_bano', 'Corte o Baño'),
        ('castracion', 'Castración'),
        ('otros', 'Otros'),
        ('vacunacion', 'Vacunación'),
        ('atencion', 'Atención'),
    )
    nombre_de_usuario = models.CharField(max_length=50)
    tipo_de_servicio = models.CharField(max_length=50, choices=TIPOS_DE_SERVICIO)
    tipo_de_turnos = models.CharField(max_length=50, choices=TIPOS_DE_TURNOS)  
    fecha = models.DateField()
    horario_disponible = models.TimeField()

    def __str__(self):
        return f"{self.tipo_servicio} - {self.tipo_turnos} - {self.fecha} - {self.horario_disponible}- {self.nombre_de_usuario}"