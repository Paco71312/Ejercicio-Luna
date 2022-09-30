# -*- coding: utf-8 -*-
from odoo import http
class Nave(http.Controller):
    @http.route('/nave/',auth='public',website=True)
    def index(self,**kw):
        return "Hola Mundo"
    
    @http.route('/nave/espaciales/',auth='public',website=True)
    def espaciales(self,**kw):
        espaciales=http.request.env['nave.espacial'].search([])
        return http.request.render('Odoo_luna.espacial_website',{'espaciales':espaciales,})
    
    @http.route('/nave/<model("nave.mision"):mision>',auth='public',website=True)
    def mision(self,mision):
        return http.request.render('Odoo_luna.mision_website',{'mision':mision,})
    
    
    
        