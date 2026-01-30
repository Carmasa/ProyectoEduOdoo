{
    'name': "Facturación",

    'summary': "Módulo para gestionar facturas de alumnos",

    'description': """
Módulo para la gestión de facturas con información de cantidad, fecha de pago y concepto.
Relación con alumnos.
    """,

    'author': "Academia EduOdoo",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '0.1',

    'depends': ['base', 'alumno'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

