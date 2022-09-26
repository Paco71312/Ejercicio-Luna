# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mision(models.Model):
    _name='nave.mision'
    _description='Es la misison que trae la nave'
    
    nave_id= fields.Many2one(comodel_name='nave.espacial',
                                    string='Nave Asignada',
                                    ondelete='cascade',
                                    required=True)
    
    name=fields.Char(string='Title',related='nave_id.name')
    
    miembros_de_la_nave=fields.Many2many(comodel_name='res.partner',
                                 string='Miembros de la nave')
    fecha_de_lazamiento=fields.Date(string='Fecha de Lanzamiento')
    fecha_de_regreso=fields.Date(string='Fecha de Regreso a la Tierra')
    