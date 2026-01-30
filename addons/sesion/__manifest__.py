{
    'name': "Sesión",

    'summary': "Módulo para gestionar sesiones de los cursos",

    'description': """
Módulo para la gestión de sesiones con información de fecha, duración y número de asientos.
Relación con cursos y clases.
    """,

    'author': "Academia EduOdoo",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '0.1',

    'depends': ['base', 'curso'],

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

