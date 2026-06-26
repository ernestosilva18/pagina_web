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
    /* Cambiar el fondo de la aplicación */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://wallpaperaccess.com/full/828106.jpg");
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
        color: #8D0000 !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }
    
    /* Estilo para los subtítulos */
    h2, h3 {
        color: #8D0000 !important;
    }
    
    /* Estilo para el texto general */
    p {
        color: #000000 !important;
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
        options=['🏠 Inicio', '💿 Discografía', '🗺️ Mapa', '📊 Estadísticas'],  # Opciones disponibles
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
        "<h1 style='text-align: center; color: #8D0000;'>🎵 TWENTY ONE PILOTS 🎵</h1>",
        unsafe_allow_html=True
    )
    
    # Agregar el logo oficial de la banda centrado
    st.markdown(
        "<div style='display: flex; justify-content: center; margin: 20px 0;'>"
        "<img src='https://band-logos.com/wp-content/uploads/2025/07/Twenty-One-Pilots-Band-Logo-3.png' "
        "alt='Twenty One Pilots Logo' style='width: 280px; border-radius: 8px;'>"
        "</div>",
        unsafe_allow_html=True
    )
    
    # Crear dos columnas para organizar el contenido
    col1, col2 = st.columns(2)
    
    # ========== COLUMNA 1: INFORMACIÓN GENERAL ==========
    with col1:
        st.markdown("<h2 style='color: #8D0000;'>ℹ️ Acerca de la Banda</h2>", unsafe_allow_html=True)
        
        # Texto de presentación
        presentacion = """
        **Twenty One Pilots** es una banda estadounidense de música alternativa formada en 2009 en Columbus, Ohio.
        
        La banda está integrada por:
        - **Tyler Joseph**: Vocalista y productor
        - **Josh Dun**: Baterista
        
        Con su estilo único que mezcla hip-hop, rock y electrónica, Twenty One Pilots se ha convertido en una de las 
        bandas más influyentes de la música contemporánea. Sus letras profundas y su energía en vivo los han llevado 
        a ganar múltiples premios y reconocimientos a nivel mundial.
        """
        
        st.markdown(presentacion)  # Mostrar el texto
    
    # ========== COLUMNA 2: DATOS INTERESANTES ==========
    with col2:
        st.markdown("<h2 style='color: #8D0000;'>🎸 Datos Interesantes</h2>", unsafe_allow_html=True)
        
        # Información adicional
        datos = """
        **Premios y Reconocimientos:**
        - Grammy Awards
        - MTV Video Music Awards
        - American Music Awards
        
        **Álbumes Principales:**
        - Vessel (2013)
        - Blurryface (2015)
        - Trench (2018)
        - Scaled and Icy (2021)
        - Clancy (2024)
        
        **Género Musical:**
        Alternative Hip-Hop / Electropop / Rock
        """
        
        st.markdown(datos)  # Mostrar los datos
    
    # Agregar separador visual
    st.markdown("---")
    
    # Sección de videos destacados con selección aleatoria
    st.markdown("<h2 style='text-align: center; color: #8D0000;'>🎬 Videos Destacados</h2>", unsafe_allow_html=True)
    
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
        "<h1 style='text-align: center; color: #8D0000;'>💿 DISCOGRAFÍA DE TWENTY ONE PILOTS</h1>",
        unsafe_allow_html=True
    )
    
    # Pequeña introducción
    st.markdown(
        "<p style='text-align: center; color: #000000; font-size: 16px;'>"
        "Explora todos los álbumes y canciones de Twenty One Pilots"
        "</p>",
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
# PÁGINA 3: MAPA DE VIDEOCLIPS (Ubicaciones de grabación)
# ============================================================================

elif pagina_seleccionada == '🗺️ Mapa':
    st.markdown(
        "<h1 style='text-align: center; color: #8D0000;'>🗺️ Mapa de Videoclips</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: #000000;'>Explora las ubicaciones de grabación de los videoclips de Twenty One Pilots.</p>",
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
# PÁGINA 3: ESTADÍSTICAS (Gráficos y análisis)
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
