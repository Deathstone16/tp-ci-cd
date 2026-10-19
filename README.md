# Trabajo práctico: pipeline CI/CD

Fundamentos de Ingeniería de Software — Gestión de la Configuración del Software.

[![CI y reporte](https://github.com/Deathstone16/tp-ci-cd/actions/workflows/pipeline.yml/badge.svg)](https://github.com/Deathstone16/tp-ci-cd/actions/workflows/pipeline.yml)

El proyecto usa una función que suma dos números para comprobar el funcionamiento
de un pipeline de integración y publicación con GitHub Actions.

## Contenido

- `calculadora.py`: función de suma.
- `test_calculadora.py`: pruebas con positivos, negativos, cero y decimales.
- `requirements.txt`: dependencias y sus versiones.
- `.github/workflows/pipeline.yml`: configuración del pipeline.
- [Plan de trabajo](docs/plan.md).
- [Evidencias de las ejecuciones](docs/evidencias.md).

![Pipeline y herramientas utilizadas](docs/pipeline.png)

## Ejecución local

Con Python 3.12, desde la carpeta del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v --html=site/index.html --self-contained-html
```

Las cuatro pruebas deben pasar. El reporte se genera en `site/index.html` y se
puede abrir con el navegador.

## Funcionamiento del pipeline

Un pull request hacia `main` inicia el job `Verificar`. El runner usa Ubuntu
24.04, obtiene el código, prepara Python 3.12, instala las dependencias y ejecuta
las pruebas. Si algún paso falla, el job queda en rojo.

La rama `main` exige un pull request y el check `Verificar` aprobado. Al integrar
un cambio, un nuevo pipeline verifica la versión de `main`, guarda el reporte
como artefacto y lo publica en GitHub Pages. `needs: verificar` establece que
el job `publicar` solo avance después de una verificación exitosa. Los PR no publican.

**Reporte público:** [ver resultados](https://deathstone16.github.io/tp-ci-cd/).

## Configuración

- Pages está configurado para publicar mediante GitHub Actions.
- El environment `github-pages` permite desplegar desde `main`.
- El job de publicación tiene permisos `pages: write` e `id-token: write`.
- `DEMO_SECRET` está guardado en los secretos del repositorio. El workflow solo
  comprueba que exista y no muestra su valor. Es una demostración del uso de
  secretos; la autenticación de Pages la gestiona GitHub.

El reporte se publica automáticamente después de las pruebas, por lo que esa
etapa funciona como despliegue continuo. Para usar una aprobación manual antes
de publicar, se puede agregar un revisor requerido al environment `github-pages`;
ese modo corresponde a entrega continua. Actualmente no se exige esa aprobación.

El código, los tests, las dependencias y el YAML quedan versionados juntos. Las
reglas de protección, Pages y los valores de los secretos se configuran en GitHub.

## Referencias

- [GitHub Actions y Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
- [Secretos en GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).
- [Reportes con pytest-html](https://pytest-html.readthedocs.io/en/latest/user_guide.html).
