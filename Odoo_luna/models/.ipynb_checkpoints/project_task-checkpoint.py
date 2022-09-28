# -*- coding: utf-8 -*-

from odoo import models, fields, api
class ProjectsTask(models.Model):
    _inherit='project.task'
    
    mision_id=fields.Many2one(comodel_name='nave.mision',
                             string='Mision relacionada',
                             ondelete='set null')
    miembros_de_la_nave=fields.Many2many(string='Miembros de la nave',
                                        related='mision_id.miembros_de_la_nave')