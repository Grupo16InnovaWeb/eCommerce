# eCommerce
Proyecto E-Commerce InnovaWeb. Evidencia de Aprendizaje N° 3

# Gestión de Usuarios para E-commerce

Este proyecto proporciona un sistema de gestión de usuarios para plataformas de e-commerce, con control de acceso basado en roles (administrador y usuario estándar), validaciones de seguridad y una base de datos MySQL.

## Características principales

- **Autenticación segura**: Hash SHA-256 para contraseñas
- **Control de acceso**: Roles de administrador y usuario estándar
- **Base de datos MySQL**: Estructura modular para fácil integración
- **Validaciones**: Contraseñas con requisitos mínimos de seguridad
- **Entorno configurable**: Mediante variables de entorno

## Requisitos previos

- Python 3.x
- MySQL Server
- pip (Gestor de paquetes de Python)

## Instalación

1. **Configuración de la base de datos**:
   - Instalar MySQL
   - Ejecutar el script `db_creation.sql` para crear la base de datos

2. **Configurar variables de entorno**:
   Crear un archivo `.env` con el siguiente contenido:
   ```
   DB_HOST=localhost
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
   DB_NAME=ecommerce_db
   ```

3. **Instalar dependencias**:
   ```bash
   pip install mysql-connector-python python-dotenv
   ```

## Ejecución

```bash
python src/main.py
```

## Pruebas iniciales

1. Registrar un usuario administrador:
   - Email: `admin@ecommerce.com`
   - Contraseña: `admin123`

2. Iniciar sesión como administrador y probar las funciones de gestión

3. Registrar un usuario estándar y verificar las restricciones de acceso

## Estructura del proyecto

```
ecommerce-users/
│
├── src/                 # Código fuente principal
├── db_creation.sql      # Script de creación de la base de datos
├── .env.example         # Ejemplo de configuración de entorno
└── requirements.txt     # Dependencias del proyecto
```

## Consideraciones de seguridad

- Las contraseñas se almacenan con hash SHA-256
- Validación de contraseñas con requisitos mínimos
- Control de acceso basado en roles

## Mejoras futuras

- [ ] Implementar recuperación de contraseña
- [ ] Añadir logging de actividades
- [ ] Desarrollar interfaz gráfica
- [ ] Agregar más validaciones en formularios

## Integrantes del proyecto

