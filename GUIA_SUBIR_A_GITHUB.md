# Cómo guardar `casa_plano.txt` en tu repositorio de GitHub

Actualmente el archivo ya está versionado en git dentro de este proyecto.

## 1) Crear un repositorio en GitHub
1. Entra a https://github.com/new
2. Crea un repositorio (por ejemplo: `casa-plano`).
3. Copia la URL del repositorio (HTTPS o SSH).

## 2) Conectar este proyecto con tu repo de GitHub
Reemplaza `TU_USUARIO` y `TU_REPO` por tus datos:

```bash
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
```

Si ya existe `origin`, actualízalo con:

```bash
git remote set-url origin https://github.com/TU_USUARIO/TU_REPO.git
```

## 3) Subir el branch actual
```bash
git push -u origin work
```

## 4) Verificar en GitHub
- Abre tu repositorio en GitHub.
- Debes ver el archivo `casa_plano.txt` en la rama `work`.

## 5) Abrir esta información en PowerShell
Desde PowerShell, entra a la carpeta del proyecto y abre los archivos:

```powershell
cd C:\ruta\a\casa.txt
Get-Content .\casa_plano.txt
Get-Content .\GUIA_SUBIR_A_GITHUB.md
```

Si quieres abrirlos en Bloc de notas:

```powershell
notepad .\casa_plano.txt
notepad .\GUIA_SUBIR_A_GITHUB.md
```

## Opcional: usar `main` como rama principal
Si prefieres usar `main`:

```bash
git branch -M main
git push -u origin main
```
