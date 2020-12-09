# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Mission(models.Model):
    _name = 'space.mission'
    _description = 'Space mission info'
    
    spaceship_id = fields.Many2one(comodel_name='space.spaceship',
                                   string='Spaceship',
                                   ondelete='cascade',
                                   required=True)
    name = fields.Char(string='Title')
    ship = fields.Char(string='Ship', related='spaceship_id.name') 

    type = fields.Text(string='Ship type', related='spaceship_id.type') 
#    passenger = fields.Text(string='Number of passengers', related='spaceship_id.passenger')
    member_ids = fields.Many2many(comodel_name='res.partner', string='Members')
    team_member_id = fields.Many2one(comodel_name='res.users', string='Team member')
    launch_date = fields.Date(string='Launch Date',
                              default=fields.Date.today)
    
    return_date = fields.Date(string='Return Date',
                              compute='_compute_return_date',
                              inverse='_inverse_end_date',
                              store=True)
    
    duration = fields.Integer(string='Mission Days',
                              dafault=1)
    captain = fields.Many2one('res.users', string="Captain")
    
#    fuel_needed = fields.Integer(string='Amount of fuel needed', store=True)
#    fuel_count = fields.Integer(
#        string="Amount of fuel needed", compute='_get_fuel_count', store=True)
    fuel_needed = fields.Integer(
        string="Amount of fuel needed", store=True)
    
    engine = fields.Integer(string='Number of engines', store=True)
    safety = fields.Integer(string='Safety features', store=True)
    
    @api.depends('launch_date', 'duration')
    def _compute_return_date(self):
        for record in self:
            if not (record.launch_date and record.duration):
                record.return_date = record.launch_date
            else:
                duration = timedelta(days=record.duration)
                record.return_date = record.launch_date + duration
    
    def _inverse_end_date(self):
        for record in self:
            if record.launch_date and record.return_date:
                record.duration = (record.return_date - record.launch_date).days + 1
            else:
                continue

