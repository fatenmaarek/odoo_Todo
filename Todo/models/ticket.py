from odoo import fields, models


class Ticket(models.Model):
    _name = 'todo.ticket'
    _description = 'Todo Ticket'

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ])
    file = fields.Binary()
    description = fields.Text()
    assign_to = fields.Char(string="Assigned To")