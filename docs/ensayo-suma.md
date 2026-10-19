# Ensayo de fallo en las pruebas

En el commit `7ba21e6` se cambió temporalmente la suma por una resta.
La instalación pasó y falló el paso de pruebas: tres casos fallaron y uno pasó.
Por ejemplo, `sumar(2, 3)` devolvió `-1` cuando el test esperaba `5`.
El caso con cero pasó porque `7 - 0` y `7 + 0` dan el mismo resultado.

[Corrida roja real](https://github.com/Deathstone16/tp-ci-cd/actions/runs/39188123316).

La protección de `main` dejó el PR bloqueado. La corrección restauró `a + b`
en otro commit y el PR se integró después de aprobar las pruebas.
