## Guía de Worflow Git
A la hora de desarrollar se apunta a `develop`, mientras que `master` se reserva únicamente para versiones estables de producción.

## Convención para Nombres de Ramas de trabajo
* **Nuevas funcionalidades:** `feature/descripcion-corta` (ej. `feature/nombre-tarea`)
* **Corrección de errores:** `fix/descripcion-corta` (ej. `fix/error-login`)
---

### 🚀 Flujo de Trabajo Diario

#### 1. Iniciar desde `develop`
Asegurarse de obtener siempre los últimos cambios antes de crear la rama:
```bash
git checkout develop
git pull origin develop
git checkout -b feature/nombre-de-tu-rama
```

#### 2. Guardar y subir cambios
Escribir mensajes de commit claros con el siguiente formato
```bash
git add .
git commit -m "feat: CRUD de Servicios"
git push -u origin featrure/nombre-de-tu-rama
```
#### 3. Abrir un PullRequest (PR)
* Crear PullRequest en GitHub
* **Base(destino): `develop` $\leftarrow$ Compare (origin): `feature/nombre-de-tu-rama`.**
* Solicitar la revisión.
* Tras la aprobación y verificación de pruebas, hacer **Squash and Merge**
* Eliminar la rama remota en GitHub
