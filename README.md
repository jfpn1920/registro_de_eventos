## 👋 ¡Bienvenidos usuarios a mi proyecto! registro de eventos

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en desarrollar un sistema en Python que permite registrar y consultar eventos utilizando diccionarios. Cada evento se almacena con su fecha como clave y su descripción como valor, facilitando la organización y el acceso a la información de manera rápida y eficiente.

El sistema permite al usuario agregar nuevos eventos y consultar todos los eventos registrados mediante un menú interactivo en consola. Además, incluye validaciones para evitar la duplicación de fechas, asegurando que cada evento tenga una fecha única. Esta estructura proporciona un control organizado de los eventos y mejora la experiencia del usuario al interactuar con la información de manera intuitiva y confiable.

Adicionalmente, el programa permite mantener un historial de eventos que puede ser consultado en cualquier momento, lo que facilita la planificación y seguimientos.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar diccionarios para almacenar eventos con fecha y descripción.  
- Aplicar funciones para agregar y mostrar eventos de forma modular.  
- Utilizar bucles `for` para recorrer los registros y mostrarlos ordenadamente.  
- Validar la existencia de fechas duplicadas para mantener la integridad de los datos.  
- Crear un menú interactivo que permita al usuario gestionar los eventos fácilmente.

#
### 🧠 Temas que se a aplicado
- Diccionarios  
- Funciones  
- Bucles `for`  
- Condicionales (`if`, `else`)  
- Validación de duplicados  
- Menú interactivo con bucle `while`

#
### ⚙️ Funcionamiento
1. Se crea un diccionario llamado `eventos` donde:
   - La clave representa la fecha del evento.  
   - El valor representa la descripción del evento.

2. El menú principal permite:  
   - Agregar un nuevo evento validando que la fecha no esté registrada previamente.  
   - Consultar todos los eventos registrados, mostrando la fecha y la descripción de cada uno.  
   - Salir del sistema.

3. Cada operación se ejecuta mediante funciones independientes para mantener el código organizado y modular.

4. El sistema se mantiene activo mediante un bucle `while` hasta que el usuario decide salir, permitiendo registrar y consultar múltiples eventos de manera continua.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```