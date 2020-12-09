# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SpaceMissionWizard(models.TransientModel):
    _name = 'space.mission.wizard'
    _description = 'space mission wizard'
    
    spaceship_ids = fields.Many2many('space.spaceship', string="Spaceships", required=True)
    
    mission_name = fields.Char(string="Mission name")
    
    
    def create_mission(self):
        for ship in self.spaceship_ids:
        
            self.env['space.mission'].create({
                'spaceship_id': ship.id,
                'name': self.mission_name
            })
