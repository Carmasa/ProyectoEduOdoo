from odoo import models, fields, api


class Facturacion(models.Model):
    _name = 'facturacion.facturacion'
    _description = 'Facturación'

    numero_factura = fields.Char(string="Número de Factura", required=True, unique=True)
    alumno_id = fields.Many2one('alumno.alumno', string="Alumno", required=True)
    cantidad = fields.Float(string="Cantidad", required=True)
    fecha_pago = fields.Date(string="Fecha de Pago")
    concepto = fields.Text(string="Concepto", required=True)
    estado = fields.Selection([
        ('draft', 'Borrador'),
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('anulada', 'Anulada')
    ], string="Estado", default='draft')

