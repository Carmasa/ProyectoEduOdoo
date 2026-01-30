from odoo import models, fields, api


class Sesion(models.Model):
    _name = 'sesion.sesion'
    _description = 'Sesión'

    titulo = fields.Char(string="Título", required=True)
    fecha_inicio = fields.Datetime(string="Fecha de Inicio", required=True)
    duracion = fields.Integer(string="Duración (minutos)", required=True)
    numero_asientos = fields.Integer(string="Número de Asientos", required=True)
    curso_id = fields.Many2one('curso.curso', string="Curso", required=True)

