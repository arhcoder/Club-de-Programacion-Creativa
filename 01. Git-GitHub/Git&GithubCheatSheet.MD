# Git y GitHub: Guía Rápida (Cheat Sheet)

Esta es una guía de referencia rápida con los comandos más comunes de Git y GitHub. Git es un sistema de control de versiones que te ayuda a rastrear los cambios en tu código, mientras que GitHub es una plataforma para alojar tus repositorios de Git y colaborar con otros.

## 1. Configuración Inicial (Solo se hace una vez)

Antes de empezar, es importante configurar tu identidad en Git y establecer la rama por defecto para los nuevos repositorios.

#### Cambiar el nombre de la rama por defecto a `main`

Por convenciones modernas y para promover un lenguaje más inclusivo, la comunidad de desarrollo ha migrado de `master` a `main` como el nombre de la rama principal.

```bash
git config --global init.defaultBranch main
```

#### Configurar tu identidad

Git necesita saber quién eres para registrar quién hace cada cambio. Esta información se guardará en cada *commit* que realices.

*   **Configurar tu correo electrónico:**
    ```bash
    git config --global user.email "tu-email@ejemplo.com"
    ```

*   **Configurar tu nombre de usuario:**
    ```bash
    git config --global user.name "Tu Nombre de Usuario"
    ```

*   **Verificar la configuración:**
    Puedes revisar que la configuración se haya guardado correctamente.
    ```bash
    git config --list
    ```

## 2. Comandos Básicos de la Terminal

Estos comandos no son de Git, pero son esenciales para moverte por tu sistema de archivos.

*   **Limpiar la pantalla de la terminal:**
    *   En macOS y Linux: `clear`
    *   En Windows: `cls`

*   **Ver el directorio actual (Print Working Directory):**
    Te muestra la ruta completa de la carpeta en la que te encuentras.
    ```bash
    pwd
    ```

*   **Listar archivos y directorios:**
    El comando `ls -al` muestra todos los archivos (incluyendo los ocultos como `.git`) en un formato de lista detallado.
    ```bash
    ls -al
    ```

*   **Cambiar de directorio (Change Directory):**
    ```bash
    # Entrar a un directorio
    cd nombre-del-directorio

    # Retroceder un nivel
    cd ..

    # Ir a tu directorio "home"
    cd ~
    ```

## 3. Flujo de Trabajo Básico en Git

Este es el ciclo que seguirás constantemente al trabajar en un proyecto.

#### Crear un Repositorio

*   **Inicializar un repositorio en una carpeta existente:**
    Este comando crea una subcarpeta oculta `.git` donde Git almacenará toda la historia y configuración del proyecto.
    ```bash
    git init
    ```

*   **Clonar un repositorio existente desde una URL:**
    Crea una copia local de un proyecto que ya existe en una plataforma como GitHub.
    ```bash
    git clone <url-del-repositorio>
    ```

#### El Ciclo Básico: Modificar, Agregar y Confirmar

1.  **Revisar el estado del repositorio:**
    Te muestra qué archivos han sido modificados, cuáles están en el *staging area* y cuáles no están siendo rastreados por Git. Es el comando más útil para saber dónde estás parado.
    ```bash
    git status
    ```

2.  **Agregar cambios al Staging Area:**
    El *staging area* (o índice) es una zona intermedia donde preparas los cambios que quieres incluir en tu próximo *commit*.
    ```bash
    # Agregar un archivo específico
    git add <nombre-del-archivo>

    # Agregar todos los cambios del directorio actual
    git add .
    ```

3.  **Confirmar los cambios (Commit):**
    Un *commit* es como una "fotografía" o un punto de guardado en la historia de tu proyecto. Cada commit tiene un mensaje que describe los cambios realizados.
    ```bash
    git commit -m "Un mensaje descriptivo de los cambios hechos"
    ```

4.  **Ver el historial de commits:**
    Muestra la lista de todos los commits realizados en la rama actual.
    ```bash
    # Muestra el historial completo
    git log

    # Una versión más limpia y visual
    git log --oneline --graph --decorate
    ```

## 4. Manejo de Ramas (Branches)

Las ramas te permiten trabajar en nuevas funcionalidades o arreglos de forma aislada sin afectar la rama principal (`main`).

*   **Listar todas las ramas:**
    La rama con un `*` es en la que te encuentras actualmente.
    ```bash
    git branch
    ```

*   **Crear una nueva rama:**
    ```bash
    git branch <nombre-de-la-nueva-rama>
    ```

*   **Cambiar de una rama a otra:**
    ```bash
    git checkout <nombre-de-la-rama>
    ```
    *   **Alternativa moderna:** El comando `switch` es más intuitivo para cambiar de rama.
        ```bash
        git switch <nombre-de-la-rama>
        ```

*   **Crear una nueva rama y cambiar a ella en un solo paso:**
    ```bash
    git checkout -b <nombre-de-la-nueva-rama>
    ```

*   **Unir ramas (Merge):**
    Integra los cambios de una rama en otra.
    **Nota:** Para hacer un merge, primero debes situarte en la rama que va a *recibir* los cambios (ej. `main`) y luego ejecutar el merge con la rama que *contiene* los cambios (ej. `mi-feature`).
    ```bash
    # 1. Cambia a la rama principal
    git checkout main

    # 2. Une los cambios de la otra rama en main
    git merge <nombre-de-la-rama-a-unir>
    ```

## 5. Trabajo con Repositorios Remotos (GitHub)

Un repositorio remoto es una versión de tu proyecto alojada en internet o en una red (comúnmente en GitHub).

*   **Agregar un repositorio remoto:**
    Conectas tu repositorio local con uno remoto. Por convención, al repositorio principal se le llama `origin`.
    ```bash
    git remote add origin <url-del-repositorio-en-github>
    ```

*   **Verificar los remotos configurados:**
    ```bash
    git remote -v
    ```

*   **Subir cambios al repositorio remoto (Push):**
    Envía tus commits locales al repositorio remoto.
    ```bash
    git push origin <nombre-de-la-rama>
    ```
    *   **Primer push:** La primera vez que subes una rama, usa la bandera `-u` para enlazar tu rama local con la remota.
        ```bash
        git push -u origin main
        ```

*   **Descargar cambios del repositorio remoto (Pull):**
    Trae los cambios más recientes del repositorio remoto y los fusiona con tu rama local. Es una combinación de `git fetch` y `git merge`.
    ```bash
    git pull origin <nombre-de-la-rama>
    ```

#### Sincronizar un Fork

Si has hecho un *fork* (una copia personal) de otro repositorio y quieres actualizarlo con los cambios del original:

1.  **Agrega el repositorio original como un remoto llamado `upstream`:**
    ```bash
    git remote add upstream <url-del-repositorio-original>
    ```

2.  **Obtén los cambios del `upstream` (Fetch):**
    `fetch` descarga los datos del remoto pero no los integra automáticamente.
    ```bash
    git fetch upstream
    ```

3.  **Fusiona los cambios:**
    Asegúrate de estar en tu rama `main` y luego fusiona los cambios desde la rama `main` del `upstream`.
    ```bash
    git checkout main
    git merge upstream/main
    ```

## 6. Resolución de Conflictos

Un conflicto ocurre cuando Git no puede fusionar automáticamente los cambios de dos ramas porque hay ediciones incompatibles en el mismo archivo.

1.  Git pausará el `merge` y te informará qué archivos tienen conflictos.
2.  Abre los archivos conflictivos en tu editor de código. Verás marcadores especiales:
    ```
    <<<<<<< HEAD
    // Tu código actual en esta rama
    =======
    // El código que viene de la otra rama
    >>>>>>> nombre-de-la-otra-rama
    ```
3.  **Edita el archivo manualmente**: decide qué código quieres conservar, elimina los marcadores (`<<<<<<<`, `=======`, `>>>>>>>`) y guarda el archivo.
4.  Una vez resueltos todos los conflictos, agrega los archivos modificados al *staging area*.
    ```bash
    git add <archivo-resuelto-1> <archivo-resuelto-2>
    ```
5.  Finaliza el proceso con un `commit`. Si estabas en medio de un `merge`, Git puede sugerir un mensaje de commit por defecto.
    ```bash
    git commit
    ```
    *   Si el `merge` se detuvo, también puedes usar:
        ```bash
        git merge --continue
        ```