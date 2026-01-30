from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'alumno.alumno'
    _description = 'Alumno'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    email = fields.Char(string="Email", required=True)
    curso_ids = fields.Many2many('curso.curso', 'curso_alumno_rel', 'alumno_id', 'curso_id', string="Cursos")
    
    _sql_constraints = [
        ('email_unico', 'UNIQUE(email)', 'El email debe ser único')
    ]

