----------------------------------------------------------------------------------------
         ANALISIS VARICELA 2017-2019 
----------------------------------------------------------------------------------------
0) Introducción 
En el siguiente modelo, tiene como objetivo mostrar la epidemiología (la distribución, frecuencia y determinantes de las enfermedades de la varicela y cómo evoluciona en los pacientes a lo largo del tiempo) usando este dataset de egresos hospitalarios desde el año 2017 hasta el 2019. Aclaro que soy estudiante de tercer año de ciencias de datos y este es un mini proyecto para pulir mis habilidades en análisis, criterio e "investigación" en  ciencias de datos. Tambien satisfacer mi curiosidad sobre el tema porque justo salgo de la enfermedad de la varicela  y me dio curiosidad sobre como evoluciona a lo largo del tiempo y que tan grave es los datasets que conseguí son públicos, aclaro que las regiones sanitarias son las siguientes que se encuentra en los links que dejo después. También se puede encontrar la población estimada de cada region sanitaria del censo( varios censos) con los links que dejo a continuación.
--------------------------------
0.1) links:
 I) https://www.gba.gob.ar/saludprovincia/regiones_sanitarias #regiones sanitarias
 II) https://www.gba.gob.ar/saludprovincia/regiones_sanitarias#:~:text=REGI%C3%93N%20SANITARIA%20I,-AUTORIDADES&text=La%20poblaci%C3%B3n%20total%20(seg%C3%BAn%20el,la%20ciudad%20de%20Bah%C3%ADa%20Blanca #poblacion de cada region, tenes que buscar por region cuanta población tiene
 III) datos.gob.ar  # fuente de dtao
------------------------------
PREGUNTAS IMPORTANTES QUE ME REALICE: 
a) ¿Qué grupos etarios son mas vulnerables? ¿Hay diferencias entre sexos?
b) Evolución anual de la enfermedad
c) ¿Que regiones sanitarias de la provincia de Buenos Aires tienen mas casos de varicela? 
d) ¿Los brotes de varicela están relacionados con la densidad poblacional?
e) ¿Cuál es el impacto de la varicela en la mortalidad o en las complicaciones graves?
f) Clasificación de riesgo de brotes en distintas regiones
----------------------------------------------------------------------------------------
1)Bibliotecas a importar 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

-----------------------------------------------------------------------------------------
2) Instrucciones de ejecución
-----------------------------------------------------------------------------------------

*) Tener los archivos "egresos-2017, egresos-2018,egresos-2019" instalado en la misma carpeta donde se encuentre el código.

*) Abrir el código en un IDE (recomendamos Spyder).

*) Ejecutar el código completo o en celdas (separados con #%%).

*) Revisar los resultados una vez finalizado su ejecución (en la parte de graficos y explorador de variables).
--------------------------------------------------------------------------------------------
3) ¿Por que es util el proyecto? 
--------------------------------------------------------------------------------------------
 La varicela, aunque se considera una enfermedad común y generalmente leve en niños, puede ser peligrosa en ciertos grupos de población, como adultos, inmunocomprometidos o embarazadas. Identificar regiones de alto riesgo de brotes de manera anticipada permite a las autoridades de salud tomar medidas preventivas, como campañas de vacunación o medidas de aislamiento.
 Si se confirma que hay una relación entre densidad poblacional y brotes, las áreas más densamente pobladas deben ser priorizadas para campañas de vacunación y educación por eso deje los links de regiones sanitarias donde aparece un estimado de la población por region sanitaria, nos da una información clave donde las regiones sanitaria que mas tienen casos de varicela es donde se encuentra la mayor cantidad de población, lo cual se concluye como una sospecha de que los brotes están relacionados con la densidad poblacional.

 Al conocer qué grupos etarios son más vulnerables, las políticas de salud pueden dirigirse específicamente a esos grupos. Por ejemplo, si los niños menores de 5 años o los adultos son los más afectados, se pueden tomar medidas para reforzar la vacunación en esos grupos.

Saber en qué regiones hay más casos permite asignar recursos de manera eficiente. Por ejemplo, si una región tiene muchos casos, se puede enviar vacunas, personal de salud o realizar campañas educativas para reducir la propagación.

Este tipo de análisis ayuda a predecir cómo se comportarán otros brotes epidémicos y a implementar políticas públicas adecuadas para contenerlos.
****
