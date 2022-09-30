{
    'name':'Odoo Luna',
    'summary':"""Esta es uan app que ayudar a Odoo a llegar a la luna""",
    'description':""" App para la Luna de Odoo
    -Nave Espacial
    -Tripulacion
    """,
    'license':'LGPL-3',
    'author':'Paco',
    'version':'0.1',
    'category': 'Training',
    'depends': ['project','website'],
    'data':['security/nave_security.xml','security/ir.model.access.csv','views/nave_menuitems.xml','views/nave_views.xml','views/mision_views.xml','views/projects_views_inherit.xml','reports/mision_report_template.xml','views/luna_web_template.xml',
        
    ],
    'demo':['demo/nave_demo.xml',
        
    ],
    
}