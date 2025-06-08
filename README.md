# eCommerce
Proyecto E-Commerce InnovaWeb. Evidencia de Aprendizaje N° 3

# Gestión de Usuarios para E-commerce

Este proyecto es un sistema de consola para la gestión de usuarios en un E-commerce de tecnología, donde los usuarios pueden registrarse, iniciar sesión y acceder a funcionalidades específicas según su rol (administrador o usuario estándar). Además, se diseñó una base de datos relacional en MySQL para estructurar los datos del sistema, aunque el código funciona sin persistencia.

## Características principales

- Registrar e iniciar sesión de usuarios con validaciones seguras.
- Control de acceso mediante roles.
- Menús personalizados según el tipo de usuario.
- Diseño de una base de datos en tercera forma normal (3FN).
- Aplicación de principios de Programación Orientada a Objetos (POO).

##  Tecnologías utilizadas

- **Lenguaje:** Python 3.x

- **Editor:** Visual Studio Code

- **Base de Datos:** MySQL (para modelado, sin conexión directa)

- **Modelo relacional:** Normalizado a 3FN

## Instrucciones para ejecutar

1. Cloná o descargá el repositorio.

2. Abrí la carpeta del proyecto desde VS Code.

3. Asegurate de tener instaladas las extensiones de Python.

4. Ejecutá el archivo `main.py`.

##  Archivos SQL incluidos

- `crear_bd.sql` → Script para crear las tablas y relaciones.

- `crud_usuarios.sql` → Insert, Select, Update y Delete para la tabla `usuarios`.

NOTA: Dichos archivos estan nombrados en formato txt
---

##  Conceptos aplicados

- Programación Orientada a Objetos (POO)

- Encapsulamiento de datos

- Modularidad y separación de responsabilidades

- Nomenclatura estándar (snake_case)

- Validación con expresiones regulares

- Modelado entidad-relación

- Integridad referencial en bases de datos


##  Validaciones implementadas

- Contraseña: mínimo 6 caracteres, debe incluir letras y números (usando expresiones regulares).

- Validación de usuario duplicado.

- Control de errores con mensajes claros.

- Acceso restringido por rol (`usuario` o `admin`).

---

##  Funcionalidades por rol

| Acción | Usuario estándar | Administrador |

|-----|----|----|

| Ver sus datos                | ✅   | ✅ |

| Ver todos los usuarios       | ❌   | ✅ |

| Cambiar rol de otro usuario  | ❌   | ✅ |

| Eliminar un usuario          | ❌   | ✅ |

---

## Estructura del proyecto

```
innovaweb_ecommerce/
│
├── src/                  # Código fuente principal
│    ├── main.py          # Punto de entrada del programa  
│    ├── menu.py          # Menú por rol
│    ├── auth.py          # Funciones de registro y login
│    └── user.py          # Clase Usuario
│
├── database/             # Base de datos
│    ├── Creacion de tablas.txt  # Script de la base de datos
│    └── CRUD para Usuarios.txt  # Consultas Clase Usuario
│
├── docs/          # Diagramas
│    ├── Diagrama de Clases.png  
|    └── Diagrama de Base de datos.png
│
└── Readme.md       
```

## Diagramas del proyecto
![alt text](/images/)

## Integrantes del proyecto

| Nombre | Rol en el Proyecto |
|------|-----|
| Acosta Johana Vanessa | Base de datos |
| Andreoli Fernando Daniel | Base de datos |
| Crespin Marianela Jenifer | Python |
| Molina Ricardo Alberto | Python |
| Vaca Cristian Andres | Python |
