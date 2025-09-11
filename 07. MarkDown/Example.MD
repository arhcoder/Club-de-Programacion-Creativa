
# Encabezado de Nivel 1 (Título Principal)
Los encabezados se usan para estructurar el documento. Se crean con el símbolo `#`. Cuantos más símbolos uses, menor será el nivel del encabezado.

## Encabezado de Nivel 2 (Subtítulo)
Este es un subtítulo, útil para las secciones principales de tu documento.

### Encabezado de Nivel 3
Para sub-secciones más específicas.

---

## Formato de Texto
Puedes dar formato al texto para enfatizar ciertas partes.

**Texto en negrita:** Se usa para dar fuerte énfasis. Se crea con dos asteriscos `**texto**` o dos guiones bajos `__texto__`.

*Texto en cursiva:* Se usa para un énfasis menor. Se crea con un asterisco `*texto*` o un guión bajo `_texto_`.

***Texto en negrita y cursiva:*** Para un énfasis máximo. Se crea con tres asteriscos `***texto***`.

~~Texto tachado:~~ Para indicar que algo ha sido eliminado o ya no es relevante. Se crea con dos virgulillas `~~texto~~`.

---

## Listas
Las listas son útiles para organizar información.

### Lista Desordenada
Se crea con asteriscos `*`, guiones `-` o signos de más `+`.
*   Elemento 1
*   Elemento 2
    *   Sub-elemento 2.1
    *   Sub-elemento 2.2

### Lista Ordenada
Se crea con números seguidos de un punto.
1.  Primer elemento
2.  Segundo elemento
3.  Tercer elemento

---

## Enlaces (Links)
Para redirigir a otras páginas web o archivos.
La sintaxis es `[Texto ancla](URL)`.

[Visita la página oficial de Markdown](https://www.markdownguide.org)

---

## Imágenes
Para mostrar imágenes en tu documento. La sintaxis es similar a los enlaces, pero con un signo de exclamación al principio.
`![Texto alternativo](URL de la imagen)`

![Logo de Markdown](https://markdown-here.com/img/icon256.png)

---

## Citas (Blockquotes)
Para resaltar texto o citar a alguien. Se crean con el símbolo `>`.

> "La simplicidad es la máxima sofisticación."
> - Leonardo da Vinci

---

## Código
Markdown permite mostrar código de dos maneras:

### Código en línea (Inline)
Para mencionar pequeñas piezas de código, como una función `printf()` o una variable `let x = 10;`. Se crea encerrando el código entre comillas invertidas `` ` ``.

### Bloque de Código
Para mostrar fragmentos de código más largos. Se crea encerrando el código entre tres comillas invertidas ` ``` `. También puedes especificar el lenguaje para obtener resaltado de sintaxis.

```javascript
function greet(name) {
  console.log("Hola, " + name + "!");
}

greet("Mundo");
```

```python
def add(a, b):
  return a + b

print(add(5, 3))
```

---

## Tablas
Para organizar datos en filas y columnas.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| :----------- | :----------: | -----------: |
| Columna 1    |  Columna 2   |    Columna 3 |
| Izquierda    |   Centrado   |      Derecha |
| `:-`         |    `:-:`     |         `-: `|

La línea con guiones `-` define la alineación de las columnas.

---

## Línea Horizontal
Para separar secciones de contenido. Se crea con tres o más guiones `---`, asteriscos `***` o guiones bajos `___`.

***

¡Y eso es todo! Con estos elementos puedes crear documentos de Markdown bien estructurados y legibles.
