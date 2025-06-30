# UEA: DAtos A Gran Escala
## 📊 Análisis y Predicción de Clientes en Telecomunicaciones

Este proyecto fue desarrollado en el contexto de la materia **Datos a Gran Escala**, utilizando la herramienta **IBM SPSS Modeler** para aplicar técnicas de análisis y minería de datos sobre un conjunto de información real del sector de telecomunicaciones.

---

## 🎯 Objetivo Del Proyecto

El proyecto tiene dos grandes enfoques:

1. **Clasificación**:
   - Determinar cuál es el **servicio más usado** entre mensajes de texto (SMS) y llamadas.
   - Identificar el **grupo de clientes con mayor propensión a quejas**.

2. **Predicción**:
   - Analizar los factores que inciden en la **tasa de abandono (churn)** de clientes.
   - Estimar qué clientes tienen **mayor riesgo de dejar el servicio**, basándose en variables como:
     - Frecuencia de quejas
     - Tiempo de suscripción
     - Frecuencia de uso

---

## 🗂️ Dataset Utilizado

- Fuente: [UCI Machine Learning Repository - Iranian Churn Dataset](https://archive.ics.uci.edu/dataset/563/iranian+churn+dataset)
- Registros: 3,150
- Atributos: 14 (como llamadas fallidas, frecuencia de uso, edad, valor del cliente, quejas, tipo de plan, churn, etc.)

Se realizó un proceso de preparación, limpieza, balanceo y construcción de nuevas variables (como `usage_preference`).

---

## 🧭 Metodología Aplicada

El proyecto siguió las etapas del **ciclo CRISP-DM**:

1. **Comprensión del negocio y del problema**
2. **Comprensión y exploración de datos**
3. **Preparación y transformación de datos**
4. **Construcción y evaluación de modelos**
5. **Presentación de resultados**

---

## 🛠️ Técnicas Y Modelos Aplicados

Para resolver los problemas de clasificación y predicción se emplearon diversos modelos como:

- 🔵 **Redes neuronales** (MLP, LSVM, Bayesiana, SVM)
- 🔶 **Árboles de decisión** (C5.0, CHAID, CRT, QUEST)
- 🟩 **KNN**
- 🟡 **Regresión logística**
- ⚙️ **Análisis de Componentes Principales (PCA)**
- ⚖️ **Balanceo de clases con datos sintéticos**
- 📈 **Evaluación mediante métricas como precisión, sensibilidad y exactitud**

---

## 📌 Descripcion General

- Se encontró que los **servicios más usados son los SMS**, especialmente entre ciertos grupos de edad.
- Las **principales causas de queja** se relacionan con llamadas fallidas y valor del cliente.
- Se detectó un patrón en los clientes con alta probabilidad de abandono, lo que permite **anticipar bajas y mejorar estrategias de retención**.

---

## 🧾 Recomendaciones Finales

- Implementar estrategias de marketing **basadas en preferencias de uso**.
- Mejorar la **gestión de quejas** y reducir fallas en llamadas.
- Aplicar **segmentación inteligente** para ofrecer planes personalizados a clientes con alto valor.

---

## 📚 Herramientas Utilizadas

- IBM SPSS Modeler
- Google Docs y Notion para documentación y seguimiento
- Python (generación de datos sintéticos)
- Dataset real proporcionado por UCI Machine Learning Repository
  
---
