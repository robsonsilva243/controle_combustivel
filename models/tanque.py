from odoo import models, fields

class CombustivelTanque(models.Model):
    _name = 'combustivel.tanque'
    _description = 'Tanque de Combustível'

    name = fields.Char('Nome do Tanque', required=True)
    capacidade = fields.Float('Capacidade (L)', default=6000.0)
    estoque_atual = fields.Float('Estoque Atual (L)')