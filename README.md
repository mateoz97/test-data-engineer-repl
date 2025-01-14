# Ejercicio práctico para Data Engineer Replication/Extraction en Deacero.

La estructura de carpetas del repositorio simula 3 servidores de Microsoft SQL Server uno con datos centrales y otros con datos por sucursal:

```
data
├── central
│   ├── CatLineasAereas.csv
├── sucursal1
│   ├── Pasajeros.csv
│   ├── Vuelos.csv
├── sucursal2
│   ├── Pasajeros.csv
│   ├── Vuelos.csv
```
## Objetivo

El requerimiento funcional consiste en centralizar y replicar la información en el datawareohuse de Bigquery.

Para esto debe realizar las implementaciones técnicas que considere necesarias para la replicación de datos con CDC y SQL Replicate hacia Bigquery.

## Información clave

- Deben respetarse las tecnologías de CDC y SQL Replicate.
- Es importante generar un diagrama de arquitectura sobre la implementación.
- La actualización de datos debe buscar la menor latencia posible segun la tecnología que se implemente o proponga.
- Debe buscarse una implementación lo mas cercana al codigo posible.
- Tienes alguna propuesta o hallazgos respecto a garantizar la calidad/integridad de la replicacón?

## Entrega del Ejercicio

- Debe realizar un fork de este repositorio para desarrollar y entregar su trabajo o tambien puede subir su proyecto a un repositorio de GitHub y compartir el enlace en un correo dirigido a jguerrero@deacero.com.
- Asegúrese de que el repositorio incluya:
    - Todos los recursos usados o generados para la solucion de los ejercicios.
    - Documentación que explique el proceso seguido y las decisiones tomadas.
    - Instrucciones claras sobre cómo configurar y ejecutar el proyecto y sus artefactos.

Suerte a todos!!! :metal: :nerd_face: :computer:

# Guía de Instalación y Configuración de Google Cloud CLI y SDK

Esta guía te llevará a través del proceso de instalación y configuración de Google Cloud CLI y SDK, así como la gestión de dependencias utilizando Poetry.

## Requisitos Previos

- Tener una cuenta de Google Cloud.
- Acceso a la terminal o línea de comandos.

## 1. Instalación de Google Cloud CLI

### 1.1. Instalación en Windows

1. **Descargar el instalador**:
   - Ve a la [página de descarga de Google Cloud CLI](https://cloud.google.com/sdk/docs/install).

2. **Ejecutar el instalador**:
   - Haz doble clic en el archivo descargado y sigue las instrucciones en pantalla.

### 1.2. Instalación en macOS

1. **Usar Homebrew**:
   - Abre la terminal y ejecuta:

     ```bash
     brew install --cask google-cloud-sdk
     ```

2. **Inicializar Google Cloud SDK**:
   - Después de la instalación, ejecuta:

     ```bash
     gcloud init
     ```

### 1.3. Instalación en Linux

1. **Descargar el script de instalación**:
   - En la terminal, ejecuta:

     ```bash
     curl https://sdk.cloud.google.com | bash
     ```

2. **Reiniciar la terminal**:
   - Cierra y vuelve a abrir la terminal.

3. **Inicializar Google Cloud SDK**:
   - Ejecuta:

     ```bash
     gcloud init
     ```

## 2. Configuración de Google Cloud CLI

1. **Autenticación**:
   - Ejecuta el siguiente comando para autenticarte:

     ```bash
     gcloud auth login
     ```

   - Esto abrirá una ventana del navegador donde podrás iniciar sesión con tu cuenta de Google.

2. **Seleccionar el proyecto**:
   - Puedes listar tus proyectos disponibles con:

     ```bash
     gcloud projects list
     ```

   - Para seleccionar un proyecto específico, usa:

     ```bash
     gcloud config set project PROJECT_ID
     ```

   - Reemplaza `PROJECT_ID` con el ID de tu proyecto.

## 3. Gestión de Dependencias con Poetry
### 3.1. Instalación de Poetry
Instalar Poetry:

Ejecuta el siguiente comando en tu terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Agregar Poetry al PATH:

Asegúrate de que el directorio de instalación de Poetry esté en tu variable de entorno PATH. Generalmente, se encuentra en ~/.local/bin.
### 3.2. Crear un nuevo proyecto con Poetry
Crear un nuevo proyecto:

En la terminal, navega al directorio donde deseas crear tu proyecto y ejecuta:

```bash
poetry new nombre_del_proyecto
```

Entrar al directorio del proyecto:

Cambia al directorio del proyecto:

```bash
cd nombre_del_proyecto
```

### 3.3. Agregar dependencias
Agregar una dependencia:

Para agregar una nueva dependencia, usa:

```bash
poetry add nombre_de_la_dependencia
```

Agregar una dependencia de desarrollo:

Para agregar una dependencia que solo se necesita en desarrollo, usa:

```bash
poetry add --dev nombre_de_la_dependencia
```
### 3.4. Instalar dependencias
Para instalar todas las dependencias definidas en el archivo pyproject.toml, simplemente ejecuta:

```bash
poetry install
```
