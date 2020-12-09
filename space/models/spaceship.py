# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    _name = 'space.spaceship'
    _description = 'Spaceship Info'
    
    name = fields.Char(string='Title', required=True)
    type = fields.Text(string='Ship type')
    fuel = fields.Selection(string= 'Fuel type', 
                            selection=[('a', 'Type A'),
                                     ('b', 'Type B'),
                                     ('c', 'Type C')],
                            copy=False)
    
    passenger = fields.Text(string='Number of passengers')
    
    active = fields.Boolean(string='Active', default=True)
    
    mission_ids = fields.One2many(comodel_name='space.mission',
                                  inverse_name='spaceship_id',
                                  string='Missions')
    
    def open_wizard(self):
        action = self.env.ref('space.space_mission_wizard_action').read()[0]
        action['context'] = {'default_spaceship_ids': self.ids}
        return action
