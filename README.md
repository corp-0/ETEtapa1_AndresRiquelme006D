# ETEtapa1_AndresRiquelme006D

## Instrucciones
1. ### Obtener el proyecto

      ``git clone https://github.com/corp-0/ETEtapa1_AndresRiquelme006D.git``

2. ### Instalar dependencias

      ``pip install -r requirements.txt``

3. ### Configurar conexión a base de datos
    - Crear un archivo y llamarlo ``.env``.
    - Copiar el contenido de ``ejemplo.env``. Corrija según sus propias credenciales.
4. ### Crear datos de prueba
    - Este comando creará usuarios y publicaciones en masa con datos aleatorios para diferenciarlos.
    - Tendrá acceso a un super usuario de nombre: ``admin`` y contraseña ``admin``.
    
      ``python manage.py datosdeprueba``

5. ### Correr el servidor

      ``python manage.py migrate``

      ``python manage.py runserver``

6. ### Acceder al CRUD
    - Para acceder al CRUD necesitará haber iniciado sesión con un usuario de nivel **ADMINISTRADOR**.
    - Utilice las credenciales del punto 4 ingresando mediante ``http://localhost:8000/admin``
    - Apartir de entonces, podrá ingresar usando ``http://localhost:8000/crud`` o mediante el enlace en la barra de navegación.
   
### Live demo
Es posible navegar y ver el sitio web en [este enlace](http://gilles.brazilsouth.cloudapp.azure.com:5050)
