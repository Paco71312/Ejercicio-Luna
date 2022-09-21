from odoo import models, fields, api

class Nave(models.Model):
    _name='nave.espacial'
    _description='Es una nave espacial'
    _rec_name:'spacial car'
        
        name=fields.Char(string='Nombre de la nave',required='True')
        #dimensiones=fields.Char(string='Dimensiones de la Nave')
        #tipo_de_combustible=fileds.Selection(string='Tipo de combustible',selection= [('gasolina','Gasolina'),('turbosina','Turbosina')], required='True',copy='False')