from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Abastecimento(models.Model):
    _name = 'combustivel.abastecimento'
    _description = 'Registro de Abastecimento'

    data = fields.Datetime('Data/Hora', default=fields.Datetime.now, required=True)
    veiculo = fields.Char('Placa/Equipamento', required=True)
    odometro = fields.Float('Horímetro/Odômetro')
    
    tanque_id = fields.Many2one('combustivel.tanque', string='Tanque', required=True)
    litros = fields.Float('Litros Abastecidos', required=True)
    valor_litro = fields.Float('Valor por Litro')
    valor_total = fields.Float('Total Calculado', compute='_compute_total', store=True)
    
    motorista_id = fields.Many2one('res.partner', string='Motorista')
    usuario_id = fields.Many2one('res.users', string='Responsável', default=lambda self: self.env.user)

    @api.depends('litros', 'valor_litro')
    def _compute_total(self):
        for rec in self:
            rec.valor_total = rec.litros * rec.valor_litro

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            tanque = self.env['combustivel.tanque'].browse(vals['tanque_id'])
            if tanque.estoque_atual < vals.get('litros', 0):
                raise ValidationError(f"Estoque insuficiente no {tanque.name}!")
            tanque.sudo().write({'estoque_atual': tanque.estoque_atual - vals['litros']})
        return super().create(vals_list)