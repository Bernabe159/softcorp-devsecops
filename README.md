# SoftCorp - Pipeline DevSecOps

Laboratorio Blue Team: implementación de un pipeline de CI/CD seguro para SoftCorp,
integrando SAST, SCA, Secret Scanning y una bóveda de secretos (Vault).

## Estructura del proyecto

```
softcorp-devsecops/
├── .github/workflows/pipeline.yml   # Pipeline de GitHub Actions (SAST + SCA + Secret Scanning)
├── .pre-commit-config.yaml           # Hook local que bloquea secretos antes del commit
├── app/
│   ├── app.py                        # Versión "insegura" (credencial hardcodeada) - para la demo
│   ├── vault_client.py               # Versión corregida - obtiene el secreto desde Vault
│   └── requirements.txt              # Incluye dependencias vulnerables a propósito (demo SCA)
├── matriz-roles-accesos.md           # Entregable: matriz de roles y accesos
└── GUIA-GIT-BASICO.md                # Guía de comandos Git para este proyecto
```

## Orden sugerido de trabajo

1. Sigue `GUIA-GIT-BASICO.md` para subir este proyecto a tu propio GitHub.
2. Verifica que el pipeline corre solo (pestaña "Actions" en GitHub) y que Trivy detecta
   las vulnerabilidades en `requirements.txt`.
3. Instala Docker Desktop y levanta Vault en modo dev (instrucciones dentro de `vault_client.py`).
4. Instala `pre-commit` (`pip install pre-commit && pre-commit install`) para activar el hook local.
5. Prepara la demo: un commit que falla (secreto detectado) y luego uno que pasa limpio.

## Entregables que cubre este repositorio

| Entregable del caso | Dónde está |
|---|---|
| Diagrama del flujo del pipeline | (pendiente: se genera aparte, ver conversación) |
| Archivo de configuración del pipeline | `.github/workflows/pipeline.yml` |
| Evidencia de integración con Vault | `app/vault_client.py` |
| Matriz de roles y accesos | `matriz-roles-accesos.md` |
| Reporte de vulnerabilidades mitigadas | Se genera automáticamente al correr el pipeline (pestaña Actions → job Trivy) |
