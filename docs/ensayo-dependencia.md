# Ensayo de fallo al instalar dependencias

En el commit `89ec3f0` se pidió temporalmente `pytest-html==0.0.0`, una versión
inexistente. pip informó `No matching distribution found` y terminó con código 1.
Falló el paso de instalación y las pruebas quedaron sin ejecutar.

[Corrida roja real](https://github.com/Deathstone16/tp-ci-cd/actions/runs/39188131263).

Esto es diferente del error de suma: en ese caso el entorno se instaló bien y
los tests detectaron un resultado incorrecto. La corrección de este ensayo
restaura `pytest-html==4.1.1`. El PR se actualizó con `main` para volver a
verificarlo sobre la línea base vigente antes de integrar.
