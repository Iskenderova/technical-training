# -*- coding: utf-8 -*-

{
    
    'name': 'Space Mission',
    
    'summary': """Space Mission""",
    
    'description': """
        Get to the moon:
        -Rocket
    
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Mission',
    'version': '0.1',
    
    'depends': ['project'],
    
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        
        'datas/ship_demo.xml',
        'datas/server_actions.xml',
        
        'views/ship_menuitems.xml',
        'views/spaceship_views.xml',        
        'views/mission_views.xml',
        'views/project_views_inherit.xml',
        
        'wizards/space_mission_wizard.xml'
        'wizards/space_project_wizard.xml'
    ],
    
    'demo': [
        
    ],    
}