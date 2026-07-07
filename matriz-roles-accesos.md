# Matriz de Roles y Accesos - SoftCorp

Aplica el **principio de menor privilegio**: cada rol tiene solo el acceso mínimo necesario, y los entornos están completamente aislados entre sí (a diferencia de la situación actual, donde staging y producción comparten credenciales administrativas).

| Rol | Repositorio (código) | Entorno Desarrollo | Entorno Staging | Entorno Producción | Vault |
|---|---|---|---|---|---|
| **Desarrollador** | Lectura/Escritura (rama propia, requiere PR) | Acceso completo | Sin acceso | Sin acceso | Sin acceso a secretos de producción |
| **Tech Lead / Revisor** | Lectura/Escritura + aprobar Pull Requests | Acceso completo | Lectura | Sin acceso | Lectura de secretos de staging |
| **DevOps / Pipeline (cuenta de servicio)** | Lectura (solo para ejecutar el pipeline) | N/A | Escritura (despliegue automático) | Escritura (despliegue automático, solo vía pipeline aprobado) | Acceso de inyección dinámica (token de corta duración) |
| **Administrador de Infraestructura** | Sin acceso directo al código | Administración | Administración | Administración (con MFA y aprobación de doble control) | Administración completa (root token restringido) |
| **Auditor / Compliance** | Lectura (solo lectura de historial) | Sin acceso | Solo logs | Solo logs | Solo logs de acceso (audit log de Vault) |

## Principios aplicados

1. **Ningún humano tiene credenciales permanentes de producción.** Solo la cuenta de servicio del pipeline puede desplegar, y solo después de que las 3 etapas de seguridad (SAST, SCA, Secret Scanning) pasen.
2. **Separación de entornos:** las credenciales de staging y producción son distintas y están en rutas (`paths`) separadas dentro de Vault (`secret/softcorp/staging/*` vs `secret/softcorp/production/*`).
3. **Aprobación obligatoria (Pull Request):** ningún cambio llega a `main` sin revisión de al menos un Tech Lead.
4. **Tokens de corta duración:** el acceso del pipeline a Vault usa tokens que expiran, no credenciales estáticas.
