# Instrucciones para el proyecto

### Configuración del entorno

Este proyecto requiere Python 3.x y varias bibliotecas de terceros que interactúan con bases de datos y manejan la manipulación de datos. A continuación, se ofrecen las instrucciones para configurar tu entorno e instalar las dependencias necesarias.

#### Pre - requisitos
Python 3.x instalado en tu sistema. Puedes descargarlo desde Python.org.

#### Dependencias
El script utiliza varias bibliotecas externas que se pueden instalar usando el gestor de paquetes de Python, pip. Ejecuta los siguientes comandos en tu terminal para instalarlas:

```
# Instala pandas para la manipulación de datos
pip install pandas
# Instala pyarrow para el almacenamiento y recuperación eficiente de datos y fsspec para la interfaz del sistema de archivos
pip install pyarrow fsspec
# Instala scikit-learn para implementar algoritmos de aprendizaje automático
pip install scikit-learn
# Instala seaborn para visualización avanzada de datos
pip install seaborn
# Instala xgboost para algoritmos de aprendizaje automático de impulso de gradiente optimizado
pip install xgboost

```

#### Análisis de datos:

![Arrears_Days_By_Client_id](https://github.com/natacardona/CreditInsight/blob/main/docs/figures/Arrears_Days_By_Client_id.png)

El gráfico "Arrears Days by Client ID" destaca las diferencias significativas en los días de mora entre clientes. Los puntos clave incluyen:
Diversidad en el Comportamiento de Pago: Algunos clientes presentan moras severas, mientras que un grupo notable mantiene sus pagos al día, reflejando la variabilidad en el cumplimiento financiero.

- <b>Presencia de Outliers</b>: Clientes con moras extremadamente altas sugieren riesgos potenciales que requieren atención específica para minimizar impactos financieros negativos.
- <b>Estrategias de Intervención</b>: La identificación de clientes con altos niveles de mora es crucial para implementar estrategias de gestión de riesgo efectivas y personalizadas.
- <b>Implicaciones Estratégicas</b>:
- <b>Revisión de Políticas de Crédito</b>: Ajustar criterios de concesión para prevenir altos niveles de mora.
- <b>Segmentación para Intervención</b>: Focalizar recursos en clientes de alto riesgo mediante estrategias de cobranza ajustadas o reestructuración de deudas.

Estos hallazgos son esenciales para optimizar la gestión del riesgo y la salud financiera de la entidad, permitiendo una planificación más efectiva y dirigida.


![Arrears_Days_Log_Scale](https://github.com/natacardona/CreditInsight/blob/main/docs/figures/Arrears_Days_Log_Scale.png)

#### Análisis de la Distribución de Días en Mora:

- <b>Predominio de Pagos Puntuales</b>: La mayoría de los préstamos se pagan a tiempo o con pequeños retrasos, lo que indica una buena salud crediticia en general de la cartera.
- <b>Disminución Exponencial de Mora</b>: Se observa una disminución exponencial en la frecuencia de los días en mora a medida que estos aumentan, lo que es típico en el comportamiento de pago de los prestatarios.
- <b>Riesgos en la Cola Larga</b>: Existen casos atípicos con moras significativas que representan riesgos potencialmente altos. Estos casos requieren atención especial para mitigar riesgos financieros.


#### Implicaciones para el Negocio:

- <b>Gestión de Riesgos</b>: La presencia de una cola larga en la distribución sugiere la necesidad de estrategias robustas de gestión de riesgos para identificar y actuar sobre los préstamos de alto riesgo.
- <b>Estrategia de Crédito</b>: Ajustar las políticas de crédito podría ser prudente para minimizar las moras prolongadas y mejorar la salud general del portafolio.

#### Recomendaciones Estratégicas:

- <b>Segmentación y Análisis Detallado</b>: Realizar análisis más detallados por segmento de préstamo y demografía del prestatario para entender mejor los patrones de riesgo.
- <b>Análisis Temporal</b>: Evaluar cómo las tendencias de mora evolucionan a lo largo del tiempo para anticipar cambios y adaptar estrategias proactivamente.

![Arrears_Days_Per_Year](https://github.com/natacardona/CreditInsight/blob/main/docs/figures/Arrears_Days_Per_Year.png)

#### Observaciones Clave:

- <b>Tendencia Ascendente</b>: Desde principios de 2022, se observa un aumento significativo en los días totales de mora, indicando un deterioro en la capacidad de pago de los clientes a lo largo del tiempo.
- <b>Patrones Estacionales</b>: Se identifican fluctuaciones que podrían estar relacionadas con eventos estacionales o ciclos económicos que afectan la capacidad de pago de los clientes.

#### Implicaciones Estratégicas:

- <b>Optimización de Cobranzas</b>: Es crucial fortalecer las estrategias de cobranza y considerar programas proactivos de gestión de riesgos para prevenir la morosidad.
- <b>Modelo de Scoring Dinámico</b>: Adaptar los modelos de riesgo de crédito a las tendencias observadas permite una respuesta más ágil y eficaz ante los cambios en el comportamiento de pago.
- <b>Preparación Ante Volatilidad</b>: Anticipar periodos de alta volatilidad y ajustar las reservas para riesgos crediticios puede mejorar la resiliencia financiera de la empresa.

#### Conclusión: 

El análisis destaca la importancia de una gestión proactiva del riesgo crediticio y la necesidad de adaptar continuamente las estrategias de crédito y cobranza para mitigar impactos negativos y aprovechar oportunidades de mejora en la eficiencia operativa.

![Heat_Map_Activation_Year](https://github.com/natacardona/CreditInsight/blob/main/docs/figures/Heat_Map_Activation_Year.png)

#### Observaciones Clave:

- <b>Tendencia General</b>: Hay una tendencia decreciente en la activación de préstamos desde el último trimestre de 2021 hasta el último trimestre disponible en 2024. Esta tendencia podría indicar cambios en la política de préstamos, condiciones del mercado, o la demanda de crédito por parte de los consumidores.

- <b>Variabilidad Estacional</b>: Se observa una variabilidad significativa entre los trimestres. Por ejemplo, los trimestres Q4 de cada año muestran picos en la actividad, lo que puede sugerir una tendencia estacional en la que los consumidores tienden a solicitar más préstamos durante el final del año.
Año 2021: El año 2021 muestra un aumento constante en la activación de préstamos, culminando en el último trimestre con el pico más alto en todo el período observado (22,790 préstamos activados).

- <b>Disminución Posterior</b>: A partir de 2022, hay una disminución notable en la activación de préstamos, siendo más marcada en 2024 con una disminución sostenida a lo largo de los trimestres.

#### Implicaciones para el Negocio:

- <b>Gestión de Riesgos y Oportunidades</b>: El descenso en la activación puede señalar una oportunidad para revisar las estrategias de concesión de créditos y marketing para reactivar el crecimiento o ajustar los productos a las necesidades del mercado.
- <b>Planificación Estratégica</b>: La estacionalidad detectada puede ser utilizada para planificar campañas de marketing y ofertas especiales que coincidan con los aumentos de demanda al final de cada año.
- <b>Evaluación de Políticas de Crédito</b>: La tendencia decreciente subraya la necesidad de evaluar las políticas de crédito para asegurarse de que siguen siendo competitivas y atractivas para los clientes potenciales.

#### Recomendaciones:

- <b>Análisis Segmentado</b>: Realizar un análisis más detallado para entender qué segmentos de préstamo están declinando más y cuáles mantienen su rendimiento.
- <b>Estrategias Promocionales</b>: Considerar la implementación de estrategias promocionales o ajustes en las condiciones de préstamo durante los trimestres más bajos para estimular la demanda.
- <b>Revisión de Condiciones del Mercado</b>: Analizar las condiciones del mercado externo que podrían estar influyendo en estos patrones, como cambios económicos, tasas de interés, o competencia

## Descripción del modelo de aprendizaje usado:

### Preparación de Datos:

Antes de empezar con el modelo, fue necesario organizar y preparar los datos recopilados. Esto incluyó la selección de la información relevante, como las fechas de activación de los préstamos y los días de atraso en los pagos, y realizar algunos cálculos preliminares para entender cuánto tiempo ha pasado desde que se activó cada préstamo hasta la fecha de atraso reportada.

#### División de Datos:
Los datos se dividieron en dos grupos: uno para entrenar (aprender) el modelo y otro para probar (verificar) su precisión. Esto es similar a estudiar para un examen con ciertos temas y luego tomar el examen para ver cuánto has aprendido.

#### Normalización de Datos:
Para que el modelo funcione correctamente y de manera justa, fue necesario asegurar que todos los datos estuvieran en la misma escala. Por ejemplo, si en un dato se cuentan días y en otro se cuentan dólares, estos deben convertirse a una escala común para evitar sesgos.

#### Entrenamiento del Modelo:
Con los datos preparados y normalizados, se procedió a entrenar el modelo. Esto implicó usar un método estadístico para aprender de los datos de entrenamiento, específicamente buscando patrones que ayuden a prever si un cliente podría dejar de pagar en el futuro.
Evaluación del Modelo:

Una vez entrenado el modelo, se evaluó su eficacia utilizando los datos de prueba. Se emplearon varias técnicas estadísticas para medir qué tan bien el modelo podía predecir los resultados comparándolos con lo que realmente ocurrió.

#### Análisis de Resultados:

Finalmente, se analizó cuáles factores (como la cantidad de días de atraso) influyen más en la probabilidad de que un cliente deje de pagar, lo cual es crucial para tomar decisiones informadas y mejorar las estrategias de crédito.

## Acerca de los resultados otorgados por el modelo de machine learning

### Evaluación del Modelo

``` AUC Score: 0.9999976504452557``` 

- El AUC (Área Bajo la Curva ROC) es una medida de la capacidad del modelo para distinguir entre las clases (clientes que cumplen y no cumplen). Un valor cercano a 1 indica una excelente capacidad discriminatoria.

### Matriz de confusión

```
[[88186    37]
[    0  1510]]
```

- Esta matriz muestra el número de predicciones correctas e incorrectas. En tu modelo, 88186 predicciones correctas de no incumplimiento, 37 incorrectas, y 1510 predicciones correctas de incumplimiento.

### Reporte de Clasificación:

- Precision: ¿Cuánto de lo que el modelo predijo como incumplimiento era realmente incumplimiento?
- Recall: ¿Cuánto de los verdaderos incumplimientos fue identificado por el modelo?
- F1-score: Media armónica entre Precision y Recall, útil cuando las clases están desbalanceadas.
```
              precision    recall  f1-score   support
           0       1.00      1.00      1.00     88223
           1       0.98      1.00      0.99      1510
```
### Importancia de las Características:

Muestra qué tan influyentes son las variables para las predicciones del modelo.

```
                 Feature  Coefficient
0           ARREARS_DAYS     9.794924
1   rolling_arrears_mean    -0.455387
2  days_since_activation    -0.536323
```

Este análisis detallado ofrece una visión clara de cómo el modelo está funcionando y qué factores son los más determinantes para prever los incumplimientos, facilitando la toma de decisiones estratégicas y ajustes en políticas de crédito.
