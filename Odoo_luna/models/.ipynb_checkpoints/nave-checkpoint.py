from odoo import models, fields, api

class Nave(models.Model):
    _name='nave.espacial'
    _description='Es una nave espacial'
    _rec_name:'spacial car'
        
    name=fields.Char(string='Nombre de la nave',required='True')
    dimensiones_de_la_nave=fields.Char(string='Dimensiones de la Nave')
    tipo_de_combustible=fields.Selection(string='Tipo de combustible',selection= [('gasolina','Gasolina'),('turbosina','Turbosina')], required='True',copy='False')
    tipo_de_nave=fields.Selection(string='Tipo de nave', selection=[('transbordador','Transbordador'),('Nave Espacial', 'Nave Espacial ')], copy='False',required='True')
    numero_de_pasajeros=fields.Integer(string='Numero de pasajeros',required='True')
    estatus_de_la_nave=fields.Selection(string='estatus de la nave', selection= [('Activa','activo'),('Retirado','retirado')],copy='False')
    active=fields.Boolean(string='Ative',default=True)