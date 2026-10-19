# Guía de ejecución

Esta guía permite reproducir el proceso desde un repositorio nuevo. El repositorio
del TP ya está configurado y sus corridas reales están registradas en
[las evidencias](03-evidencias.md). Para practicar en él, usar una rama nueva y un PR;
no repetir `git init`, crear otro remoto ni intentar subir directamente a `main`.

## 1. Entender el programa

`sumar(2, 3)` devuelve `5`. `assert sumar(2, 3) == 5` comprueba ese resultado.
Si cambiamos `+` por `-`, devuelve `-1` y la comparación falla. pytest termina
con código distinto de cero; Actions interpreta ese código como un fallo.

Ejecutar los comandos del README. Antes de seguir, poder explicar qué archivo
contiene la función, cuál la prueba y dónde se genera el HTML.

## 2. Crear el repositorio por etapas

Crear un repositorio vacío de GitHub con nombre, por ejemplo, `tp-ci-cd`.
Para usar Pages con una cuenta gratuita, usar un repositorio público si está permitido
por la cátedra. Si se usa uno privado, verificar qué admite el plan de la cuenta.
No inicializarlo con otro README si se van a usar estos comandos.

Desde la carpeta del proyecto:

```powershell
git init -b main
git add .gitignore calculadora.py test_calculadora.py requirements.txt
git commit -m "Agrego suma y pruebas de casos basicos"
```

Si Git solicita nombre y correo, configurar los propios. No inventar la identidad
del autor ni fechas. Luego reemplazar `TU_USUARIO` en el comando siguiente:

```powershell
git remote add origin https://github.com/TU_USUARIO/tp-ci-cd.git
git push -u origin main
git add .github/workflows/pipeline.yml
git commit -m "Agrego verificacion y publicacion del reporte"
```

Todavía no subir ese segundo commit: primero configurar GitHub como sigue.

## 3. Configurar GitHub

1. En **Settings > Pages > Build and deployment**, elegir **GitHub Actions**.
2. En **Settings > Secrets and variables > Actions**, crear un repository secret
   llamado `DEMO_SECRET`. Usar un valor de demostración inventado, no una contraseña
   personal. El valor se carga únicamente en ese formulario.
3. Si se quiere aprobación humana, crear o editar el environment `github-pages`
   en **Settings > Environments** y agregar un **Required reviewer**.
   Para una demo individual, permitir la aprobación de la propia ejecución.
   Restringir las ramas de despliegue a `main`.
4. Ahora ejecutar `git push`. Abrir **Actions > CI y reporte** y observar los jobs.
5. Si configuraste aprobación, usar **Review deployments** y aprobar para publicar.
6. Abrir la URL que muestra `Publicar reporte`. Confirmar los cuatro casos en verde.

Si falta `DEMO_SECRET`, falla la comprobación del secreto en `publicar`; eso
es un problema de configuración, no un fallo de la función. Si Pages no está
habilitado, la publicación puede fallar aunque las pruebas pasen.

## 4. Proteger main

Cuando ya existe una primera ejecución, en **Settings > Branches** crear una regla
para `main` (o un ruleset equivalente): exigir PR antes del merge y exigir que pase
el status check **Verificar**. Elegir el nombre que efectivamente muestra GitHub.
Exigir que la rama esté actualizada antes del merge ayuda a validar la integración.
Aplicar la regla a administradores/deshabilitar bypass para poder demostrar el bloqueo.

Para un TP individual no hace falta exigir la aprobación de otra persona al PR;
eso es independiente del status check y de la aprobación del despliegue.
Si la cuenta no ofrece protección para ese tipo de repositorio, registrar la
limitación y revisarla con el docente; no afirmar que la protección está activa.

## 5. Primer rojo: resultado incorrecto

```powershell
git switch -c demo/error-suma
```

En `calculadora.py`, cambiar solo `return a + b` por `return a - b`.

```powershell
git add calculadora.py
git commit -m "Ensayo fallo de pruebas al cambiar la suma"
git push -u origin demo/error-suma
```

Abrir un PR desde esa rama hacia `main`. La ejecución empieza al abrir el PR.
La instalación debe pasar y **Ejecutar pruebas y generar reporte** debe fallar.
Expandir el log y buscar `AssertionError` y la comparación entre lo obtenido y
lo esperado. Guardar captura y URL antes de corregir.

Devolver la línea a `return a + b`, hacer un nuevo commit y push a la misma rama.
El mismo PR se vuelve a verificar. Guardar la corrida verde. Integrar el PR solo
cuando el check pase; después del merge, observar la publicación en `main`.

## 6. Segundo rojo: dependencia no disponible

Con el PR anterior ya integrado:

```powershell
git switch main
git pull --ff-only
git switch -c demo/error-dependencia
```

En `requirements.txt`, cambiar `pytest-html==4.1.1` por `pytest-html==0.0.0`.
Esa versión no está disponible y pip no puede satisfacer el requerimiento.
Hacer commit, push y abrir otro PR hacia `main`.

```powershell
git add requirements.txt
git commit -m "Ensayo dependencia no disponible"
git push -u origin demo/error-dependencia
```

Ahora falla **Instalar dependencias**. Buscar `No matching distribution found`
o `Could not find a version that satisfies the requirement`. Las pruebas quedan
sin ejecutar: no hubo una comparación de resultados, falló la preparación del entorno.
Guardar la captura y URL. Restaurar `pytest-html==4.1.1`, hacer commit y push,
esperar el verde e integrar el PR. No integrar deliberadamente ninguna versión rota.

## 7. Documentar y cerrar

Completar `03-evidencias.md` con los datos observados. Agregar las capturas dentro
de `docs/evidencias/`, sin secretos. Incorporar README, plan, diagrama y guías en
un PR de documentación. Los mensajes de commit de esta guía son sugerencias;
el historial debe describir las acciones que realmente se hicieron.

Confirmar que hay dos rojos de causas distintas, un verde, un reporte público y
una demostración de bloqueo de merge. Practicar la exposición de tres minutos.
