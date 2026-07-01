# PÁGINA WEB DE TWENTY ONE PILOTS CON STREAMLIT
# ============================================================================

#En primer lugar, debemos importar las librerías necesarias para la página web.
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import folium
import streamlit.components.v1 as components
import random
import re

#Luego, debemos cargar los datos desde el archivo Excel donde hice mi base de datos para poder mostrarlos en la página y que puedan ser leídos para el resto de la página.
df_discografia = pd.read_excel("mi_base_de_datos.xlsx")


#Ahora iniciamos a configurar la página con el título, el icono y el diseño ancho.
st.set_page_config(
    page_title="Twenty One Pilots | Discografía",
    page_icon="🎵",
    layout="wide"
)

#Luego establecemos el título y el ícono de la página en la pestaña del navegador. Luego, debemos volver a configurar la página para asegurar que los valores sean consistentes.
st.set_page_config(
    page_title="Twenty One Pilots | Discografía",  #Título de la pestaña
    page_icon="🎵",  #Ícono de la pestaña
    layout="wide"  #Diseño de página ancha (más espacio)
)

# ============================================================================
# APLICAR ESTILOS PERSONALIZADOS (Fondo de pantalla y estilos para el texto)
# ============================================================================

#En este apartado, principalmente creé estilos para que, en cada apartado de la página, solo utilice la variable asociada al estilo: h1, 2, 3, etc. 
#Esto permite que, si quiero cambiar el color de todos los títulos, solo tenga que cambiarlo en un lugar y no en cada título de la página. 
#Además, también agregué un fondo de pantalla para toda la página y un estilo para que el texto se lea mejor.
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css?family=Material+Icons');
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0&display=swap');

    /* Aplicar la fuente a toda la aplicación */
    html, body, [class*="st-"] {
        font-family: 'Jost', sans-serif;
    }

    /* Asegurar que los íconos de Streamlit usen las fuentes de Material Icons/Symbols */
    .material-icons,
    .material-icons-outlined,
    .material-icons-round,
    .material-icons-sharp,
    .material-icons-two-tone,
    .material-symbols-outlined {
        font-family: 'Material Icons', 'Material Symbols Outlined' !important;
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 48;
    }

    /* Corregir el botón de contraer/expandir la barra lateral */
    [data-testid="collapsedControl"] span,
    [data-testid="collapsedControl"] i,
    [data-testid="collapsedControl"] div {
        font-family: 'Material Icons', 'Material Symbols Outlined' !important;
    }

    /* Cambiar el fondo de la aplicación */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.ibb.co/Ndj2fxhx/Fondex-4.jpg");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Agregar transparencia al contenido principal para que se lea bien */
    .main {
        background-color: rgba(0, 0, 0, 0.8);
    }
    
    /* Estilo para los títulos */
    h1 {
        color: #DD2A2A !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }
    
    /* Estilo para los subtítulos */
    h2, h3 {
        color: #5DADE2 !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }

    /* Estilo para otros textos */
    h4 {
        color: #CEFF4A !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }

    /* Estilo para otros textos */
    h5 {
        color: #EE88AF !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }
    
    /* Estilo para el texto general */
    p {
        color: #000000 !important;
    }

    /* Estilo para el texto general */
    p {
        color: #000000 !important; text-shadow: 3px 3px 6px rgba(0,0,0,0.6); 

    }

    </style>
    """,
    unsafe_allow_html=True  #Este código es para permitir que streamlit interprete el código HTML/CSS
)

# ============================================================================
# SEGUNDO: MENÚ DE NAVEGACIÓN EN LA BARRA LATERAL
# ============================================================================

#En primer lugar, utilizamos la función st.sidebar para crear una barra lateral donde colocaremos el menú de navegación principal.
with st.sidebar:
    #Luego, utilizamos option_menu para crear un menú interactivo que permita al usuario seleccionar entre diferentes páginas.
    pagina_seleccionada = option_menu(
        menu_title="🎵 MENÚ PRINCIPAL",  #Título que se mostrará en la parte superior del menú.
        options=['🏠 Inicio', '💿 Discografía', '📖 Lore', '🗺️ Mapa', '❓ ¿Qué tanto conoces a TOP? |-/', '📊 Estadísticas'],  #Opciones disponibles que el usuario puede seleccionar.
        icons=['house', 'music-note-list', 'book', 'map', 'question-circle', 'graph-up'],  #Iconos de cada opción para una mejor visualización y estética.
        menu_icon="mic",  #Ícono principal del menú que representa la aplicación.
        default_index=0  #La opción seleccionada por defecto (0 = Inicio) cuando la página se carga
    )
    #Finalmente, todo este apartado lo almacenamos en la variable 'pagina_seleccionada' para usarlo en toda la página y mostrar el contenido correspondiente según la opción seleccionada por el usuario.

# ============================================================================
# TERCERO: PÁGINA 1: INICIO (Presentación de la banda)
# ============================================================================

if pagina_seleccionada == '🏠 Inicio':
    #En primer lugar, utilizamos el comando st.markdown para que podamos mostrar el título principal de la página con un estilo visual más llamativo, utilizando uno de los estilos que creé al inicio.
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>TWENTY ONE PILOTS</h1>",
        unsafe_allow_html=True
    )
    
    #Luego, insertamos el logo oficial de la banda para mejorar la estética de la página y que el usuario pueda identificarla visualmente de manera inmediata a través de el comando st.markdown y un código HTML que permite centrar la imagen y darle un tamaño adecuado.
    st.markdown(
        "<div style='display: flex; justify-content: center; margin: 20px 0;'>"
        "<img src='https://logos-world.net/wp-content/uploads/2024/12/21-Pilots-Logo-2011.png' "
        "alt='Twenty One Pilots Logo' style='width: 280px; border-radius: 8px;'>"
        "</div>",
        unsafe_allow_html=True
    )
    
    #Después, creamos dos columnas para ordenar el contenido de forma más clara y de paso dar algo de información de la banda antes de continuar.
    col1, col2 = st.columns(2)
    
    #-COLUMNA 1: INFORMACIÓN GENERAL-
    with col1:
        #En este apartado, organizamos la información general de la banda dentro de la primera columna para que el usuario pueda conocerla de forma ordenada. Además, utilizamos el comando st.markdown para que podamos mostrar el título de la sección de información general con un estilo visual más llamativo, utilizando otro de los estilos que creé al inicio.
        st.markdown("<h3 style='color: #8D0000;'>ℹ️ Acerca de la Banda</h3>", unsafe_allow_html=True)
        
        #Posteriormente, presentamos el texto introductorio de la banda para que el usuario comprenda su origen y su trayectoria de manera sencilla a través del comando st.markdown y un código HTML que nos permite justificar el texto, darle un tamaño adecuado y un color que contraste con el fondo de la página.
        st.markdown("""
                    <div style='text-align: justify; font-size: 16px; color: black'>
                    <b>Twenty One Pilots</b> es una banda estadounidense de música alternativa formada en 2009 en Columbus, Ohio.
        
                    La banda está integrada por:
                    <ol>
                    <li>- <b>Tyler Joseph</b>: Vocalista y productor</li>
                    <li>- <b>Josh Dun</b>: Baterista</li>
                    </ol>
        
                    La banda se ha consolidado como un fenómeno global gracias a su sonido ecléctico que fusiona elementos de rock alternativo, pop, hip-hop, electrónica y reggae, además de destacar por la profunda carga emocional e introspectiva de sus letras, las cuales abordan temas como la salud mental, la fe y la inseguridad. Con álbumes conceptuales multiplatino como Blurryface (2015) —que hizo historia al lograr que todas sus canciones recibieran al menos la certificación de oro— y una estética visual y narrativa inconfundible, el grupo ha roto récords en la industria musical y se ha ganado una base de fanáticos devotos gracias a sus enérgicos e impredecibles conciertos en vivo.
        
                    </div>
                    
        """, unsafe_allow_html=True)
        
    
    #-COLUMNA 2: DATOS INTERESANTES-
    with col2:
        # Ahora, añadimos una segunda columna con datos destacados para que completemos la presentación con información adicional relevante. Nuevamente utilizamos el comando st.markdown para que podamos mostrar el título de la sección de datos interesantes con un estilo visual más llamativo, utilizando otro de los estilos que creé al inicio.
        st.markdown("<h3 style='color: #8D0000;'>🎸 Datos Interesantes</h3>", unsafe_allow_html=True)
        
        #Después, mostramos información complementaria sobre premios, álbumes y género para que el usuario obtenga una visión más completa de la banda.
        st.markdown("""
                    <div style='text-align: justify; font-size: 16px; color: black'>
                    <b>Premios y Reconocimientos:</b>
                    <ol>
                    - Grammy Awards
                    </ol>
                    <ol>
                    - MTV Video Music Awards
                    </ol>
                    <ol>
                    - American Music Awards
                    </ol>

                    <b>Álbumes Principales:</b>
                    - Twenty One Pilots (2009)
                    - Regional at Best (2011) (actualmente inexistente)
                    - Vessel (2013)
                    - Blurryface (2015)
                    - Trench (2018)
                    - Scaled and Icy (2021)
                    - Clancy (2024)
                    - Breach (2025)

                    <b>Género Musical:</b>
                    Alternative Hip-Hop / Electropop / Rock
        
                    </div>
                    
        """, unsafe_allow_html=True)

    
    #Después, incorporamos un separador visual para que la transición entre secciones se perciba de forma más limpia a traves del comando st.markdown y un código que nos permite crear una línea horizontal.
    st.markdown("---")
    
    #Luego, utilizamos el comando st.markdown para que podamos mostrar el título de la sección de videos destacados y le asignamos el estilo correspondiente.
    st.markdown("<h3 style='text-align: center; color: #8D0000;'>🎬 Videos Destacados</h3>", unsafe_allow_html=True)
    
    #Posteriormente, consultamos la base de datos para que podamos obtener los enlaces de los videos disponibles y los almacenamos en la variable 'videos_disponibles' para que podamos utilizarlos más adelante.
    videos_disponibles = df_discografia[df_discografia['Link_mv'].notna()]['Link_mv'].dropna().unique().tolist()
    
    if len(videos_disponibles) >= 2:
        #Después, seleccionamos dos videos de forma aleatoria para que la página presente contenido variado cada vez que se recargue la sección. 
        #Esto lo hacemos utilizando la función random.sample para que podamos obtener dos videos distintos de la lista de videos disponibles y los almacenamos en la variable 'videos_seleccionados'.
        videos_seleccionados = random.sample(list(videos_disponibles), min(2, len(videos_disponibles)))
        
        #En seguida, creamos dos columnas para que podamos mostrar ambos videos de manera equilibrada.
        video_col1, video_col2 = st.columns(2)
        
        with video_col1:
            #Luego, insertamos el primer video en la columna correspondiente para que el usuario lo pueda reproducir de inmediato a través del comando st.video y le pasamos el enlace del primer video seleccionado.
            st.video(videos_seleccionados[0])  #Video de YouTube
        
        with video_col2:
            if len(videos_seleccionados) > 1:
                #Por último, añadimos el segundo video en la segunda columna para completar la vista de contenido destacado. Nuevamente utilizamos el comando st.video y le pasamos el enlace del segundo video seleccionado.
                st.video(videos_seleccionados[1])  #Video de YouTube

# ============================================================================
# CUARTO: PÁGINA 2: DISCOGRAFÍA (Álbumes y canciones)
# ============================================================================

elif pagina_seleccionada == '💿 Discografía': 
    #En primer lugar, utilizamos este bloque para mostrar el título principal de la sección y presentar una breve introducción sobre la discografía.
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>|-/ DISCOGRAFÍA DE TWENTY ONE PILOTS</h1>",
        unsafe_allow_html=True
    )
    
    #Ahora, utilizamos este mensaje para contextualizar al usuario y explicarle que podrá explorar los álbumes, canciones y detalles de cada una de ellas con el comando st.markdown.
    st.markdown(
        "<p style='text-align: center; color: #000000; font-weight: bold; font-size: 1.1em;'>Aquí puedes explorar todos los álbumes y canciones de Twenty One Pilots, ver detalles de cada canción y conocer el mensaje detrás de cada una de ellas.</p>",
        unsafe_allow_html=True
    )
    
    #Luego, añadimos un separador para que la sección se vea más ordenada y clara.
    st.markdown("---")

    #Posteriormente, aplicamos un estilo a los botones para que la discografía se vea más limpia y consistente con el diseño general de la página a través del comando st.markdown y un código CSS que nos permite personalizar el color de fondo, el color del texto, el borde y el efecto al pasar el cursor sobre los botones interactivos.
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
            box-shadow: none !important;
        }
        div.stButton > button:hover {
            background-color: #f0f0f0 !important;
        }
        div.stButton > button:focus-visible {
            outline: 2px solid #000000 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    #Luego, determinamos si la base de datos cuenta con una columna de portadas para que podamos mostrar imágenes de los álbumes cuando estén disponibles y almacenamos el nombre de la columna en la variable 'portada_col'.
    portada_col = 'Link_portada' if 'Link_portada' in df_discografia.columns else None
    albumes = df_discografia['Álbum'].dropna().unique()

    #Ahora empezamos con lo bueno, definimos esta función para que podamos identificar columnas que no necesitamos mostrar en los filtros o en el procesamiento adicional. Esto a través de la normalización del nombre de la columna y la verificación contra una lista de nombres excluidos.
    def columna_excluida(col):
        nombre = col.lower().replace(' ', '').replace('_', '')
        return nombre in ['latitudvideo', 'longitudvideo', 'latitud', 'longitud', 'amplitud']

    #Posteriormente, creamos otra función para que podamos obtener el nombre de una canción de forma más sencilla, incluso si el DataFrame usa distintos nombres de columna. 
    #Luego de eso, verificamos si el índice de la fila contiene un valor que pueda ser considerado como nombre de canción y lo devolvemos si es válido. Si no se encuentra ningún nombre válido, devolvemos una cadena vacía.
    #Esto realmente es innecesario, principalmente porque la columna tiene ya el nombre de las canciones. Sin embargo, decidí ponerlo así en caso alguien en el futuro decida usar el código u otra base de datos que no tenga la columna de canciones con el nombre exacto.
    def obtener_nombre_cancion(fila):
        candidatos = [
            'TÍTULO', 'Título', 'TITULO', 'Canción', 'Cancion', 'Nombre', 'Nombre de canción', 'Nombre de cancion',
            'Titulo', 'Título', 'Title', 'title', 'track', 'Track',
            'track_name', 'Track Name', 'Song', 'song'
        ]
        for c in candidatos: #Aquí, recorremos la lista de candidatos para que podamos verificar si alguna de las columnas coincide con los nombres que podrían representar el título de la canción.
            if c in fila.index:
                val = fila.get(c)
                if pd.notna(val) and str(val).strip() != '':
                    return str(val).strip()
        for col in fila.index:
            col_low = col.lower()
            if any(k in col_low for k in ['nombre', 'titulo', 'title', 'track', 'song']): #Aquí verificamos si el nombre de la columna contiene palabras clave que podrían indicar que es el título de la canción.
                val = fila.get(col)
                if pd.notna(val) and str(val).strip() != '':
                    return str(val).strip()
        try:
            idx = fila.name
            if pd.notna(idx) and str(idx).strip() != '':
                idx_str = str(idx).strip()
                if not idx_str.isnumeric():
                    return idx_str
        except Exception:
            pass
        return ''

    #Ahora, utilizamos esta función para que podamos recuperar valores de una fila sin importar el nombre exacto de la columna. 
    #Para ello, recorremos una lista de nombres de columna candidatos y devolvemos el primer valor no nulo que encontremos. Si no se encuentra ningún valor válido, devolvemos None.
    def buscar_valor(fila, candidatos):
        for c in candidatos:
            if c in fila.index:
                val = fila.get(c)
                if pd.notna(val) and str(val).strip() != '':
                    return val
        return None

    #Luego, definimos esta función para que podamos obtener la portada de un álbum a partir de la coincidencia del nombre del álbum en la base de datos. 
    #Además, normalizamos el nombre del álbum para evitar problemas de mayúsculas, minúsculas o espacios en blanco. Si encontramos coincidencias, devolvemos el primer valor de portada disponible; si no, devolvemos None.
    def obtener_portada_por_album(album):
        if not isinstance(album, str) or not album.strip():
            return None
        album_norm = album.strip().lower()

        if 'Link_portada' in df_discografia.columns:
            coincidencias = df_discografia[df_discografia['Álbum'].astype(str).str.strip().str.lower() == album_norm]
            if not coincidencias.empty:
                valores_portada = coincidencias['Link_portada'].dropna().unique()
                if len(valores_portada) > 0:
                    return valores_portada[0] 

    #Posteriormente, inicializamos estas variables de sesión para que podamos recordar si el usuario ha abierto un detalle de canción o un álbum específico.
    if 'song_detalle' not in st.session_state: #Este código es para que, si el usuario ha abierto un detalle de canción, podamos recordar esa acción y mostrar la vista correspondiente en lugar de la lista general de álbumes y canciones.
        st.session_state['song_detalle'] = None
    if 'album_abierto' not in st.session_state: #Este otro código es para que, si el usuario ha abierto un álbum específico, podamos recordar esa acción y mostrar la lista de canciones correspondientes en lugar de la lista general de álbumes.
        st.session_state['album_abierto'] = None

    #Luego, verificamos si el usuario ha seleccionado ver los detalles de una canción para que podamos mostrar esa vista en lugar de la lista general.
    if st.session_state.get('song_detalle'): #Si el usuario ha seleccionado ver los detalles de una canción, mostramos la información detallada de esa canción en lugar de la lista general de álbumes y canciones.
        fila_det = pd.Series(st.session_state['song_detalle']['fila']) 
        nombre_det = obtener_nombre_cancion(fila_det) or 'Título desconocido'
        st.markdown(f"<h2 style='color: #8D0000;'>Detalles de la canción: {nombre_det}</h2>", unsafe_allow_html=True)
        col_img, col_info = st.columns([1, 2])
        with col_img: #Aquí, mostramos la portada de la canción si está disponible en la base de datos. Si no, intentamos obtener la portada del álbum correspondiente. Además, mostramos la fotografía del lugar si está disponible y el enlace al videoclip si existe. Esto lo logramos utilizando la función buscar_valor para obtener los valores de las columnas correspondientes y luego mostramos las imágenes y enlaces utilizando st.image y st.markdown.
            link_portada = buscar_valor(fila_det, ['Link_portada'])
            if not link_portada:
                album_actual = st.session_state.get('song_detalle', {}).get('album', '')
                link_portada = obtener_portada_por_album(album_actual)
            if link_portada:
                st.image(link_portada, width=320)
            foto_lugar = buscar_valor(fila_det, ['Fotografía_lugar', 'Fotografia_lugar', 'Fotografía Lugar', 'Fotografia Lugar'])
            if foto_lugar:
                st.image(foto_lugar, width=320)
                link_mv = buscar_valor(fila_det, ['Link_mv', 'Link MV', 'Link_MV', 'Linkmv'])
                if link_mv:
                    st.markdown(f"<p style='color: #000000; margin-top: 10px;'><strong>Videoclip:</strong> <a href='{link_mv}' target='_blank'>{link_mv}</a></p>", unsafe_allow_html=True)
        with col_info: #Aquí, mostramos la información detallada de la canción, incluyendo el año de lanzamiento, las reproducciones en Spotify, el género, la duración, el enlace a las letras y cualquier mensaje adicional. Utilizamos la función buscar_valor para obtener los valores de las columnas correspondientes y luego mostramos la información utilizando st.markdown.
            #Luego, generamos las variables para mostrar la información detallada de la canción, incluyendo el año de lanzamiento, las reproducciones en Spotify, el género, la duración, el enlace a las letras y cualquier mensaje adicional.
            año = buscar_valor(fila_det, ['Año', 'Year'])
            if año:
                st.markdown(f"<p style='color: #000000;'><strong>Año:</strong> {año}</p>", unsafe_allow_html=True)
            reproducciones = buscar_valor(fila_det, ['Reproducciones en Spotify', 'Reproducciones Spotify', 'Reproducciones', 'Plays'])
            if reproducciones:
                st.markdown(f"<p style='color: #000000;'><strong>Reproducciones en Spotify:</strong> {reproducciones}</p>", unsafe_allow_html=True)
            genero = buscar_valor(fila_det, ['Género', 'Genero'])
            if genero:
                st.markdown(f"<p style='color: #000000;'><strong>Género:</strong> {genero}</p>", unsafe_allow_html=True)
            duracion = buscar_valor(fila_det, ['Duración', 'Duracion', 'Duration'])
            if duracion:
                st.markdown(f"<p style='color: #000000;'><strong>Duración:</strong> {duracion}</p>", unsafe_allow_html=True)
            link_letras = buscar_valor(fila_det, ['Link_letras', 'Link_letra', 'Link_Letras', 'Letra'])
            if link_letras:
                st.markdown(f"<p style='color: #000000;'><strong>Link letras:</strong> <a href='{link_letras}' target='_blank'>{link_letras}</a></p>", unsafe_allow_html=True)
            mensaje = buscar_valor(fila_det, ['Mensaje', 'mensaje', 'Comentario', 'commentario'])
            if mensaje:
                st.markdown(f"<p style='color: #000000;'><strong>Mensaje:</strong> {mensaje}</p>", unsafe_allow_html=True)
        if st.button('Volver a la discografía', key='volver_detalle'):
            st.session_state['song_detalle'] = None
        st.markdown('---')
        st.stop() 

    #Luego, recorremos cada álbum para que podamos mostrar su portada, información general y la lista de canciones asociadas. Esto lo hacemos utilizando un bucle for que recorre la lista de álbumes y, para cada álbum, filtramos las canciones correspondientes en el DataFrame. 
    #Si el álbum tiene canciones, mostramos la portada (si está disponible), el total de canciones, el año del álbum y el género. Además, añadimos un botón para que el usuario pueda ver las canciones del álbum y, si lo hace, mostramos la lista de canciones con sus detalles.
    for idx, album in enumerate(albumes):
        canciones_del_album = df_discografia[df_discografia['Álbum'] == album]
        if canciones_del_album.empty:
            continue

        foto_album = None #Aquí, inicializamos la variable 'foto_album' como None para que podamos almacenar la portada del álbum si está disponible. Luego, verificamos si la columna de portadas existe y si contiene valores no nulos para el álbum actual. Si encontramos una portada válida, la asignamos a 'foto_album'.
        if portada_col and portada_col in canciones_del_album.columns:
            valores_foto = canciones_del_album[portada_col].dropna().unique()
            if len(valores_foto) > 0:
                foto_album = valores_foto[0]

        st.markdown(
            f"<h2 style='color: #8D0000; border-bottom: 2px solid #FFD700; padding-top: 15px;'>💿 {album}</h2>", 
            unsafe_allow_html=True #Luego, mostramos el título del álbum con un estilo visual más llamativo y una línea decorativa debajo del título para separar visualmente cada álbum en la lista.
        )
        album_col1, album_col2 = st.columns([1, 2]) #Ahora, creamos dos columnas para mostrar la portada del álbum y la información general de manera equilibrada. La primera columna tendrá un ancho relativo de 1 y la segunda columna tendrá un ancho relativo de 2.
        with album_col1: #En la primera columna, mostramos la portada del álbum si está disponible. Si no hay una portada disponible, mostramos un mensaje indicando que no hay imagen de portada. Esto lo hacemos utilizando st.image para mostrar la imagen y st.markdown para mostrar el mensaje.
            if foto_album:
                st.image(foto_album, caption=f"Portada de {album}", width=400)
            else:
                st.markdown(
                    "<div style='padding: 40px; background: rgba(255,255,255,0.08); border-radius: 12px; text-align: center;'>"
                    "<p style='color:#000000; margin: 0;'>Sin imagen de portada disponible.</p>"
                    "</div>", unsafe_allow_html=True
                )
            abrir_album_key = f"abrir_album_{idx}"
            if st.button(f"Ver canciones de {album}", key=abrir_album_key):
                if st.session_state.get('album_abierto') == album:
                    st.session_state['album_abierto'] = None
                else:
                    st.session_state['album_abierto'] = album
        with album_col2: #En la segunda columna, mostramos información general del álbum, incluyendo el total de canciones, el año del álbum y el género. Esto lo hacemos utilizando st.markdown para mostrar la información con un estilo visual más llamativo.
            st.markdown(
                f"<p style='color: #000000; font-size: 16px;'><strong>Total de canciones:</strong> {len(canciones_del_album)}</p>",
                unsafe_allow_html=True
            )
            año_album = buscar_valor(canciones_del_album.iloc[0], ['Año', 'Year'])
            if año_album:
                st.markdown(f"<p style='color: #000000;'><strong>Año del álbum:</strong> {año_album}</p>", unsafe_allow_html=True)
            genero_album = buscar_valor(canciones_del_album.iloc[0], ['Género', 'Genero'])
            if genero_album:
                st.markdown(f"<p style='color: #000000;'><strong>Género:</strong> {genero_album}</p>", unsafe_allow_html=True)

        #Por otro lado, comprobamos si el álbum está abierto para que podamos mostrar las canciones correspondientes debajo de su información general. 
        if st.session_state.get('album_abierto') == album: #Así, si el usuario ha abierto un álbum específico, mostramos la lista de canciones asociadas a ese álbum. Para cada canción, mostramos su título, mensaje (si está disponible), portada del álbum (si está disponible) y un botón para ver los detalles de la canción. Esto lo hacemos utilizando un bucle for que recorre las canciones del álbum y st.markdown para mostrar la información con un estilo visual más llamativo.
            st.markdown(
                f"<h3 style='color: #8D0000;'>🎵 Canciones en {album}</h3>",
                unsafe_allow_html=True
            )
            for song_idx, fila in canciones_del_album.iterrows(): #Aquí, recorremos cada canción del álbum para mostrar su información detallada. Para cada canción, obtenemos el nombre de la canción, el enlace a la portada (si está disponible), el enlace a las letras (si está disponible) y cualquier mensaje adicional. Luego, construimos un bloque HTML que contiene esta información y lo mostramos utilizando st.markdown. Además, añadimos el botón para que el usuario pueda ver los detalles de la canción.
                nombre_cancion = obtener_nombre_cancion(fila) or 'Título desconocido'
                link_portada = buscar_valor(fila, ['Link_portada'])
                link_letras = buscar_valor(fila, ['Link_letras', 'Link_letra', 'Link_Letras', 'Letra'])
                mensaje = buscar_valor(fila, ['Mensaje', 'mensaje', 'Comentario', 'commentario'])

                card_html = (
                    "<div style='display:flex; align-items:flex-start; gap:18px; margin-bottom: 16px; padding: 16px; border-radius: 16px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.14);'>"
                    "<div style='flex:1; min-width: 0;'>"
                    f"<h4 style='color: #8D0000; margin: 0 0 8px 0;'>🎶 {nombre_cancion}</h4>"
                    f"<p style='color: #000000; margin: 0 0 8px 0; line-height: 1.5;'>" + (f"{mensaje}" if mensaje else "") + "</p>"
                    "</div>"
                ) 
                if foto_album:
                    card_html += (
                        "<div style='width: 180px; min-width: 180px;'>"
                        f"<img src='{foto_album}' alt='Portada del álbum' style='width:100%; border-radius: 14px; object-fit: cover;'>"
                        "</div>"
                    )
                card_html += "</div>"

                st.markdown(card_html, unsafe_allow_html=True)
                detalle_key = f"detalle_cancion_{idx}_{song_idx}"
                if st.button('Ver detalles', key=detalle_key):
                    st.session_state['song_detalle'] = {'album': album, 'fila': fila.to_dict()}
            st.markdown('---') #Añadimos un separador visual para que la transición entre secciones se perciba mejor.

    #Posteriormente, mostramos estas métricas para que el usuario pueda ver de forma rápida el resumen general de la discografía. Esto lo hacemos utilizando el comando st.markdown para mostrar el título de la sección de estadísticas generales.
    #Luego, creamos tres columnas para distribuir la información de manera equilibrada y más legible. 
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    
    with stat_col1: 
        #En esta columna, contamos los álbumes para que el usuario vea cuántos discos están disponibles en la sección con el comando len() y lo almacenamos en la variable 'total_albumes'. Luego, mostramos esta métrica utilizando st.metric para que el usuario pueda ver de forma rápida el total de álbumes disponibles.
        total_albumes = len(albumes)
        st.metric(
            label="Total de Álbumes",  # Etiqueta
            value=total_albumes  # Valor a mostrar
        )
    
    with stat_col2:
        #Luego, contamos las canciones para que podamos mostrar el total de entradas disponibles en la discografía.
        total_canciones = len(df_discografia)
        st.metric(
            label="Total de Canciones",
            value=total_canciones
        )
    
    with stat_col3:
        #Finalmente, calculamos los géneros únicos para que el usuario pueda identificar la diversidad musical presente en los datos.
        if 'Género' in df_discografia.columns:
            total_generos = df_discografia['Género'].nunique()
            # .nunique() cuenta valores únicos
            st.metric(
                label="Géneros Musicales",
                value=total_generos
            )

    #Por último, cerramos este contenedor para que el diseño de la sección quede correctamente estructurado.
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================================
# QUINTO: PÁGINA 3: LORE
# ============================================================================

elif pagina_seleccionada == '📖 Lore':
    #En primer lugar, preparamos el encabezado principal de esta sección antes de construir el contenido. Por ello, utilizamos el comando st.markdown para mostrar el título de la sección con un estilo similar al resto de secciones.
    pass
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>GUÍA SOBRE PERSONAJES Y CIUDADES DE LA HISTORIA QUE NECESITAN SABER PARA ENTENDER</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: #000000; font-weight: bold; font-size: 1.1em;'>Esto al principio puede ser un poco confuso y no es necesario aprendérselo ahora, pero cada vez que se pierdan con respecto a algún personaje, vuelvan a acá para aclarar quién es. Cabe aclarar que estas descripciones se van modificando y completando a medida que salen más detalles sobre los personajes.</p>",
        unsafe_allow_html=True
    )
    #Posteriormente, creamos dos columnas para organizar la información de personajes y lugares en paralelo.
    col1, col2 = st.columns(2)
    
    #-COLUMNA 1: INFORMACIÓN GENERAL-
    with col1:
        st.markdown("<h2 style='color: #8D0000;'>PERSONAJES</h2>", unsafe_allow_html=True)
        
        #Aquí agregamos textos de presentación con imágenes a la derecha.
        personajes = [
            {
                "nombre": "Blurryface",
                "descripcion": "es el líder de los 9 obispos, pero a la vez es uno de ellos, es como el obispo Nico decide llamarse a él mismo. Es el que mayor poder tiene. Apareció en el 2015 representando los miedos e inseguridades de Tyler. Se presenta en las canciones con una voz grave y el color que lo distingue es el rojo.",
                "imagen": "https://i.pinimg.com/736x/30/fe/26/30fe262ff9c2e7874aabc66642d74ffd.jpg"
            },
            {
                "nombre": "Nico and the niners (obispos)",
                "descripcion": "los obispos controlan dema y predican la palabra del vialismo. Su autoridad proviene de dos cosas: un poder milagroso y una religión secuestrada, uno alimenta al otro formando un ciclo. El color que los representa es el rojo y no pueden ver el color amarillo.",
                "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaTHNcTCUusNTeVuTf3WBNJfNfrfQe2f2S_Q&s"
            },
            {
                "nombre": "Nico",
                "descripcion": "Nico es uno de los 9 obispos que hay en dema, pero a la vez tiene control sobre los otros 9 obispos, lo que significa que si bien él es una persona con poder que está por arriba de los 9 obispos al mismo tiempo es parte de ellos. También es blurryface, pero esto lo explico a detalle más adelante.",
                "imagen": "https://static.wikia.nocookie.net/twenty-one-pilots/images/c/c4/Nico-Blurryface.png/revision/latest/scale-to-width-down/1200?cb=20250305220952"
            },
            {
                "nombre": "Tyler",
                "descripcion": "simboliza un personaje que está todo el tiempo entrando y saliendo de Dema, el cual representa la lucha sobre querer salir de esa ciudad.",
                "imagen": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tyler_Joseph_on_Clancy_Tour_%28cropped%29.jpg"
            },
            {
                "nombre": "Josh",
                "descripcion": "es el lider de los banditos. Intenta sacar a Tyler y otras personas de dema.",
                "imagen": "https://i.pinimg.com/736x/bd/2f/f8/bd2ff80d4bba3db7a59249000b4bdb62.jpg"
            },
            {
                "nombre": "Banditos",
                "descripcion": "viven en Trench y son la rebelion. Ellos quieren terminar con el sistema que imponen los obispos en dema e intentan sacar a la gente que está atrapada en ese lugar. Se visten de amarillo, ya que como los obispos no pueden ver ese color es perfecto para usarlo como camuflaje y pasar por desapercibidos cuando están cerca de ellos.",
                "imagen": "https://i.pinimg.com/736x/02/be/80/02be804349d17a8da32f53dea65d5f7a.jpg"
            },
            {
                "nombre": "Clancy",
                "descripcion": "es el personaje de Tyler. Ha escrito cartas contando como se vive en Trench, en Dema y relatando su propia experiencia en esos lugares.",
                "imagen": "https://i.pinimg.com/736x/c5/e9/45/c5e94582234b2f2e80db7353020009af.jpg"
            },
            {
                "nombre": "Trash",
                "descripcion": "es el dragón azul brillante de la era Scaled and Icy que encarna el poder de la imaginación indomable. Aunque inicialmente es utilizado por los obispos como una fachada de propaganda feliz y corporativa para ocultar el control mental sobre Clancy, este 'dragón de basura' (asociado en realidad a los rebeldes) termina rompiendo las reglas y destruyendo las barreras del sistema.",
                "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROnSDLBA4Ga1ag_ndK1Q0cl8EZWEFRltFgBw&s"
            },
            {
                "nombre": "Ned",
                "descripcion": "es una criatura tímida y tierna introducida en la era Trench que simboliza la creatividad pura, la inocencia y el alma infantil del artista. Representa esa parte vulnerable de la mente que los obispos de Dema intentan robar y marchitar, siendo alimentada por el entusiasmo y el deseo de escapar de la opresión.",
                "imagen": "https://static.wikia.nocookie.net/twenty-one-pilots/images/0/0b/Ned.jpg/revision/latest?cb=20200614014742"
            }
            
        ]

        for personaje in personajes: #Aquí, recorremos la lista de personajes para mostrar su información y su imagen correspondiente. Para cada personaje, creamos dos columnas: una para el texto descriptivo y otra para la imagen. Esto lo hacemos utilizando un bucle for que recorre la lista de personajes y st.columns para crear las columnas. Luego, mostramos el nombre del personaje en negrita y color rojo, seguido de su descripción en
            texto_col, imagen_col = st.columns([3, 1])
            with texto_col:
                st.markdown(
                    f"- <span style='color: #8D0000; font-weight: bold;'>{personaje['nombre']}:</span> <span style='color: #000000;'>{personaje['descripcion']}</span>",
                    unsafe_allow_html=True
                )
            with imagen_col:
                st.image(personaje['imagen'], width=90)
    
    #-COLUMNA 2: DATOS INTERESANTES-
    with col2:
        st.markdown("<h2 style='color: #8D0000;'>LUGARES Y RELIGIÓN</h2>", unsafe_allow_html=True)
        
        #En esta sección, mostramos información sobre los lugares y la religión presentes en la historia. Para ello, creamos una lista de diccionarios que contienen el nombre del lugar, su descripción y un enlace a una imagen representativa. 
        lugares = [
            {
                "nombre": "VIALISMO",
                "descripcion": "es la religión de Dema predicada por los obispos. Esta religión está llena de ideales tóxicos y autodestructivos que te llenan de miedos e inseguridades que perjudican tu vida llevando a los habitantes de Dema a la autodestrucción, ya que según ellos esta es el único camino hacia el paraíso. Esta autodestrucción también les permite que las personas se conviertan en vasijas disponibles para que ellos las utilicen.",
                "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr7eo0Dkcq6e6DIiH-TzfLk4w4Fh9FENgvzg&s"
            },
            {
                "nombre": "Dema",
                "descripcion": "es la ciudad donde viven los obispos y la gente controlada por su sistema. Tiene forma de torre de silencio, los cuales eran edificios funerarios utilizados en India en donde ponían los cadáveres humanos separándoles por hombres, mujeres y niños; en el universo de top esta se separa en lápidas, edificios donde están encerradas las personas y las 9 torres correspondientes a cada uno de los 9 obispos.",
                "imagen": "https://static.wikia.nocookie.net/twenty-one-pilots/images/0/0a/DEMA_Map.webp/revision/latest/scale-to-width-down/250?cb=20240206114415"
            },
            {
                "nombre": "Trench",
                "descripcion": "es el continente donde transcurre la historia. Dentro de este se encuentra la ciudad de Dema, un puerto, la isla Voldsøy (isla de la violencia) y entre las montañas alejadas esta el campamento de los banditos, donde estos viven y es un lugar seguro.",
                "imagen": "https://pbs.twimg.com/media/FN_0bDXVEAATkD3.jpg"
            },
            
        ]

        for lugar in lugares: #Aquí, recorremos la lista de lugares para mostrar su información y su imagen correspondiente. Para cada lugar, creamos dos columnas: una para el texto descriptivo y otra para la imagen. Esto lo hacemos utilizando un bucle for que recorre la lista de lugares y st.columns para crear las columnas. Luego, mostramos el nombre del lugar en negrita y color rojo, seguido de su descripción en color negro.
            texto_col, imagen_col = st.columns([3, 1])
            with texto_col:
                st.markdown(
                    f"- <span style='color: #8D0000; font-weight: bold;'>{lugar['nombre']}:</span> <span style='color: #000000;'>{lugar['descripcion']}</span>",
                    unsafe_allow_html=True
                )
            with imagen_col:
                st.image(lugar['imagen'], width=90)


#En esta sección, se contará ya la historia a través de un botón interactivo con el comando st.button
        if 'mostrar_historia' not in st.session_state: 
            st.session_state.mostrar_historia = False

        st.markdown( #En primer lugar creamos el estilo para botón interactvo, para que sea blanco e independiente del modo de color de la página.
            """
            <style>
            div.stButton > button {
                background-color: #ffffff !important;
                color: #000000 !important;
                border: 1px solid #000000 !important;
            }
            div.stButton > button:hover {
                background-color: #f2f2f2 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if st.button('Conoce la Historia detrás de las canciones', key='btn_ir_historia'): #Aquí, creamos un botón interactivo que permite al usuario mostrar u ocultar la historia detrás de las canciones. Al hacer clic en el botón, se alterna el valor de la variable de sesión 'mostrar_historia', lo que permite controlar si se muestra o no la historia en la interfaz.
            st.session_state.mostrar_historia = not st.session_state.mostrar_historia

        if st.session_state.mostrar_historia: #Si la variable de sesión 'mostrar_historia' es verdadera, mostramos la historia detrás de las canciones. Para ello, utilizamos el comando st.markdown para mostrar un título y luego recorremos una lista de secciones que contienen el título, el texto y la imagen correspondiente a cada capítulo de la historia. Esto lo hacemos utilizando un bucle for que recorre la lista de secciones y st.markdown para mostrar la información con un estilo visual más llamativo.
            st.markdown('---')
            st.markdown("<h2 style='color: #8D0000;'>Historia</h2>", unsafe_allow_html=True)

            historia_secciones = [
                {
                    'titulo': 'Capítulo 1: Blurryface (La Manifestación de la Inseguridad)',
                    'texto': '**La historia comienza con la personificación de las inseguridades, miedos y dudas más oscuros de Tyler Joseph bajo el nombre de Blurryface. Este ente representa la voz de la autocrítica extrema y el deseo de rendirse. Por ello, canciones como Stressed Out y Fairly Local exponen la lucha diaria entre la persona que uno quiere ser y la presión asfixiante de las expectativas externas e internas. Blurryface se apodera de la mente, haciendo que el protagonista cuestione su valía, su arte y su fe. A lo largo de esta etapa, se establece la tensión entre dejarse llevar por el nihilismo que impone esta voz oscura o aferrarse a las creencias y a la música como una vía de escape, aunque el camino sea doloroso y confuso.**',
                    'imagen': 'https://static.wikia.nocookie.net/twenty-one-pilots/images/5/58/Blurryface.jpg/revision/latest?cb=20160105182338'
                },
                {
                    'titulo': 'Capítulo 2: Trench (El Escape y Los Banditos)',
                    'texto': '**Tyler, ahora adoptando la identidad de Clancy, logra despertar y tomar conciencia de su realidad. Se revela que su mente está atrapada en Dema, una ciudad circular y opresiva construida con bloques de hormigón y rodeada de lápidas de neón. Dema está gobernada por Nueve Obispos quienes controlan a los ciudadanos mediante el Vialism, una religión falsa que glorifica el suicidio, el auto-sacrificio y la resignación bajo la promesa de un destino llamado “The Glorious Gone”. Así, Clancy logra escapar de la ciudad hacia los valles inexplorados de Trench (Jumpsuit). En esta travesía por las trincheras, es perseguido implacablemente por los obispos, quienes intentan capturarlo mediante la técnica del seizing (poseer cuerpos o controlar mentes a distancia). Sin embargo, Clancy no está solo; cuenta con la ayuda de Josh Dun (The Torchbearer / El Portador de la Antorcha), su guía y compañero leal que enciende faros de esperanza, y de los Banditos, un grupo rebelde que viste cinta amarilla (símbolo de resistencia) para bloquear el control mental de los obispos. En este valle, Clancy también interactúa con Clifford (el buitre mascota de los Banditos que representa la transformación de la muerte en vida) y descubre a Ned, una criatura tímida y tierna que simboliza la inocencia pura, la imaginación y la creatividad del artista que los obispos intentan marchitar. Fortalecido por la resistencia, Clancy sobrevive en las trincheras y planea regresar para liberar a los demás prisioneros.**',
                    'imagen': 'https://www.billboard.com/wp-content/uploads/media/Twenty-One-Pilots-press-photo-2018-cr-Brad-Heaton-billboard-1548.jpg'
                },
                {
                    'titulo': 'Capítulo 3: Scaled and Icy (La Propaganda y el Control)',
                    'texto': '**El título del álbum es un anagrama de “Clancy is dead” (Clancy está muerto). Tras los eventos de Trench, Clancy es recapturado por los obispos y llevado de vuelta a Dema. Al no poder doblegar su espíritu rebelde por la fuerza, deciden cambiar de estrategia: lo encierran y lo obligan a protagonizar transmisiones en vivo y conciertos obligatorios alegres (Saturday, The Outside) para lavar el cerebro a la población y transmitir una falsa felicidad corporativa. A pesar de la fachada brillante y colorida, la rebelión sigue viva bajo la superficie. Se observa la intervención de Trash (El Dragón Azul), una majestuosa criatura que simboliza el poder de la imaginación indomable. Aunque inicialmente es utilizado por los obispos como fachada de propaganda feliz, el dragón (asociado a los buitres rebeldes) ataca a la cúpula de Dema, destruyendo el submarino corporativo donde los mantenían cautivos. Paralelamente, se revela que Keons (uno de los Nueve Obispos) simpatiza con los rebeldes y ayuda a Clancy, lo que provoca que los demás obispos lo asesinen por traición. Aprovechando el caos y el conocimiento adquirido, Clancy descubre cómo utilizar el poder de posesión mental (seizing) por cuenta propia, rompe las cadenas de la farsa y escapa de nuevo hacia la costa exterior, preparándose para la ofensiva final.**',
                    'imagen': 'https://rollingstoneindia.com/wp-content/uploads/2021/05/Twenty-One-Pilots-Pub-3-Mason-Castillo-LO.jpeg'
                },
                {
                    'titulo': 'Capítulo 4: Clancy (El Retorno y el Juicio Final)',
                    'texto': '**Clancy regresa voluntariamente a Dema y Trench (Overcompensate, Navigating) convertido en un líder de la resistencia mucho más maduro y empoderado. Ha aprendido a utilizar el poder de posesión, lo que le permite influir en las mentes de otros ciudadanos para reclutarlos desde adentro y sabotear a los obispos. Sin embargo, el clímax de esta incursión ocurre cuando Clancy debe cruzar el peligroso estrecho de Paladin Strait para llegar a la orilla donde lo esperan Josh y sus aliados, enfrentándose al abrumador miedo a una recaída final. Al cruzar, se produce el juicio definitivo y el enfrentamiento cara a cara contra Nico. Sin embargo, la confrontación toma un giro devastadoramente realista: en el forcejeo, Clancy es apuñalado por unas astas (simbolismo de que la misma esperanza o las herramientas creativas que utilizaba pueden volverse en su contra). Aunque logra liberar una onda expansiva que somete a Nico, el final de esta etapa revela una verdad dolorosa e inherente a la salud mental: la lucha no es lineal ni se gana de forma definitiva. Así, se descubre que "Clancy" no es solo una persona, sino un manto, un espíritu de resistencia que ha sido tomado por muchos a lo largo de los años. Incluso el propio villano, Nico, fue alguna vez un Clancy que perdió su batalla en el pasado y se convirtió en obispo. Al asumir la capa roja, Clancy acepta el peso de la repetición; el ciclo parece reiniciarse, pero esta vez con la convicción de que la resistencia es un proceso continuo.**',
                    'imagen': 'https://www.impericon.com/cdn/shop/articles/20240319_clancyalbumcover_2.png?v=1737119612'
                },
                {
                    'titulo': 'Capítulo 5: Breach (La Rendición y el Abrazo del Ciclo)',
                    'texto': '**En la conclusión de la saga, el concepto de la historia se rompe. Tyler Joseph abandona la necesidad de esconderse detrás de una compleja metáfora de ciencia ficción y mundos imaginarios. Así, en Breach, se revela que el verdadero enemigo no puede ser derrotado simplemente destruyendo una ciudad imaginaria. El ciclo de la depresión y la ansiedad no desaparece mágicamente. En lugar de luchar perpetuamente contra el avatar de Blurryface/Nico, el protagonista comprende que estas sombras oscuras son parte intrínseca de su propia mente y de su historia. De esta manera, la narrativa concluye con un mensaje de aceptación radical: para superar el dolor, hay que dejar de huir de él o combatirlo con elaboradas fantasías de escape. El ciclo se rompe simbólicamente cuando el creador decide dejar ir la ficción, abrazar sus vulnerabilidades y vivir en el mundo real, aceptando que las recaídas son posibles, pero que siempre habrá una nueva mañana para intentar estar bien.**',
                    'imagen': 'https://static.wikia.nocookie.net/twenty-one-pilots/images/9/9e/Breach.jpg/revision/latest?cb=20250521165146'
                }
            ]

            for idx, seccion in enumerate(historia_secciones): #Aquí, recorremos la lista de secciones de la historia para mostrar su información y su imagen correspondiente. 
                #Para cada sección, mostramos los subtítulos con un estilo diferente al texto y luego creamos dos columnas: una para el texto descriptivo y otra para la imagen. Esto lo hacemos utilizando un bucle for que recorre la lista de secciones y st.columns para crear las columnas. Luego, mostramos el texto de la historia en color
                st.markdown(
                    f"<h5 p style='color: #8D0000; font-weight: bold;'>{seccion['titulo']}</h5>",
                    unsafe_allow_html=True
                )
                texto_col, imagen_col = st.columns([3, 1])

                with texto_col:
                    texto_historia = st.session_state.get(f"historia_texto_{idx}", seccion['texto'])
                    st.write(texto_historia)

                with imagen_col:
                    foto_historia = st.session_state.get(f"historia_foto_{idx}", seccion['imagen'])
                    if foto_historia:
                        st.image(foto_historia, width=600)

# ============================================================================
# SEXTO: PÁGINA 4: MAPA DE VIDEOCLIPS (Ubicaciones de grabación)
# ============================================================================

elif pagina_seleccionada == '🗺️ Mapa':
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>🗺️ Mapa de Videoclips</h1>",
        unsafe_allow_html=True
    )
    
    st.markdown(
        "<p style='text-align: center; color: #000000; font-weight: bold; font-size: 1.1em;'>Explora los lugares donde fueron grabados los videoclips de Twenty One Pilots. Recuerda que no todas las canciones tienen uno.</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    #En primer lugar, utilizamos esta función para normalizar nombres de columnas, eliminando acentos, eñes y espacios, de modo que podamos comparar columnas sin errores.
    def normalize_col(col_name):
        if col_name is None:
            return ''
        text = str(col_name).lower().strip()
        for a, b in [('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'), ('ñ', 'n')]:
            text = text.replace(a, b)
        return ''.join(ch for ch in text if ch.isalnum())

    #Luego, utilizamos esta función para buscar la columna correcta en la base de datos a partir de una lista de posibles nombres, usando la normalización anterior.
    def obtener_columna(df, candidatos):
        normalized_columns = {normalize_col(c): c for c in df.columns}
        for c in candidatos:
            key = normalize_col(c)
            if key in normalized_columns:
                return normalized_columns[key]
        return None

    #Posteriormente, y de manera opcional, analizamos si la librería folium está disponible antes de continuar con el mapa. 
    #Esto lo puse principalmente para que, si alguien algún día utiliza de ejemplo mi código y no tiene folium instalado, no se rompa la página y pueda ver el resto de funcionalidades.
    if folium is None:
        st.error('La librería folium no está instalada. Por favor instala folium en tu entorno con: pip install folium')
        st.stop()

    #Luego, identificamos las columnas de lugar, latitud y longitud en la base de datos, utilizando la función anterior para buscar entre varias opciones posibles. Esto nos permite adaptarnos a diferentes formatos de bases de datos que puedan tener nombres de columnas distintos (nuevamente, esto es útil si alguien más utiliza mi código con su propia base de datos).
    lugar_col = obtener_columna(df_discografia, [
        'Lugar de grabación', 'Lugar de grabacion', 'Lugar Grabación', 'Lugar Grabacion',
        'Lugar', 'Location', 'ubicación', 'ubicacion', 'locacion'
    ])
    lat_col = obtener_columna(df_discografia, [
        'Latitud_video', 'Latitud video', 'Latitud', 'latitud_video', 'latitudvideo', 'lat', 'latitude'
    ])
    lon_col = obtener_columna(df_discografia, [
        'Longitud_video', 'Longitud video', 'Longitud', 'longitud_video', 'longitudvideo', 'lon', 'longitude'
    ])
    foto_lugar_col = obtener_columna(df_discografia, [
        'Fotografía_lugar', 'Fotografia_lugar', 'Fotografía Lugar', 'Fotografia Lugar', 'Foto Lugar', 'Foto_lugar'
    ])

    link_col = obtener_columna(df_discografia, [
        'Link_mv', 'Link MV', 'Link_MV', 'Linkmv', 'Link video', 'Link Vídeo', 'LinkVideo', 'Video Link'
    ])

    #En caso no se encuentran los datos mínimos, se mostrará una advertencia y no se creará el mapa. Esto también es opcional, pero lo puse para que algún usuario x sepa que no hay datos de ubicación y no se quede con la duda de por qué no aparece el mapa.
    if not lugar_col or not lat_col or not lon_col:
        st.warning('No se encuentran columnas válidas de ubicación o coordenadas en la base de datos.')
    else: #Si se encuentran las columnas necesarias, procedemos a filtrar los datos para quedarnos solo con las filas que tienen coordenadas válidas y no nulas. 
        #Esto es importante para evitar errores al crear el mapa y asegurar que solo se muestren ubicaciones correctas.
        df_map = df_discografia[
            df_discografia[lugar_col].notna() &
            df_discografia[lat_col].notna() &
            df_discografia[lon_col].notna()
        ].copy()
        df_map[lat_col] = pd.to_numeric(df_map[lat_col], errors='coerce')
        df_map[lon_col] = pd.to_numeric(df_map[lon_col], errors='coerce')
        df_map = df_map.dropna(subset=[lat_col, lon_col])

        #Si ya no queda ninguna fila con coordenadas válidas, lo indico al usuario.
        if df_map.empty:
            st.info('No hay canciones con videoclip y ubicación válida en la base de datos.')
        else:
            #En este punto, defino cómo obtener el nombre de la canción desde varias columnas posibles (por razones ya explicadas anteriormente). Esto es útil para que el mapa muestre correctamente los nombres de las canciones en los popups.
            def obtener_nombre_cancion(fila):
                candidatos = [
                    'TÍTULO', 'Título', 'TITULO', 'Canción', 'Cancion', 'Nombre', 'Nombre de canción', 'Nombre de cancion',
                    'Titulo', 'Title', 'title', 'track', 'Track', 'track_name', 'Track Name', 'Song', 'song'
                ]
                for c in candidatos: #Aquí, recorremos la lista de posibles nombres de columna para obtener el nombre de la canción desde la fila actual de la base de datos. 
                    #Si encontramos un valor válido (no nulo y no vacío), lo devolvemos como el nombre de la canción. Si no se encuentra ningún valor válido, devolvemos 'Título desconocido'.
                    if c in fila.index:
                        val = fila.get(c)
                        if pd.notna(val) and str(val).strip() != '':
                            return str(val).strip()
                return 'Título desconocido'

            df_map['song_name'] = df_map.apply(obtener_nombre_cancion, axis=1) #Aquí, aplicamos la función anterior a cada fila de la base de datos filtrada para crear una nueva columna 'song_name' que contendrá el nombre de la canción correspondiente a cada ubicación. Esto nos permitirá mostrar los nombres de las canciones en los popups del mapa.
            df_map['location'] = df_map[lugar_col].astype(str)
            df_map['latitude'] = df_map[lat_col]
            df_map['longitude'] = df_map[lon_col]

            midpoint = [df_map['latitude'].mean(), df_map['longitude'].mean()]
            mapa = folium.Map(location=midpoint, zoom_start=2, tiles='CartoDB positron', control_scale=True)

            ubicaciones = {}
            for _, row in df_map.iterrows():
                key = (row['latitude'], row['longitude'], row['location'])
                ubicaciones.setdefault(key, {'rows': [], 'photo': None})
                ubicaciones[key]['rows'].append(row)
                if foto_lugar_col and ubicaciones[key]['photo'] is None:
                    foto = row.get(foto_lugar_col)
                    if pd.notna(foto) and str(foto).strip() != '':
                        ubicaciones[key]['photo'] = str(foto).strip()

            #Luego, creamos los marcadores en el mapa con sus respectivos popups y enlaces (si existen). Aquí, recorremos el diccionario de ubicaciones y para cada ubicación, construimos el contenido del popup que mostrará el nombre del lugar, la foto (si existe) y la lista de canciones grabadas en ese lugar.
            for (lat, lon, location), info in ubicaciones.items():
                popup_lines = [f"<strong>{location}</strong><br/>"]
                if info['photo']:
                    popup_lines.append(f"<img src='{info['photo']}' style='width: 100%; max-width: 280px; display:block; margin-bottom: 8px; border-radius: 10px;' alt='Foto de {location}' />")
                for song_row in info['rows']:
                    line = f"• {song_row['song_name']}"
                    if link_col and pd.notna(song_row.get(link_col)):
                        line += f" <a href='{song_row[link_col]}' target='_blank' style='color:#ffffff;'>[Ver videoclip]</a>"
                    popup_lines.append(line)
                popup_html = '<br/>'.join(popup_lines)
                folium.Marker(
                    [lat, lon],
                    popup=folium.Popup(popup_html, max_width=350),
                    icon=folium.Icon(color='red', icon='music', prefix='fa')
                ).add_to(mapa)

            #Posteriormente, renderizamos el mapa para que tenga bordes redondeados y sombra, y lo mostramos.
            st.markdown("<div style='border-radius: 14px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.15);'>", unsafe_allow_html=True)
            map_html = mapa.get_root().render()
            components.html(map_html, height=650, scrolling=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown('---')
            st.markdown('### Videoclips incluidos')
            columnas_tabla = ['song_name', lugar_col, lat_col, lon_col]
            if link_col:
                columnas_tabla.insert(2, link_col)
            st.dataframe(
                df_map[columnas_tabla].rename(columns={
                    'song_name': 'Canción',
                    lugar_col: 'Lugar de grabación',
                    link_col: 'Link MV',
                    lat_col: 'Latitud',
                    lon_col: 'Longitud'
                }),
                use_container_width=True
            ) #Finalmente, mostramos la tabla con los videoclips incluidos en el mapa, renombrando las columnas para que sean más legibles. Esto permite al usuario ver de manera clara y organizada la información de cada videoclip, incluyendo el nombre de la canción, el lugar de grabación, el enlace al videoclip (si existe) y las coordenadas geográficas.

# ============================================================================
# SÉPTIMO: PÁGINA 5: JUEGO INTERACTIVO
# ============================================================================

elif pagina_seleccionada == '❓ ¿Qué tanto conoces a TOP? |-/':
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>ADIVINA LA CANCIÓN</h1>",
        unsafe_allow_html=True 
    ) #En primer lugar, mostramos el nombre del juego como título centrado y en color rojo. Esto sirve para que el usuario sepa de qué trata la página y se sienta motivado a participar en el juego.
    
    #Luego, presentamos una breve descripción para invitar al usuario a jugar.
    st.markdown(
        "<p style='text-align: center; color: #000000; font-weight: bold; font-size: 1.1em;'>Demuestra aquí y ahora si eres realmente un verdadero fan de TOP, o si aún te falta aprender más de la banda ✨.</p>",
        unsafe_allow_html=True
    )

    #Posteriormente, definimos la función para cargar las canciones desde un archivo Excel. Esta función utiliza la librería pandas para leer el archivo y extraer los títulos de las canciones, limpiándolos de caracteres no alfabéticos y normalizándolos a minúsculas. 
    #Además, maneja posibles errores como la ausencia del archivo o de la columna esperada.
    @st.cache_data
    def load_songs(archivo_excel="mi_base_de_datos.xlsx"):
        #En esta función se carga el archivo Excel (la base de datos) y se extraen los títulos de las canciones.
        #Luego, se limpiamos los títulos eliminando caracteres no alfabéticos y normalizando a minúsculas. 
        #Finalmente, se filtran los títulos vacíos que puedan haber quedado tras la limpieza.
        try:
            df = pd.read_excel(archivo_excel)
            if "TÍTULO" in df.columns:
               # Luego, limpio los títulos eliminando caracteres no alfabéticos y normalizo a minúsculas.
               titles = df["TÍTULO"].astype(str).apply(lambda x: re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚ ]', '', x).lower().strip())
               # Después, filtro los títulos vacíos que puedan haber quedado tras la limpieza.
               titles = [title for title in titles if title]
               return titles
            else:
                st.error("La columna 'TÍTULO' no se encontró en el archivo Excel. Por favor, asegúrate de que el nombre de la columna sea correcto.")
                return []
        except FileNotFoundError:
            st.error(f"El archivo no se encontró en la ruta: {archivo_excel}. Por favor, verifica la ruta y el nombre del archivo.")
            return []
        except Exception as e:
            st.error(f"Ocurrió un error al cargar el archivo Excel: {e}")
            return []

    #-Inicializar el estado del juego-
    #Aquí definimos la función para inicializar el estado del juego, seleccionando una canción secreta al azar de la lista de canciones cargadas y estableciendo los contadores de intentos y letras adivinadas. 
    #También se inicializan las variables que indican si el juego ha terminado o si el jugador ha ganado.
    def initialize_game():
        # Aquí defino el estado inicial de la partida y selecciono una canción secreta.
        songs = st.session_state.all_songs
        if not songs:
            st.error("No hay canciones disponibles para jugar. Por favor, verifica el archivo Excel.")
            return

        st.session_state.secret_word = random.choice(songs)
        st.session_state.guessed_letters = set()
        st.session_state.incorrect_guesses = 0
        st.session_state.max_incorrect_guesses = 6
        st.session_state.game_over = False
        st.session_state.game_won = False
        st.session_state.message = ""

    #-Función para mostrar la palabra secreta-
    #En primer lugar, definimos la función para mostrar la palabra secreta con guiones bajos para las letras no adivinadas y espacios para las letras adivinadas. 
    #Esto permite al jugador ver su progreso en el juego y saber cuántas letras le faltan por adivinar.
    def display_word(word, guessed_letters):
        #En esta función construimos la representación visible de la palabra con guiones y espacios.
        displayed = ""
        for char in word:
            if char == ' ':
                displayed += '  ' #Doble espacio para indicar un espacio en la palabra
            elif char in guessed_letters:
                displayed += char + ' '
            else:
                displayed += '_ '
        return displayed.strip()

    #-Cargar las canciones solo una vez-
    #Ahora, cargamos las canciones desde el archivo Excel solo una vez y las almacenamos en el estado de sesión de Streamlit. Esto evita que se recarguen cada vez que el usuario interactúa con la página. Esto realmente es para mejorar la eficiencia del juego.
    if 'all_songs' not in st.session_state:
        st.session_state.all_songs = load_songs('mi_base_de_datos.xlsx') # ¡Asegúrate de que esta ruta sea correcta!
        if not st.session_state.all_songs:
            st.stop() # Detener la ejecución si no hay canciones

    #-Inicializar juego si no está inicializado o si se reinicia-
    #Posteriormente, verificamos si el juego ya ha sido inicializado o si se ha terminado. Si no se ha inicializado o si el juego ha terminado, llamamos a la función de inicialización para reiniciar el juego y seleccionar una nueva canción secreta.
    if 'secret_word' not in st.session_state or st.session_state.game_over:
        initialize_game()

    #-Mostrar el estado actual del juego-
    #Finalmente, creamos tres columnas para centrar el contenido del juego y mostrar la palabra secreta, los intentos restantes y las letras adivinadas.
    col_izq, col_centro, col_der = st.columns([1, 4, 1])
    with col_centro: #Luego, dentro de la columna central, verificamos si el juego no ha terminado. Si el juego sigue activo, mostramos la palabra secreta con guiones bajos para las letras no adivinadas, los intentos restantes y las letras que ya han sido adivinadas por el jugador.
        if not st.session_state.game_over: #Si el juego no ha terminado, mostramos la palabra secreta con guiones bajos para las letras no adivinadas y espacios para las letras adivinadas. También mostramos los intentos restantes y las letras que ya han sido adivinadas por el jugador.
            word_display = display_word(st.session_state.secret_word, st.session_state.guessed_letters)
            st.markdown(f"<div style='background:#ffffff;color:#000000;padding:12px;border-radius:10px;display:inline-block;'>" \
                        f"<strong>Palabra:</strong> <code style='background:transparent;color:#000000;border:none;'>{word_display}</code></div>",
                        unsafe_allow_html=True)
            st.write(f"Intentos restantes: {st.session_state.max_incorrect_guesses - st.session_state.incorrect_guesses}")
            st.write(f"Letras adivinadas: {', '.join(sorted(list(st.session_state.guessed_letters))).upper()}")

        #-Entrada de la letra-
        #A continuación, creamos un formulario para que el jugador pueda ingresar su adivinanza, ya sea una letra o la palabra completa. 
        #Pero primero asignamos un estilo al formulario y los botones para que tengan un fondo blanco y letra negra.
        st.markdown(
            """
            <style>
            .stTextInput>div>div>input,
            .stTextInput>div>div>textarea {
                background-color: #ffffff !important;
                color: #000000 !important;
                border-color: #000000 !important;
            }
            /* Estilar el botón de envío dentro del formulario */
            .stForm button {
                background-color: #ffffff !important;
                color: #000000 !important;
                border: 1px solid #000000 !important;
                box-shadow: none !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        
        #Posteriormente, creamos un formulario para que el jugador pueda ingresar su adivinanza, ya sea una letra o la palabra completa.
        with st.form(key="form_adivinanza", clear_on_submit=True):
           guess = st.text_input("Adivina una letra o la palabra completa:", max_chars=20).lower().strip()
           submit_button = st.form_submit_button(label="Enviar")
        
        #Luego, verificamos si el jugador ha ingresado una letra o palabra completa y ha presionado el botón de envío. Si es así, validamos la entrada para asegurarnos de que sea una letra o una palabra completa válida.
        if guess and submit_button:
            if len(guess) == 1 and guess.isalpha(): #Adivinanza de una sola letra.
                #Si la letra ya fue adivinada, aviso al usuario.
                if guess in st.session_state.guessed_letters:
                    st.warning("Ya adivinaste esa letra. ¡Intenta con otra!")
                elif guess in st.session_state.secret_word:
                    #Si la letra está en la palabra, la agregamos a las letras adivinadas.
                    st.session_state.guessed_letters.add(guess)
                    #Verificamos si ganó después de cada letra correcta.
                    current_display = display_word(st.session_state.secret_word, st.session_state.guessed_letters).replace(' ', '')
                    cleaned_secret_word = st.session_state.secret_word.replace(' ', '')
                    if current_display == cleaned_secret_word:
                        st.session_state.game_won = True
                        st.session_state.game_over = True
                        st.session_state.message = "¡Qué increíble es tener a alguien realmente fan de esta increíble banda. ¡Ganaste!"
                else:
                    #Si la letra no está en la palabra, se incrementa el contador de errores.
                    st.session_state.incorrect_guesses += 1
                    st.session_state.guessed_letters.add(guess) #También añadimos letras incorrectas a las adivinadas.
                    st.error("¡Incorrecto!")
            elif len(guess) > 1 and guess.isalpha(): #Adivinanza de la palabra completa.
                #Si el usuario intenta adivinar la palabra completa, comparamos directamente.
                if guess == st.session_state.secret_word: #Así, si la palabra completa es correcta, el jugador gana inmediatamente.
                    st.session_state.game_won = True
                    st.session_state.game_over = True
                    st.session_state.message = "¡Qué increíble es tener a alguien realmente fan de esta increíble banda. ¡Ganaste!"
                else: #Si la palabra completa es incorrecta, el jugador pierde todos los intentos restantes y el juego termina.
                    st.session_state.incorrect_guesses = st.session_state.max_incorrect_guesses
                    st.session_state.game_over = True
                    st.session_state.message = "Oooh, inténtalo de nuevo, quizás aún deberías conocer más de la banda. ¡Te quedaste sin intentos!"
            else: #Si la entrada no es válida (ni una letra ni una palabra completa), mostramos un mensaje de advertencia al usuario.
                st.warning("Por favor, ingresa solo una letra o la palabra completa (solo caracteres alfabéticos).")

        #-Verificar si se agotaron los intentos-
        if st.session_state.incorrect_guesses >= st.session_state.max_incorrect_guesses and not st.session_state.game_won:
            #Si no quedan intentos, el juego debe marcarseo como terminado.
            st.session_state.game_over = True
            if not st.session_state.message: #Solo si no hay un mensaje previo de adivinar palabra completa
                st.session_state.message = "Te quedaste sin intentos. Oooh, inténtalo de nuevo, quizás aún deberías conocer más de la banda."

    #-Mensaje de fin de juego y botón para reiniciar-
    #Si el juego ha terminado, mostramos la palabra secreta y un mensaje final dependiendo de si el jugador ganó o perdió. También estilizamos el botón de reinicio para que mantenga la estética del juego y permitimos al jugador reiniciar el juego haciendo clic en él.
    if st.session_state.game_over:
        st.markdown(f"### La palabra secreta era: **{st.session_state.secret_word.upper()}**")
        st.info(st.session_state.message)
        st.markdown(
            """
            <style>
            .stButton>button {
                background-color: #ffffff !important;
                color: #000000 !important;
                border: 1px solid #000000 !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        if st.button("¡Jugar de nuevo!"):
            initialize_game()
            st.rerun() #Reinicia la página para comenzar un nuevo juego.

# ============================================================================
# OCTAVO: PÁGINA 6: ESTADÍSTICAS (Gráficos y análisis)
# ============================================================================

elif pagina_seleccionada == '📊 Estadísticas':
    #En primer lugar, utilizamos st.markdown para mostrar el título de la última sección centrado y con estilo.
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>📊 ESTADÍSTICAS Y ANÁLISIS</h1>",
        unsafe_allow_html=True
    )
    
    #Luego, creamos una separación visual entre el título y el contenido.
    st.markdown("---")
    
    #-GRÁFICO 1: CANCIONES POR ÁLBUM-
    #Posteriormente, presentamos el subtítulo para el primer gráfico.
    st.markdown("<h2 style='color: #8D0000;'>🎵 Canciones por Álbum</h2>", unsafe_allow_html=True)
    
    #A continuación, contamos cuántas canciones hay en cada álbum utilizando la función .value_counts() de pandas, que nos devuelve un Series con los conteos de cada valor único en la columna 'Álbum'.
    canciones_por_album = df_discografia['Álbum'].value_counts()
    
    #Después, generamos un gráfico de barras a partir de esos conteos con st.bar_chart(), que crea automáticamente el gráfico.
    st.bar_chart(canciones_por_album)

    st.markdown("---")
    
    #-GRÁFICO 2: DISTRIBUCIÓN POR GÉNERO-
    #Ahora comprobamos si la columna 'Género' existe en la base de datos para evitar errores. Nuevamente y como en casos anteriores, esto es útil si alguien más utiliza mi código con su propia base de datos que podría no tener esa columna.
    if 'Género' in df_discografia.columns: 
        #Si existe, mostramos el subtítulo para la distribución por género.
        st.markdown("<h2 style='color: #8D0000;'>🎸 Distribución por Género</h2>", unsafe_allow_html=True)
        
        #Luego calculamos la cantidad de canciones por cada género.
        canciones_por_genero = df_discografia['Género'].value_counts()
        
        #Ygeneramos el gráfico de barras para visualizar esa distribución.
        st.bar_chart(canciones_por_genero)
        
        st.markdown("---")
    
    #-TABLA DE DATOS COMPLETA-
    #Finalmente, presento el título de la tabla con todos los datos utilizados en los gráficos, para que el usuario pueda ver la información completa de manera tabular.
    st.markdown("<h2 style='color: #8D0000;'>📋 Tabla Completa de Datos</h2>", unsafe_allow_html=True)
    
    #Como último paso, mostramos la base de datos completa y permitimos que use todo el ancho disponible.
    st.dataframe(
        df_discografia,
        use_container_width=True
    )
    
    
# ============================================================================
# NOVENO (OPCIONAL):FOOTER (Pie de página, más que nada por estética.
# ============================================================================

#Después de todo el contenido, separamos la sección con una línea horizontal.
st.markdown("---")
#Insertamos el pie de página con un st.markdown que contiene HTML para centrar el texto, cambiar el color y tamaño de fuente, y mostrar un mensaje de derechos reservados (a modo de broma claro).
st.markdown("<footer style='text-align: center; color: #888888; font-size: 14px;'>© 2026 Mi Web de TOP 😝. Todos los derechos reservados.</footer>", unsafe_allow_html=True)

# ============================================================================
# FIN DEL CÓDIGO
# ============================================================================
