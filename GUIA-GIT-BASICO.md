# Guía mínima de Git para este proyecto

Solo necesitas estos comandos. No hace falta aprender más que esto por ahora.

## 1. Instalar Git (una sola vez)
Descarga desde https://git-scm.com/download/win e instala con las opciones por defecto.

## 2. Configurar tu identidad (una sola vez)
Abre "Git Bash" (se instala junto con Git) y escribe:

```
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

## 3. Crear el repositorio en GitHub
1. Entra a https://github.com y crea una cuenta si no tienes.
2. Click en "New repository" (botón verde).
3. Nombre: `softcorp-devsecops`
4. Déjalo público o privado (para la demo, público es más simple, ya que GitHub Actions es gratis en repos públicos).
5. NO marques "Add README" (ya tienes tus archivos).
6. Click "Create repository". GitHub te va a mostrar unos comandos — los usamos abajo.

## 4. Subir tus archivos por primera vez
Desde la carpeta `softcorp-devsecops` (donde están tus archivos), en Git Bash:

```bash
cd ruta/a/tu/carpeta/softcorp-devsecops
git init
git add .
git commit -m "Estructura inicial del proyecto SoftCorp DevSecOps"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/softcorp-devsecops.git
git push -u origin main
```

Te va a pedir iniciar sesión la primera vez (se abre el navegador).

## 5. Flujo normal de trabajo (los únicos 4 comandos que vas a repetir)

Cada vez que cambies algo y quieras subirlo:

```bash
git add .                          # Prepara los cambios
git commit -m "Descripción breve"  # Guarda los cambios localmente con un mensaje
git push                           # Sube los cambios a GitHub
```

Si quieres traer cambios que hiciste desde otra máquina:

```bash
git pull
```

## 6. Para la DEMO EN VIVO (jueves)

Esto es lo importante: vas a hacer un commit que **debería fallar** el pipeline, para demostrar que funciona:

```bash
# Ejemplo: agregar un secreto a propósito para que Gitleaks lo bloquee
echo 'API_KEY = "AKIAFAKEEXAMPLEKEY123456"' >> app/demo_falla.py
git add .
git commit -m "demo: intento de subir un secreto"
git push
```

Luego vas a GitHub → pestaña "Actions" → mostrar en vivo cómo el pipeline se pone en rojo (falla) en la etapa de Secret Scanning.

Después, para mostrar el caso exitoso, borras esa línea y vuelves a hacer push — el pipeline se pone en verde.

## 7. Ver el estado de tu repositorio en cualquier momento

```bash
git status
```

Te dice qué archivos cambiaste y si tienes algo pendiente de subir.
