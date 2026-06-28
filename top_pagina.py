# ============================================================================
# PÁGINA WEB DE TWENTY ONE PILOTS CON STREAMLIT
# ============================================================================
# Antes de ejecutar este script, asegurate de estar en la carpeta correcta:
# cd ruta_de_tu_carpeta (ej: cd c:\Users\marti\OneDrive\Escritorio\PC3)

# ============================================================================
# PASO 1: CREAR ENTORNO VIRTUAL (Ejecuta esto en la terminal)
# ============================================================================
# python -m venv .venv
# Esto crea un entorno virtual donde instalaremos las librerías necesarias

# ============================================================================
# PASO 2: ACTIVAR ENTORNO VIRTUAL (Ejecuta esto en la terminal)
# ============================================================================
# En Windows:
# .venv\Scripts\activate
# En MacOS/Linux:
# source .venv/bin/activate

# ============================================================================
# PASO 3: INSTALAR STREAMLIT Y LIBRERÍAS (Ejecuta esto en la terminal)
# ============================================================================
# pip install streamlit
# pip install streamlit-option-menu
# pip install pandas
# pip install openpyxl
# pip install folium

# ============================================================================
# PASO 4: EJECUTAR LA PÁGINA WEB (Ejecuta esto en la terminal)
# ============================================================================
# python -m streamlit run top_pagina.py

# ============================================================================
# IMPORTAR LIBRERÍAS
# ============================================================================

# Importar Streamlit: librería principal para crear aplicaciones web
import streamlit as st
# Importar option_menu: para crear menús de navegación personalizados
from streamlit_option_menu import option_menu
# Importar pandas: para manipular datos (DataFrames)
import pandas as pd
# Importar openpyxl: para leer archivos Excel
import openpyxl
# Importar folium para mapas interactivos

import folium
import streamlit.components.v1 as components
# Importar random para seleccionar videos aleatorios
import random
import re


# ============================================================================
# CARGAR LA BASE DE DATOS
# ============================================================================

# Leer el archivo Excel y guardarlo en la variable df_discografia
df_discografia = pd.read_excel("mi_base_de_datos.xlsx")
# Esto carga todos los datos de canciones desde el archivo Excel

# ============================================================================
# CONFIGURAR LA PÁGINA
# ============================================================================

# Establecer el título y el ícono de la página en la pestaña del navegador
st.set_page_config(
    page_title="Twenty One Pilots | Discografía",  # Título de la pestaña
    page_icon="🎵",  # Ícono de la pestaña
    layout="wide"  # Diseño de página ancha (más espacio)
)

# ============================================================================
# APLICAR ESTILOS CSS PERSONALIZADOS (Fondo de pantalla)
# ============================================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600;700&display=swap'); 
    /* Aplicar la fuente a toda la aplicación */ html, body, [class*="st-"] {
    font-family: 'Jost', sans-serif;
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
    unsafe_allow_html=True  # Permitir que Streamlit interprete el código HTML/CSS
)

# ============================================================================
# CREAR MENÚ DE NAVEGACIÓN EN LA BARRA LATERAL
# ============================================================================

with st.sidebar:
    # Crear un menú con opciones de navegación
    pagina_seleccionada = option_menu(
        menu_title="🎵 MENÚ PRINCIPAL",  # Título del menú
        options=['🏠 Inicio', '💿 Discografía', '📖 Lore', '🗺️ Mapa', '¿Qué tanto conoces a TOP? |-/', '📊 Estadísticas'],  # Opciones disponibles
        icons=['house', 'music-note-list', 'map', 'graph-up'],  # Iconos de cada opción
        menu_icon="mic",  # Ícono principal del menú
        default_index=0  # La opción seleccionada por defecto (0 = Inicio)
    )
    # El menú se guardará en la variable 'pagina_seleccionada'

# ============================================================================
# PÁGINA 1: INICIO (Presentación de la banda)
# ============================================================================

if pagina_seleccionada == '🏠 Inicio':
    # Mostrar título principal centrado y con color rojo
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>TWENTY ONE PILOTS</h1>",
        unsafe_allow_html=True
    )
    
    # Agregar el logo oficial de la banda centrado
    st.markdown(
        "<div style='display: flex; justify-content: center; margin: 20px 0;'>"
        "<img src='https://logos-world.net/wp-content/uploads/2024/12/21-Pilots-Logo-2011.png' "
        "alt='Twenty One Pilots Logo' style='width: 280px; border-radius: 8px;'>"
        "</div>",
        unsafe_allow_html=True
    )
    
    # Crear dos columnas para organizar el contenido
    col1, col2 = st.columns(2)
    
    # ========== COLUMNA 1: INFORMACIÓN GENERAL ==========
    with col1:
        st.markdown("<h3 style='color: #8D0000;'>ℹ️ Acerca de la Banda</h3>", unsafe_allow_html=True)
        
        # Texto de presentación

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
        
    
    # ========== COLUMNA 2: DATOS INTERESANTES ==========
    with col2:
        st.markdown("<h3 style='color: #8D0000;'>🎸 Datos Interesantes</h3>", unsafe_allow_html=True)
        
        # Información adicional

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

    
    # Agregar separador visual
    st.markdown("---")
    
    # Sección de videos destacados con selección aleatoria
    st.markdown("<h3 style='text-align: center; color: #8D0000;'>🎬 Videos Destacados</h3>", unsafe_allow_html=True)
    
    # Obtener videos disponibles de la base de datos
    videos_disponibles = df_discografia[df_discografia['Link_mv'].notna()]['Link_mv'].dropna().unique().tolist()
    
    if len(videos_disponibles) >= 2:
        # Seleccionar 2 videos aleatorios
        videos_seleccionados = random.sample(list(videos_disponibles), min(2, len(videos_disponibles)))
        
        # Crear columnas para mostrar videos
        video_col1, video_col2 = st.columns(2)
        
        with video_col1:
            st.video(videos_seleccionados[0])  # Video de YouTube
        
        with video_col2:
            if len(videos_seleccionados) > 1:
                st.video(videos_seleccionados[1])  # Video de YouTube
    else:
        st.markdown(
            "<p style='text-align: center; color: #000000;'>No hay videos disponibles en la base de datos.</p>",
            unsafe_allow_html=True
        )

# ============================================================================
# PÁGINA 2: DISCOGRAFÍA (Álbumes y canciones)
# ============================================================================

elif pagina_seleccionada == '💿 Discografía':
    # Mostrar título
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>|-/ DISCOGRAFÍA DE TWENTY ONE PILOTS</h1>",
        unsafe_allow_html=True
    )
    
    # Pequeña introducción
    st.markdown(
        "<p style='text-align: center; color: #000000; font-weight: bold; font-size: 1.1em;'>Aquí puedes explorar todos los álbumes y canciones de Twenty One Pilots, ver detalles de cada canción y conocer el mensaje detrás de cada una de ellas.</p>",
        unsafe_allow_html=True
    )
    
    # Agregar separador
    st.markdown("---")
    
    portada_col = 'Link_portada' if 'Link_portada' in df_discografia.columns else None
    albumes = df_discografia['Álbum'].dropna().unique()

    def columna_excluida(col):
        nombre = col.lower().replace(' ', '').replace('_', '')
        return nombre in ['latitudvideo', 'longitudvideo', 'latitud', 'longitud', 'amplitud']

    def obtener_nombre_cancion(fila):
        candidatos = [
            'TÍTULO', 'Título', 'TITULO', 'Canción', 'Cancion', 'Nombre', 'Nombre de canción', 'Nombre de cancion',
            'Titulo', 'Título', 'Title', 'title', 'track', 'Track',
            'track_name', 'Track Name', 'Song', 'song'
        ]
        for c in candidatos:
            if c in fila.index:
                val = fila.get(c)
                if pd.notna(val) and str(val).strip() != '':
                    return str(val).strip()
        for col in fila.index:
            col_low = col.lower()
            if any(k in col_low for k in ['nombre', 'titulo', 'title', 'track', 'song']):
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

    def buscar_valor(fila, candidatos):
        for c in candidatos:
            if c in fila.index:
                val = fila.get(c)
                if pd.notna(val) and str(val).strip() != '':
                    return val
        return None

    if 'song_detalle' not in st.session_state:
        st.session_state['song_detalle'] = None
    if 'album_abierto' not in st.session_state:
        st.session_state['album_abierto'] = None

    if st.session_state.get('song_detalle'):
        fila_det = pd.Series(st.session_state['song_detalle']['fila'])
        nombre_det = obtener_nombre_cancion(fila_det) or 'Título desconocido'
        st.markdown(f"<h2 style='color: #8D0000;'>Detalles de la canción: {nombre_det}</h2>", unsafe_allow_html=True)
        col_img, col_info = st.columns([1, 2])
        with col_img:
            link_portada = buscar_valor(fila_det, ['Link_portada'])
            if link_portada:
                st.image(link_portada, width=320)
            foto_lugar = buscar_valor(fila_det, ['Fotografía_lugar', 'Fotografia_lugar', 'Fotografía Lugar', 'Fotografia Lugar'])
            if foto_lugar:
                st.image(foto_lugar, width=320)
                link_mv = buscar_valor(fila_det, ['Link_mv', 'Link MV', 'Link_MV', 'Linkmv'])
                if link_mv:
                    st.markdown(f"<p style='color: #000000; margin-top: 10px;'><strong>Videoclip:</strong> <a href='{link_mv}' target='_blank'>{link_mv}</a></p>", unsafe_allow_html=True)
        with col_info:
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

    for idx, album in enumerate(albumes):
        canciones_del_album = df_discografia[df_discografia['Álbum'] == album]
        if canciones_del_album.empty:
            continue

        foto_album = None
        if portada_col and portada_col in canciones_del_album.columns:
            valores_foto = canciones_del_album[portada_col].dropna().unique()
            if len(valores_foto) > 0:
                foto_album = valores_foto[0]

        st.markdown(
            f"<h2 style='color: #8D0000; border-bottom: 2px solid #FFD700; padding-top: 15px;'>💿 {album}</h2>",
            unsafe_allow_html=True
        )
        album_col1, album_col2 = st.columns([1, 2])
        with album_col1:
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
        with album_col2:
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

        if st.session_state.get('album_abierto') == album:
            st.markdown(
                f"<h3 style='color: #8D0000;'>🎵 Canciones en {album}</h3>",
                unsafe_allow_html=True
            )
            for song_idx, fila in canciones_del_album.iterrows():
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
            st.markdown('---')

    # Mostrar estadísticas generales
    st.markdown("<h3 style='color: #8D0000;'>📊 Estadísticas Generales</h3>", unsafe_allow_html=True)
    
    # Crear columnas para mostrar datos
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    
    with stat_col1:
        # Contar el total de álbumes
        total_albumes = len(albumes)
        st.metric(
            label="Total de Álbumes",  # Etiqueta
            value=total_albumes  # Valor a mostrar
        )
    
    with stat_col2:
        # Contar el total de canciones
        total_canciones = len(df_discografia)
        st.metric(
            label="Total de Canciones",
            value=total_canciones
        )
    
    with stat_col3:
        # Contar los géneros únicos
        if 'Género' in df_discografia.columns:
            total_generos = df_discografia['Género'].nunique()
            # .nunique() cuenta valores únicos
            st.metric(
                label="Géneros Musicales",
                value=total_generos
            )

    # Cerrar el contenedor de fondo específico para Discografía
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================================
# PÁGINA 2: DISCOGRAFÍA (Álbumes y canciones)
# ============================================================================

elif pagina_seleccionada == '📖 Lore':
    # Mostrar título
    pass
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>GUÍA SOBRE PERSONAJES Y CIUDADES DE LA HISTORIA QUE NECESITAN SABER PARA ENTENDER</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: #000000; font-weight: bold; font-size: 1.1em;'>Esto al principio puede ser un poco confuso y no es necesario aprendérselo ahora, pero cada vez que se pierdan con respecto a algún personaje, vuelvan a acá para aclarar quién es. Cabe aclarar que estas descripciones se van modificando y completando a medida que salen más detalles sobre los personajes.</p>",
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    
    # ========== COLUMNA 1: INFORMACIÓN GENERAL ==========
    with col1:
        st.markdown("<h2 style='color: #8D0000;'>PERSONAJES</h2>", unsafe_allow_html=True)
        
        # Texto de presentación con imágenes a la derecha
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

        for personaje in personajes:
            texto_col, imagen_col = st.columns([3, 1])
            with texto_col:
                st.markdown(
                    f"- <span style='color: #8D0000; font-weight: bold;'>{personaje['nombre']}:</span> <span style='color: #000000;'>{personaje['descripcion']}</span>",
                    unsafe_allow_html=True
                )
            with imagen_col:
                st.image(personaje['imagen'], width=90)
    
    # ========== COLUMNA 2: DATOS INTERESANTES ==========
    with col2:
        st.markdown("<h2 style='color: #8D0000;'>LUGARES Y RELIGIÓN</h2>", unsafe_allow_html=True)
        
        # Información adicional
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

        for lugar in lugares:
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

        if st.button('Conoce la Historia detrás de las canciones', key='btn_ir_historia'):
            st.session_state.mostrar_historia = not st.session_state.mostrar_historia

        if st.session_state.mostrar_historia:
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

            for idx, seccion in enumerate(historia_secciones):
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
# PÁGINA 4: MAPA DE VIDEOCLIPS (Ubicaciones de grabación)
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

    def normalize_col(col_name):
        if col_name is None:
            return ''
        text = str(col_name).lower().strip()
        for a, b in [('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'), ('ñ', 'n')]:
            text = text.replace(a, b)
        return ''.join(ch for ch in text if ch.isalnum())

    def obtener_columna(df, candidatos):
        normalized_columns = {normalize_col(c): c for c in df.columns}
        for c in candidatos:
            key = normalize_col(c)
            if key in normalized_columns:
                return normalized_columns[key]
        return None

    if folium is None:
        st.error('La librería folium no está instalada. Por favor instala folium en tu entorno con: pip install folium')
        st.stop()

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

    if not lugar_col or not lat_col or not lon_col:
        st.warning('No se encuentran columnas válidas de ubicación o coordenadas en la base de datos.')
    else:
        df_map = df_discografia[
            df_discografia[lugar_col].notna() &
            df_discografia[lat_col].notna() &
            df_discografia[lon_col].notna()
        ].copy()
        df_map[lat_col] = pd.to_numeric(df_map[lat_col], errors='coerce')
        df_map[lon_col] = pd.to_numeric(df_map[lon_col], errors='coerce')
        df_map = df_map.dropna(subset=[lat_col, lon_col])

        if df_map.empty:
            st.info('No hay canciones con videoclip y ubicación válida en la base de datos.')
        else:
            def obtener_nombre_cancion(fila):
                candidatos = [
                    'TÍTULO', 'Título', 'TITULO', 'Canción', 'Cancion', 'Nombre', 'Nombre de canción', 'Nombre de cancion',
                    'Titulo', 'Title', 'title', 'track', 'Track', 'track_name', 'Track Name', 'Song', 'song'
                ]
                for c in candidatos:
                    if c in fila.index:
                        val = fila.get(c)
                        if pd.notna(val) and str(val).strip() != '':
                            return str(val).strip()
                return 'Título desconocido'

            df_map['song_name'] = df_map.apply(obtener_nombre_cancion, axis=1)
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
            )

# ============================================================================
# PÁGINA 5: JUEGO INTERACTIVO
# ============================================================================

elif pagina_seleccionada == '¿Qué tanto conoces a TOP? |-/':
    # Mostrar título
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>ADIVINA LA CANCIÓN</h1>",
        unsafe_allow_html=True
    )
    
    st.markdown(
        "<p style='text-align: center; color: #000000; font-weight: bold; font-size: 1.1em;'>Demuestra aquí y ahora si eres realmente un verdadero fan de TOP, o si aún te falta aprender más de la banda ✨.</p>",
        unsafe_allow_html=True
    )

    @st.cache_data
    def load_songs(archivo_excel="mi_base_de_datos.xlsx"):
        try:
            df = pd.read_excel(archivo_excel)
            if "TÍTULO" in df.columns:
               # Limpiar títulos: remover caracteres no alfabéticos y convertir a minúsculas
               titles = df["TÍTULO"].astype(str).apply(lambda x: re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚ ]', '', x).lower().strip())
               # Filtrar títulos vacíos después de la limpieza
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

# --- Inicializar el estado del juego ---
    def initialize_game():
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

# --- Función para mostrar la palabra secreta ---
    def display_word(word, guessed_letters):
        displayed = ""
        for char in word:
            if char == ' ':
                displayed += '  ' # Doble espacio para indicar un espacio en la palabra
            elif char in guessed_letters:
                displayed += char + ' '
            else:
                displayed += '_ '
        return displayed.strip()

# --- Cargar las canciones solo una vez ---
    if 'all_songs' not in st.session_state:
        st.session_state.all_songs = load_songs('mi_base_de_datos.xlsx') # ¡Asegúrate de que esta ruta sea correcta!
        if not st.session_state.all_songs:
            st.stop() # Detener la ejecución si no hay canciones

# --- Inicializar juego si no está inicializado o si se reinicia ---
    if 'secret_word' not in st.session_state or st.session_state.game_over:
        initialize_game()

# --- Mostrar el estado actual del juego ---
    col_izq, col_centro, col_der = st.columns([1, 4, 1])
    with col_centro:
        if not st.session_state.game_over:
            st.markdown(f"### Palabra: `{display_word(st.session_state.secret_word, st.session_state.guessed_letters)}`")
            st.write(f"Intentos restantes: {st.session_state.max_incorrect_guesses - st.session_state.incorrect_guesses}")
            st.write(f"Letras adivinadas: {', '.join(sorted(list(st.session_state.guessed_letters))).upper()}")

    # --- Entrada de la letra ---
        with st.form(key="form_adivinanza", clear_on_submit=True):
           guess = st.text_input("Adivina una letra o la palabra completa:", max_chars=20).lower().strip()
           submit_button = st.form_submit_button(label="Enviar")

        if guess and submit_button:
            if len(guess) == 1 and guess.isalpha(): # Adivinanza de una sola letra
                if guess in st.session_state.guessed_letters:
                    st.warning("Ya adivinaste esa letra. ¡Intenta con otra!")
                elif guess in st.session_state.secret_word:
                    st.session_state.guessed_letters.add(guess)
                # Verificar si ganó después de cada letra correcta
                    current_display = display_word(st.session_state.secret_word, st.session_state.guessed_letters).replace(' ', '')
                    cleaned_secret_word = st.session_state.secret_word.replace(' ', '')
                    if current_display == cleaned_secret_word:
                        st.session_state.game_won = True
                        st.session_state.game_over = True
                        st.session_state.message = "¡Qué increíble es tener a alguien realmente fan de esta increíble banda. ¡Ganaste!"
                         # <--- Añade esto para refrescar la pantalla inmediatamente con el mensaje
                else:
                    st.session_state.incorrect_guesses += 1
                    st.session_state.guessed_letters.add(guess) # También añadir letras incorrectas a las adivinadas
                    st.error("¡Incorrecto!")
            elif len(guess) > 1 and guess.isalpha(): # Adivinanza de la palabra completa
                if guess == st.session_state.secret_word:
                    st.session_state.game_won = True
                    st.session_state.game_over = True
                    st.session_state.message = "¡Qué increíble es tener a alguien realmente fan de esta increíble banda. ¡Ganaste!"
                     # <--- Añade esto también
                else:
                    st.session_state.incorrect_guesses = st.session_state.max_incorrect_guesses # Pierde todos los intentos si falla la palabra
                    st.session_state.game_over = True
                    st.session_state.message = "Oooh, inténtalo de nuevo, quizás aún deberías conocer más de la banda. ¡Te quedaste sin intentos!"
                     # <--- Y aquí para forzar la actualización
            else:
                st.warning("Por favor, ingresa solo una letra o la palabra completa (solo caracteres alfabéticos).")
        
        # Limpiar el input después de enviar
            

    # --- Verificar si se agotaron los intentos ---
        if st.session_state.incorrect_guesses >= st.session_state.max_incorrect_guesses and not st.session_state.game_won:
            st.session_state.game_over = True
            if not st.session_state.message: # Solo si no hay un mensaje previo de adivinar palabra completa
                st.session_state.message = "Te quedaste sin intentos. Oooh, inténtalo de nuevo, quizás aún deberías conocer más de la banda."
             # <--- Asegúrate de que este rerun esté presente para que se renderice el bloque inferior de fin de juego

# --- Mensaje de fin de juego y botón para reiniciar ---
    if st.session_state.game_over:
        st.markdown(f"### La palabra secreta era: **{st.session_state.secret_word.upper()}**")
    
    # Mostramos el mensaje (Ganaste, Perdiste, o Sin intentos) de forma estática
        st.info(st.session_state.message)
    
    # El juego solo se reiniciará cuando el usuario haga clic en este botón explícitamente
        if st.button("¡Jugar de nuevo!"):
            initialize_game()
            st.rerun() # Este rerun dentro del botón sí es correcto porque el usuario acaba de pedir reiniciar


# ============================================================================
# PÁGINA 5: ESTADÍSTICAS (Gráficos y análisis)
# ============================================================================

elif pagina_seleccionada == '📊 Estadísticas':
    # Mostrar título
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>📊 ESTADÍSTICAS Y ANÁLISIS</h1>",
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # ========== GRÁFICO 1: CANCIONES POR ÁLBUM ==========
    st.markdown("<h2 style='color: #8D0000;'>🎵 Canciones por Álbum</h2>", unsafe_allow_html=True)
    
    # Contar cuántas canciones hay en cada álbum
    canciones_por_album = df_discografia['Álbum'].value_counts()
    # .value_counts() cuenta cuántas veces aparece cada valor
    
    # Crear un gráfico de barras
    st.bar_chart(canciones_por_album)
    # st.bar_chart(): crea un gráfico de barras automáticamente
    
    st.markdown("---")
    
    # ========== GRÁFICO 2: DISTRIBUCIÓN POR GÉNERO ==========
    if 'Género' in df_discografia.columns:
        st.markdown("<h2 style='color: #8D0000;'>🎸 Distribución por Género</h2>", unsafe_allow_html=True)
        
        # Contar las canciones por género
        canciones_por_genero = df_discografia['Género'].value_counts()
        
        # Crear un gráfico de pastel
        st.bar_chart(canciones_por_genero)
        
        st.markdown("---")
    
    # ========== TABLA DE DATOS COMPLETA ==========
    st.markdown("<h2 style='color: #8D0000;'>📋 Tabla Completa de Datos</h2>", unsafe_allow_html=True)
    
    # Mostrar la tabla con todos los datos
    st.dataframe(
        df_discografia,
        use_container_width=True
    )
    
    # ========== DESCARGA DE DATOS ==========
    st.markdown("---")
    st.markdown("<h2 style='color: #8D0000;'>⬇️ Descargar Datos</h2>", unsafe_allow_html=True)
    
    # Convertir el DataFrame a archivo CSV
    csv_data = df_discografia.to_csv(index=False)
    # .to_csv(): convierte el DataFrame a formato CSV (valores separados por comas)
    
    # Crear un botón de descarga
    st.download_button(
        label="📥 Descargar como CSV",  # Texto del botón
        data=csv_data,  # Los datos a descargar
        file_name="discografia_top.csv",  # Nombre del archivo
        mime="text/csv"  # Tipo de archivo (CSV)
    )

# ============================================================================
# FOOTER (Pie de página)
# ============================================================================

st.markdown("---")
st.markdown(
    "<footer style='text-align: center; color: #888888; font-size: 12px;'>"
    "<p>🎵 Página desarrollada con Streamlit | © 2024 Twenty One Pilots Database 🎵</p>"
    "</footer>",
    unsafe_allow_html=True
)

# ============================================================================
# FIN DEL CÓDIGO
# ============================================================================
