# Plan conceptual

## Historia de usuario

Como integrante del equipo, quiero que cada propuesta de cambio se pruebe
automáticamente, para detectar errores antes de integrarla a la rama principal
y disponer de un reporte de la versión integrada.

## Tareas y criterios de aceptación

| Tarea | Cómo voy a comprobarla |
| --- | --- |
| Crear el repositorio y trabajar con ramas. | Hay commits separados y un PR hacia `main`. |
| Agregar una función simple y sus pruebas. | Los cuatro casos pasan localmente. |
| Definir los eventos del workflow. | Abrir o actualizar un PR inicia la verificación. |
| Preparar un entorno e instalar dependencias. | El log muestra Python 3.12 y la instalación. |
| Ejecutar las pruebas como compuerta de calidad. | Una suma incorrecta da rojo. |
| Producir un artefacto. | Las pruebas generan `site/index.html`. |
| Publicar solo desde `main` si pasa la verificación. | El reporte integrado tiene una URL pública. |
| Manejar un secreto sin escribir su valor. | El job accede a `secrets.DEMO_SECRET` y solo confirma su presencia. |
| Proteger la línea base. | Un PR rojo no se puede integrar por el camino normal. |
| Registrar errores de causas distintas. | Hay un rojo en instalación, otro en pruebas y un verde, con sus logs. |
| Preparar la defensa. | Puedo explicar el YAML y predecir el efecto de un cambio. |

## Decisiones

- Python permite mantener el programa en dos líneas y concentrarse en el proceso.
- pytest expresa cada caso como una comparación fácil de leer.
- pytest-html genera un reporte listo para publicar sin escribir otro programa.
- GitHub Actions corre junto al repositorio y deja cada ejecución asociada al commit.
- GitHub Pages publica el HTML sin contratar otro servicio.
- Dos jobs separan la verificación de la publicación; `needs` expresa su dependencia.
- Primero se prepara el entorno, después se instalan dependencias y recién entonces
  se prueban los resultados. Si un paso falla, los siguientes pasos normales no corren.

## Relación con gestión de la configuración

El código, los tests, las dependencias declaradas y el workflow son ítems de
configuración. Cambiarlos produce un diff y queda registrado en un commit.
El PR permite revisar la propuesta y el pipeline aporta una verificación automática.
`main` representa la línea base; las reglas de protección son las que hacen
obligatorio superar esa verificación antes de integrar.

Versionar el YAML permite saber qué reglas se usaban, revisar modificaciones y
recuperar configuraciones anteriores. Las reglas de protección, los secretos y
la configuración de Pages están en GitHub y también hay que documentarlos:
no todo queda incluido automáticamente en el YAML.
