# Preparación de la defensa

Este es un mapa para practicar, no un texto para recitar. Adaptar las palabras
a lo que entendés y describir solo lo que efectivamente hayas ejecutado.

## Recorrido de tres minutos

| Tiempo | Qué mostrar | Idea que explicar |
| --- | --- | --- |
| 0:00–0:25 | Diagrama y función | El programa es mínimo para concentrarse en automatizar la verificación. |
| 0:25–1:05 | YAML | El PR dispara el workflow; el runner trae el código, prepara Python, instala y prueba. |
| 1:05–1:40 | Dos corridas rojas | En una falla la instalación; en la otra se ejecutan los tests y el resultado es incorrecto. |
| 1:40–2:10 | Corrida verde y PR | La corrección pasa los tests y el check obligatorio permite integrar. |
| 2:10–2:40 | Job publicar y URL | `needs` exige el verde; solo `main` publica el reporte generado. |
| 2:40–3:00 | Historial y secreto | El YAML queda versionado; el valor del secreto queda fuera del repositorio. |

Dejar las pestañas abiertas antes de empezar. Una ejecución puede tardar más que
la exposición: iniciar una si corresponde, y explicar con las corridas previas
mientras termina. Mostrar el resultado real cuando esté disponible.

## Ideas en palabras sencillas

- **Integración continua:** integrar cambios chicos con frecuencia y comprobarlos
  automáticamente para detectar roturas pronto. Tener un YAML sin integrar seguido
  no alcanza para adoptar la práctica.
- **Entrega continua:** dejar un resultado verificado listo para publicar; una
  persona autoriza su salida.
- **Despliegue continuo:** publicar automáticamente los cambios que pasan los
  controles. En este proyecto lo publicado es un reporte HTML.
- **Runner:** la máquina de GitHub que ejecuta un job. Al arrancar necesita obtener
  el código; que el repositorio esté alojado en GitHub no lo coloca en su carpeta.
- **Job y step:** un job agrupa pasos en el mismo runner; otro job usa otro entorno.
  El artefacto permite pasar el reporte entre los jobs.
- **Quality gate:** la condición para avanzar. Si pytest devuelve error, falla
  `verificar`; `needs` detiene la publicación y la protección de rama bloquea el merge.
- **Artefacto:** el reporte HTML generado por las pruebas y empaquetado para Pages.
- **Secreto:** un valor guardado fuera del código. `${{ secrets.DEMO_SECRET }}`
  referencia el valor; el YAML no lo contiene. El paso solo valida que esté cargado.
- **Línea base:** la versión controlada en `main`, protegida por reglas de integración.
- **Workflow versionado:** puedo ver quién cambió una regla, revisarla y volver a
  una versión anterior. Un panel modificado a mano no deja ese mismo diff junto al código.
- **Versiones fijadas:** reducen sorpresas, aunque este ejemplo no es una congelación
  total del entorno: `3.12` admite distintas revisiones y existen dependencias transitivas.

## Modificación en vivo: predecir antes de ejecutar

Usar una rama de práctica y un PR. No hacer la modificación directamente en `main`.
Estas son predicciones para este workflow y un runner limpio, no errores ya observados.

| Cambio | Predicción y razón |
| --- | --- |
| Comentar solo `run: python -m pip install -r requirements.txt`. | Ese step queda con `name` y sin `run` ni `uses`: el workflow es inválido, no es todavía una dependencia faltante durante los tests. |
| Comentar las dos líneas del step de instalación (`- name` y `run`). | El YAML sigue siendo válido. Sin instalar pytest-html, falla el comando de pruebas por módulo u opciones no disponibles. El mensaje exacto depende de lo que traiga el entorno. |
| Comentar solo el `run` del step de pruebas. | Queda un step sin acción ni comando y GitHub rechaza el workflow. |
| Comentar el step completo de pruebas. | En un PR puede quedar verde sin probar: se eliminó la compuerta. En `main` también falta `site/` y la carga del reporte debe fallar. |
| Comentar `needs: verificar`. | Publicar ya no espera a verificar y puede intentar desplegar sin tener el artefacto. El resultado exacto depende de los tiempos; se perdió la garantía de orden. |
| Comentar solo el `if` de `publicar`. | También intenta publicar desde PR; allí no se carga el artefacto y puede ser bloqueado por el environment o fallar al buscarlo. |

La modificación de una sola línea más clara para practicar es comentar el `run`
de instalación y reconocer que produce un **error de definición del workflow**.
Si se quiere demostrar una dependencia faltante durante la ejecución, hay que
quitar el step completo manteniendo un YAML válido.

Después de la prueba, restaurar el archivo, hacer commit y confirmar el verde.

## Preguntas para comprobar que lo entendés

1. Si todo pasa en mi máquina, ¿por qué ejecutar también en un runner limpio?
2. ¿Por qué una dependencia que no se instala impide probar el programa?
3. ¿Qué diferencia hay entre un test que falla y un workflow que ni siquiera es válido?
4. ¿Qué bloquea de verdad el merge: el color rojo o la regla de protección?
5. ¿Por qué un PR con cuatro tests verdes no publica un sitio en este diseño?
6. ¿Dónde se autoriza la publicación si usamos aprobación manual?
7. ¿Qué cosas quedan en Git y cuáles se configuran fuera del repositorio?

No pasar de etapa hasta poder responderlas mirando los archivos.
