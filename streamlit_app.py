import streamlit as st
import base64 

import ppt2rise
import helpers

# Config page
st.set_page_config(page_title="PPT2RISE", 
                   page_icon=":sunrise:", 
                   layout='centered', 
                   initial_sidebar_state='auto')

# Create a title + explanation
st.title(":night_with_stars: PPT2 A RISE :city_sunrise:")
st.write("Selecciona una presentación en formato pptx y obtén una versión equivalente en formato jupyter notebook + extensión RISE.")

st.header("Acciones")
# Button for loading the ppt
upload_text = "Cargar un archivo pptx"
uploaded_file = st.file_uploader(upload_text)

# Work and use a progress bar
if uploaded_file: # and uploaded_file.name.endswith("ppt"):
    # Create a custom named folder to work on 
    ppt_basename =  uploaded_file.name.replace(".pptx", "")
    basedir = helpers.create_custom_folder(ppt_basename)
    # Name conventions
    # Fix for ppt and pptx
    ppt_filename = uploaded_file.name
    ppt_basedir  = basedir + "/ppt"
    ppt_filepath = ppt_basedir + "/" + uploaded_file.name
    ipy_filename = ppt_basename + ".ipynb"
    ipy_basedir  = basedir + "/ipynb"
    ipy_filepath = ipy_basedir + "/" + ipy_filename
    zip_filename = ppt_basename + ".zip"
    zip_basedir = basedir + "/zip"
    zip_filepath = zip_basedir + "/" + zip_filename
    # Save the file
    with open(ppt_filepath, "wb") as f:
       f.write(uploaded_file.read())
    # Convert the file
    ppt2rise.ppt2rise(ppt_filepath, ipy_filepath)
    # Zip the folder
    helpers.make_archive(ipy_basedir, zip_filepath)
    # Congratulate on finish
    st.balloons()
    # Download button
    #zip_filename = zip_filepath = "simple.zip"
    # Offer a download path
    style = 'color:black;text-decoration:inherit'
    with open(zip_filepath, "rb") as f:
        bytes = f.read()
        b64 = base64.b64encode(bytes).decode()
        download_text = "Download zipped jupyter + RISE notebook"
        href = f'<a style="{style}" href="data:file/zip;base64,{b64}" download=\'{zip_filename}\'>{download_text}</a>'
        button = f'<div style="align:center"> <button class="css-qbe2hs" type="submit">{href}</button> </div>'
        st.markdown(button, unsafe_allow_html=True)

st.header("Documentación")
with st.beta_expander("¿Qué es todo esto?"):
    st.write("**¿Qué es esta página?**")
    st.write("Es un servicio para convertir una presentación en formato pptx (Powerpoint - Microsoft Office) a jupyter notebook con la extensión RISE. No es perfecto, pero ayuda enormemente a obtener una versión inicial con textos e imágenes.")
    st.write("**¿Qué es jupyter notebook?**")
    st.write("Es un formato que permite desarrollar código de manera interactiva, para distintos lenguajes: Julia, Python y R, entre otros.") 
    st.write("**¿Qué es la extensión RISE?**")
    st.write("Es una extensión para Jupyter Notebook que permite **presentar** el notebook como una presentación a pantalla completa. De esa manera, es posible presentar en charlas, conferencias o clases mostrando y ejecutando código. ¡Ya no es necesario pegar pantallazos de código!") 

with st.beta_expander("Ejemplos"):
    st.image("rise.gif")

with st.beta_expander("FAQ - Preguntas frecuentes"):
    st.write("**¿Cómo funciona?**")
    st.write("La verdad es más sencillo de lo que parece. Una librería de python llamada python-pptx permite (entre otras cosas) abrir los archivos pptx, con lo cual se extrae su contenido y se guarda en el formato requerido para jupyter notebook y la extensión RISE.")
    st.write("**¿Porqué complicarse la vida?**")
    st.write("El formato jupyter notebook + extensión RISE tiene muchas ventajas:")
    st.write("""
* Interactividad. Es posible ejecutar código en directo, sin cambiar a un terminal.
* Autocontenido. Datos, código y presentación quedan en un mismo archivo y repositorio. Es más fácil de compartir.
* Múltiples formatos. Puedes compartir la presentación como un archivo ipynb para que otros exploren interactivamente, o como una presentación en formato html, o como un pdf.
* Es software libre. No tiene costo.""")
    st.write("**¿Cómo lo utilizo?**")
    st.write("Está muy bien explicado en la página de RISE, pero en resumen, tienes que primero instalar rise")
    st.code("pip install RISE")
    st.write("luego iniciar el jupyter notebook:")
    st.code("jupyter notebook")
    st.write("Finalmente abrir el notebook y lanzar la presentación.")

with st.beta_expander("Enlaces"):
    st.write("* [Documentación oficial de RISE](https://rise.readthedocs.io/)")
    st.write("* [Documentación oficial de Streamlit (inglés)](https://streamlit.io/)")  
    st.write("* [Tutorial de RISE](https://sebastiandres.github.io/blog/tutorial-rise/)")