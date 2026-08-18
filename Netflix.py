import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter

# MOTOR DE RECOMENDACION

# nos traemos los datos
data = pd.read_csv("netflix_titles.csv")

# eliminamos aquellas filas que todos los valores esten vacios
data_clear = data.dropna(how="all")

# creamos nuestra tabla de recomendaciones
data_recommend = data_clear[
    ["title", "listed_in", "description", "cast", "director", "country", "rating"]
]
# limpiamos aquellas que tengan nan
data_recommend["cast"] = data_recommend["cast"].fillna("")
data_recommend["director"] = data_recommend["cast"].fillna("")
data_recommend["country"] = data_recommend["country"].fillna("")
data_recommend["rating"] = data_recommend["rating"].fillna("")


# unimos los elementos que queremos que luego analice
join = (
    data_recommend["listed_in"]
    + " "
    + data_recommend["description"]
    + " "
    + data_recommend["cast"]
)


# inizializamos el TfidfVectorizer
vectorizer = TfidfVectorizer()

# le pasamos nuestro join
tfidif_matrix = vectorizer.fit_transform(join)

# vemos el vocabulario que ha extraido
# print(vectorizer.get_feature_names_out())

# calculamos el coseno para que nos indique cual tiene la similitudes mas altas
similarity = cosine_similarity(tfidif_matrix)


# PARTE VISUAL

# creamos el objeto
screen = tkinter.Tk()

# creamos el titulo de la ventana
screen.title("Netflix Recommendation System")

# definir el ancho y alto
screen.geometry("900x650")

# ponemos el fondo de la pantalla oscuro
screen.configure(bg="#141414")

# no puedo cambiar el tamaño
screen.resizable(False, False)


# creamos el titulo
title1 = tkinter.Label(
    screen,
    text="NETFLIX",
    bg="#141414",
    fg="#E50914",
    font=("Arial", 34, "bold"),
)

# colocamos el titulo
title1.pack(pady=(40, 10))


# creamos un subtitulo para indicar al usuario lo que tiene que hacer
subtitle = tkinter.Label(
    screen,
    text="¿Qué película o serie te ha gustado?",
    bg="#141414",
    fg="white",
    font=("Arial", 18),
)

# colocamos el subtitulo
subtitle.pack(pady=10)


# creamos el espacio para ingresar la pelicula
enter = tkinter.Entry(
    screen,
    width=45,
    font=("Arial", 16),
    justify="center",
)

# colocamos el espacio para ingresar la pelicula
enter.pack(pady=20)


# creamos la funcion para que funcione el boton
def action_button():

    # nos traemos la pelicula que ha escrito el usuario
    film = enter.get()

    # lo convertimos todo a minusculas y quitamos espacios
    film = film.lower().strip()

    if film == "":
        result.delete("1.0", "end")
        result.insert("end", "Porfavor ingresa una pelicula")
        return

    # comprobamos si la pelicula esta dentro de nuestra base de peliculas y la ponemos en minnuscula
    if film in data_recommend["title"].str.lower().values:

        # buscamos el indice donde este la pelicula
        index_movie = data_recommend[data_recommend["title"].str.lower() == film].index[
            0
        ]

        # buscamos la similitud que tiene esa pelicula con el resto
        movie_similary = similarity[index_movie]

        # creamos una lista vacia para guardar las peliculas similares
        film_similary = []

        # recorremos posicion y similitud
        for position, similarity_film in enumerate(movie_similary):

            # si es distinta a la de la propia pelicula
            if similarity_film != 1:

                # las añadimos todas a una lista que contendra posicion y similitud
                film_similary.append((position, similarity_film))

        # ordenamos la similitud de mayor a menor
        film_similary.sort(key=lambda x: x[1], reverse=True)

        # convertimos el numero en lista
        titles = data_recommend["title"].tolist()

        # limpiamos los resultados anteriores antes de mostrar los nuevos
        result.delete("1.0", "end")

        # recorremos la lista y sacamos los 10 primeros titulos
        for numero, (position, similarity_film) in enumerate(
            film_similary[:10], start=1
        ):

            # sacamos el porcentaje de las recomendaciones
            porcent = int(similarity_film * 100)

            # mostramos cada titulo en la pantalla y hacemos un salto de linea
            result.insert(
                "end",
                str(numero)
                + "."
                + titles[position]
                + " - similitud: "
                + str(porcent)
                + "%\n",
            )

    else:
        result.delete("1.0", "end")  # borramos lo anterior
        result.insert("end", "Pelicula no encontrada")


# creamos el boton
button = tkinter.Button(
    screen,
    text="RECOMENDAR",
    font=("Arial", 14, "bold"),
    bg="#E50914",
    fg="white",
    activebackground="#B20710",
    activeforeground="white",
    width=20,
    command=action_button,
)

# colocamos el boton
button.pack(pady=20)


# creamos el titulo para los resultados
recommend_title = tkinter.Label(
    screen,
    text="Recomendaciones para ti",
    bg="#141414",
    fg="white",
    font=("Arial", 16, "bold"),
)

# colocamos el titulo de los resultados
recommend_title.pack(pady=(15, 5))


# creamos el espacio para los resultados
result = tkinter.Text(
    screen,
    width=55,
    height=11,
    font=("Arial", 14),
    bg="#222222",
    fg="white",
    bd=0,
    padx=15,
    pady=15,
)

# colocamos el espacio para los resultados
result.pack(pady=10)


# mantenemos la ventana abierta
screen.mainloop()
