{
    'name': "Alumno",

    'summary': "Módulo para gestionar alumnos de los cursos",

    'description': """
Módulo para la gestión de alumnos con información de nombre, apellidos y email.
Relaciones con cursos y facturas.
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

