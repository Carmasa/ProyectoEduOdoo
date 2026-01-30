# EduOdoo - Sistema de Gestión Académica

Sistema de gestión académica basado en **Odoo 19.0** para administrar cursos de idiomas con 6 módulos integrados.

## 📊 Módulos

| Módulo | Descripción |
|--------|-------------|
| **profesor** | Gestiona docentes (nombre, apellidos, titulación, email) |
| **curso** | Gestiona cursos (título, descripción, nivel MCER, precio) |
| **sesion** | Gestiona sesiones de cursos (fecha, duración, asientos) |
| **alumno** | Gestiona estudiantes (nombre, apellidos, email) |
| **clases** | Gestiona detalles de clases (nombre, horario, grupo) |
| **facturacion** | Gestiona facturas (número, cantidad, estado, concepto) |

## 🚀 Instalación

```bash
# 1. Activar entorno Python 3.11
cd odoo
.\venv\Scripts\activate

# 2. Configurar PostgreSQL

# 3. Instalar módulos
.\venv\Scripts\python.exe odoo-bin -r user -w pass --addons-path=addons -d TrabajoFinalOdooDB -u base -i profesor,curso,alumno,sesion,clases,facturacion --stop-after-init

# 4. Ejecutar servidor
.\venv\Scripts\python.exe odoo-bin -r user -w pass --addons-path=addons -d TrabajoFinalOdooDB
```

Acceder: **http://localhost:8069** (admin / admin)

## ✅ Restricciones Resueltas

| # | Restricción | Solución |
|---|------------|----------|
| 1 | Dependencias circulares | Reorganización jerárquica sin ciclos |
| 2 | Python 3.13 incompatible con reportlab | Instalación de Python 3.11 |
| 3 | Archivo LICENSE faltante | Creación con licencia LGPL-3.0 |
| 4 | Clave `license` faltante en manifests | Adición de `'license': 'LGPL-3'` en todos los módulos |

## 📁 Dependencias
```

## 🔍 Verificación

**Desde Odoo:** Settings > Technical > Models → Verificar 6 modelos

**Desde PostgreSQL:**
```bash
psql -U user -d pass
\dt profesor_* curso_* sesion_* alumno_* clases_* facturacion_*
```

## 📱 Próximas Fases

- Fase 2: Vistas (formularios y tablas)
- Fase 3: Reportes PDF
- Fase 4: Automatizaciones

---
