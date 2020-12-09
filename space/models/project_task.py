# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    mission_id = fields.Many2one(comodel_name='space.mission',
                                 string='Related Mission',
                                 ondelete='set null')
    
    member_ids = fields.Many2many(string='Members',
                                  related='mission_id.member_ids')