# To-Do List App

## English

To-Do List web application built with **Django**, using **MySQL** as the database, **Redis** and **WebSockets** for real-time notifications, and **Docker Compose** for containerized deployment.

---

## Features

- Create, read, update, and delete (CRUD) to-do tasks  
- User registration and authentication
- Real time notifications using WebSockets, Channels and Redis
- Mark tasks as complete or pending  
- Simple and responsive Django Template interface  
- Data stored in a MySQL database    
- Fully containerized with Docker and Docker Compose for easy deployment

---

## Tech Stack

- **Backend:** Django 5.x 
- **Database:** MySQL 8  
- **Real-time communication:** Redis  
- **Containerization:** Docker + Docker Compose  
- **Environment:** `.env` file to configurate the environment 

---

## Setup Instructions
Make sure to have Docker installed in your system.
### 1️. Clone the repository

```bash
git clone https://github.com/AlbertoBarradas/to-do-list.git
```

### 2. In the repository root directory, copy the example environment file and edit the values if needed

For macOS/Linux users:
```bash
cp todo_list/.env.example todo_list/.env
```

For Windows users:
```bash
copy todo_list\.env.example todo_list\.env
```

### 3. Build and start the containers (make sure Docker Engine is running)
```bash
docker compose up --build
```

### 4. Once all the containers are running, access the app

http://localhost:8000/

### To access the MySQL database, execute the following command, and enter the password used in the environment file:
```bash
docker exec -it to-do-list-mysql-1 mysql -u todo_user -p
```


## Español

Aplicación de lista de tareas construida en **Django**, usando **MySQL** como base de datos, **Redis** y **WebSockets** para notificaciones en tiempo real, y **Docker Compose** para despliegue en contenedores.

---

## Características

- Operaciones de creación, lectura, actualización y eliminación de tareas
- Registro y autenticación de usuarios
- Notificaciones en tiempo real usando WebSockets, Channels y Redis
- Marcar tareas como completadas o pendientes
- Interfaz de Django Template interactiva
- Datos almacenados en base de datos MySQL    
- Despliegue facil con Docker y Docker Compose.

---

## Tecnologías usadas

- **Backend:** Django 5.x 
- **Base de datos:** MySQL 8  
- **Comunicación en tiempo real:** Redis y WebSockets 
- **Contenedores:** Docker + Docker Compose  
- **Entorno:** archivo `.env` para configuración de entorno  

---

## Instrucciones de ejecución
Asegurate de tener Docker instalado en tu sistema.

### 1️. Clonar repositorio

```bash
git clone https://github.com/AlbertoBarradas/to-do-list.git
```

### 2. En la raiz del repositorio, copia el archivo del entorno y edita los valores si es necesario.

Para usuarios macOS/Linux:
```bash
cp todo_list/.env.example todo_list/.env
```

Para usuarios Windows:
```bash
copy todo_list\.env.example todo_list\.env
```

### 3. Construye y ejecuta los contenedores (asegurate que Docker Engine se está ejecutando)
```bash
docker compose up --build
```

### 4. Una vez que los contenedores estan corriendo, entra al siguiente link para ver la aplicación

http://localhost:8000/

### Para acceder a la base de datos MySQL, ejecuta el siguiente comando e ingresa la contraseña usada en el archivo de entorno:
```bash
docker exec -it to-do-list-mysql-1 mysql -u todo_user -p
```

## Author
Alberto Barradas