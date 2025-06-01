# 🧬 Proyecto ACA – Autómata Celular Académico

![Simulación de Autómata Celular](https://img.shields.io/badge/Estado-En%20Desarrollo-orange)

---

## 📖 Descripción

ACA (Autómata Celular Académico) es un simulador de autómatas celulares inspirado en el **Juego de la Vida** de Conway, extendido con “milagros” especiales que introducen nacimientos extraordinarios.  
La simulación se desarrolla sobre una matriz de hasta 20×20 celdas (extensible a 30×30), donde cada celda puede estar vacía, contener una célula normal (`O`) o una célula ángel (`A`). El programa evoluciona la matriz generación a generación, aplicando reglas de supervivencia, nacimiento y muerte, así como eventos milagrosos bajo ciertas condiciones.

---

## 📋 Tabla de Contenidos

1. [Objetivos](#-objetivos)  
2. [Requerimientos](#-requerimientos)  
3. [Estructura de Archivos](#-estructura-de-archivos)  
4. [Instalación y Uso](#-instalación-y-uso)  
5. [Descripción de Funciones](#-descripción-de-funciones)  
6. [Formato de Entrada y Salida](#-formato-de-entrada-y-salida)  
7. [Milagros Especiales](#-milagros-especiales)  
8. [Recomendaciones de Prueba](#-recomendaciones-de-prueba)  

---

## 🎯 Objetivos

- **Leer y cargar** una configuración inicial desde un archivo de texto (`acaentra.txt`) o entrada manual.  
- **Modificar dinámicamente** la matriz: agregar/eliminar células bajo demanda.  
- **Generar configuraciones aleatorias** basadas en un número de células vivas definido o al azar.  
- **Simular la evolución** de la matriz generación a generación, imprimiendo cada estado en pantalla.  
- **Aplicar “milagros”** especiales (nacimientos extraordinarios) cuando el usuario lo solicite.  
- **Ejecutar X generaciones** de una sola vez, deteniéndose si no quedan células vivas.  
- **Guardar el estado final** de la matriz en un archivo de salida (`acasali.txt`).  
- **Ofrecer una interfaz de texto** amigable, modular y bien documentada.

---

## ⚙️ Requerimientos

- Python 3.7 o superior.
- Solo librerías estándar de Python o las vistas en clases (cualquier otro uso de librerias no vistas en clases y holguin nos mete un 00 de una).  
- Terminal o consola para ejecutar el script. (como si los sistemas no tuvieran terminal, pero cabe recalcar)

---

## 📂 Estructura de Archivos

```
/ACA-Project
│
├── README.md                ← Documentación principal (este archivo)
├── acaentra.txt             ← Archivo de entrada de ejemplo (configuración inicial)
├── acasali.txt              ← Archivo de salida generado tras la simulación
└── ZamoraLP.py              ← Archivo principal de Python (reemplazar con tu apellido e iniciales)
```

> **Nota:**  
> El nombre del archivo `.py` debe seguir la convención:  
> `ApellidoIniciales.py`  
> Ejemplo: `ZamoraLP.py` (si el integrante más raro del grupo se apellida Zamora y las iniciales de los demás son L y P).

---

## 🚀 Instalación y Uso

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tu-usuario/ACA-Project.git
   cd ACA-Project
   ```

2. **Preparar el archivo de entrada**  
   - Edita `acaentra.txt` con el formato correcto (ver sección “Formato de Entrada y Salida”).  
   - Opcional: no incluir `acaentra.txt` y elegir la opción de “entrada manual” al ejecutar.

3. **Ejecutar el programa**  
   ```bash
   python ZamoraLP.py
   ```
   _(Sustituye `ZamoraLP.py` por el nombre real de tu archivo .py)_

4. **Opciones del menú principal**  
   Al iniciar, se mostrará un menú con opciones numeradas:
   1. Cargar archivo de entrada  
   2. Ingreso manual de población inicial  
   3. Generar configuración aleatoria  
   4. Mostrar matriz actual  
   5. Evolucionar 1 generación  
   6. Evolucionar X generaciones  
   7. Aplicar un “milagro”  
   8. Modificar células manualmente  
   9. Guardar estado final en archivo  
   0. Salir del programa  

   Sigue las indicaciones en pantalla para seleccionar y confirmar cada acción.

---

## 🔍 Descripción de Funciones

A continuación se listan las funciones principales que componen el programa, junto con su propósito y comportamiento esperado:

1. **`leer_archivo_entrada(filename: str) → matriz`**  
   - Lee el archivo `acaentra.txt`.  
   - Primera línea: dimensiones `n,m` (10 ≤ n,m ≤ 30).  
   - Líneas siguientes: coordenadas `i,j` (fila, columna) de cada célula viva.  
   - Retorna una matriz de tamaño `n × m`, con `1` para célula viva normal y `0` para vacía.

2. **`guardar_archivo_salida(filename: str, matriz)`**  
   - Recorre la matriz final y escribe en `acasali.txt` las líneas `i,j` de cada célula viva.  
   - Formato idéntico al de entrada: sin espacios, separadas por comas.

3. **`inicializar_matriz_aleatoria(n: int, m: int, cantidad: Optional[int]) → matriz`**  
   - Si `cantidad` es `None`, elige un número aleatorio de células vivas entre `n` y `n*m`.  
   - Distribuye de forma aleatoria las células en la matriz con `cantidad` posiciones vivas (valor `1`).  
   - Devuelve la matriz inicial.

4. **`mostrar_matriz(matriz)`**  
   - Imprime la matriz en pantalla:  
     - `.` → celda vacía  
     - `O` → célula viva normal  
     - `A` → célula ángel  
   - Cada fila en una línea, sin corchetes ni comas.

5. **`contar_vecinos(matriz, i: int, j: int) → int`**  
   - Dada la posición `(i,j)`, contabiliza las 8 celdas vecinas (arriba, abajo, izquierda, derecha y diagonales).  
   - Considera que fuera de límites son celdas vacías.  
   - Devuelve el conteo de células vivas (normales y ángeles).

6. **`actualizar_generacion(matriz) → nueva_matriz`**  
   - Recorre cada celda y aplica las reglas de evolución:  
     - **Regla 1 (soledad):** Si está viva y ≤1 vecino, muere.  
     - **Regla 2 (superpoblación):** Si está viva y ≥4 vecinos, muere.  
     - **Regla 3 (supervivencia):** Si está viva y tiene 2 o 3 vecinos, sobrevive.  
     - **Regla 4 (nacimiento):** Si está vacía y tiene exactamente 3 vecinos, nace célula normal.  
   - **Importante:** Todas las actualizaciones se basan en el estado actual; no modificar la matriz original durante el recorrido.

7. **`verificar_extincion(matriz) → bool`**  
   - Revisa si existen células vivas (valores `1` o `2` para ángeles) en toda la matriz.  
   - Retorna `True` si NO hay células vivas y `False` en caso contrario.

8. **`modificar_matriz(matriz)`**  
   - Permite al usuario agregar o eliminar células en posiciones concretas:  
     - Ingresar coordenadas `(i,j)`.  
     - Elegir “agregar” (si está vacía) o “eliminar” (si hay célula).  
     - Actualiza la matriz en tiempo real.

9. **Milagros (Funciones Especiales):**  
   - **`ejecutar_milagro_1(matriz)`**  
     1. Recorre la matriz en **espiral** comenzando desde `(0,0)` hacia el centro.  
     2. Cuenta cuántas celdas con `(x, y)` ambos impares (índices 1-based) están vacías.  
     3. Si ≥ 50% (parte entera) de esas celdas están libres, coloca una célula ángel (`A`) en la **primera** celda vacía del recorrido.  
   - **`ejecutar_milagro_2(matriz)`**  
     1. Recorre la **diagonal secundaria inferior** (de izquierda a derecha, desde la esquina inferior izquierda hacia arriba).  
     2. Cuenta las celdas cuya coordenada `x` (fila 1-based) es par.  
     3. Si ≥ 70% (parte entera) de esas celdas están libres, coloca una célula normal (`O`) en la **última** celda vacía del recorrido.  
   - **`ejecutar_milagro_3(matriz)`**  
     1. Recorrido en **zigzag vertical** (columna 0, de arriba a abajo; columna 1, de abajo a arriba; alternando).  
     2. Cuenta cuántas celdas con coordenada `y` (columna 1-based) impar están vacías.  
     3. Si ≥ 60% (parte entera) de esas celdas están libres, coloca `O` en la **primera** celda libre que se encuentre en la **segunda mitad** del recorrido completo.

---

## 🔤 Formato de Entrada y Salida

### Archivo de Entrada – `acaentra.txt`

```text
n,m
i1,j1
i2,j2
...
ik,jk
```

- **Línea 1:** `n,m` — número de filas (`n`) y columnas (`m`) de la matriz.  
  - Restricción: 10 ≤ n,m ≤ 30.  
- **Líneas 2…k:** Cada línea contiene coordenadas `i,j` (sin espacios) donde existe una célula viva inicialmente.  
  - Índices basados en 1 (la primera fila/columna es `1,1`).  
  - Solo se listan celdas vivas; las demás se consideran vacías.

### Ejemplo de `acaentra.txt`

```
10,10
1,1
1,2
2,1
5,5
7,8
```

### Archivo de Salida – `acasali.txt`

```text
i1,j1
i2,j2
...
```

- Cada línea es la coordenada `(i,j)` de una célula viva al finalizar la simulación.  
- Mismo formato que las líneas 2…k de entrada.

---

## ✨ Milagros Especiales

- **Milagro 1 – Espiral**  
  - Recuento de celdas con `(x, y)` impares libres.  
  - Si cumple el umbral (50% entero), nacerá una célula ángel en la **primera** celda vacía del espiral.

- **Milagro 2 – Diagonal Secundaria Inferior**  
  - Recuento de celdas con `x` par libres.  
  - Si cumple el umbral (70% entero), nacerá célula normal en la **última** celda vacía del recorrido diagonal.

- **Milagro 3 – Zigzag Vertical**  
  - Recuento de celdas con `y` impar libres.  
  - Si cumple el umbral (60% entero), nacerá célula normal en la **primera** celda libre de la **segunda mitad** del recorrido.

> **Importante:** El usuario puede elegir ejecutar cualquiera de estos milagros en cualquier momento, siempre y cuando haya al menos una celda vacía que cumpla la condición de nacimiento.

---

## 🧪 Recomendaciones de Prueba

1. **Matrices Pequeñas (5×5)**  
   - Permiten validar a ojo las posiciones de vecinos y los nacimientos.  
   - Ejemplo de patrones estáticos y osciladores sencillos.

2. **Verificar Reglas Base Sin Milagros**  
   - Crear configuraciones con:
     - Una célula aislada (muere por soledad).  
     - Bloques de 4 en cuadrado (sobrevive indefinidamente).  
     - Líneas de 3 (oscila).

3. **Probar Cada Milagro Individualmente**  
   - Diseñar una matriz donde las condiciones de porcentaje se cumplan justo en el límite.  
   - Verificar que la célula (`O` o `A`) nazca en la posición indicada (primera/última/segunda mitad).

4. **Extinción Anticipada**  
   - Ejecutar X generaciones donde X sea grande hasta que no queden células y verificar que el programa se detenga anticipadamente con el mensaje “No quedan células vivas. Simulación terminada en generación K.”

5. **Entrada Manual vs. Archivo**  
   - Cargar desde archivo y comparar con la versión ingresada manualmente (misma configuración).  
   - Verificar que ambas rutas produzcan idéntica matriz inicial.

---

## 🛠️ Cómo Contribuir

1. **Fork** este repositorio.  
2. Crear una **rama nueva** (`git checkout -b feature/nombre-funcionalidad`).  
3. Realizar cambios y documentar con comentarios claros.  
4. Hacer **commit** de los cambios (`git commit -m "Descripción breve del cambio"`).  
5. Hacer **push** a tu rama (`git push origin feature/nombre-funcionalidad`).  
6. Abrir un **Pull Request** para revisión.

Por favor, sigue la **guía de estilo**:
- Nombres de variables descriptivos (p. ej., `filas`, `columnas`, `matriz`).
- Funciones pequeñas y modulares.
- Comentarios claros explicando lógica compleja (p. ej., recorrido en espiral).
- Mantener el **PEP8** (espacios, sangrías, longitud de líneas ≤ 79 caracteres).
