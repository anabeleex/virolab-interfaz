import difflib
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import plotly.figure_factory as ff
from scipy.stats.stats import pearsonr
import base64
from streamlit_image_select import image_select
import difflib
import numpy



#List of the symptoms is listed here in list l1.
l1=['manchas_marron','manchas_verde','manchas_amarillo','deformacion_hoja','clorosis','purpura_hoja','anillos_verde','anillos_amarillo','fruto_reducido','crecimiento','pardeamiento_fruto','enrollamiento','tallo_marron','menos_frutos','deformacion_fruto','necrosis','afidos','trips','nematodos','chicharrita','mosquitasb','propagacion','transmision','semillas','polen','abejorros','orosius']

#List of Diseases is listed in list disease.
disease=['AYVV','AMV','ANSV','ArMV','BCTV','CaCV','ChiLCV','CdTV','CEVd','CLVd','CMV','ETBTV','PMoV','PZSV','PepMV','PepGMV','PSTVd','PVY','TbCSV','TEV','TYDV','ToALCV','TASVd','TAV','TBRV','ToBMV','ToBRFV','TBSV','ToCLPV','ToCV','TCDVd','TCSV','ToChSV','ToCSV','ToDLV','TGMV','ToMarV','TMV','ToMMV','ToNDV','TomNSV','ToSLCV','ToSRV','TSWV','ToTV','TYLCV','TZSV','ToYVSV','ToYSV','TYRV']

sintomas = ["Manchas marrón oscuro en las hojas","Manchas verde oscuro/claro en las hojas","Manchas amarillas en las hojas","Deformación de la hoja","Clorosis","Coloración púrpura en las hojas","Presencia de anillos color verde en el fruto","Presencia de anillos color amarillo o decoloración en el fruto","Tamaño reducido del fruto","Se detiene el crecimiento de la planta","Pardeamiento del fruto","Enrollamiento de la hoja","Tallo con manchas color marrón","Disminución en el número de frutos","Deformación en el fruto","Necrosis"]

l2=[]
for i in range(0,len(l1)):
    l2.append(0)

df=pd.read_csv("VIRUS3.csv")
X= df[l1]
y = df[["Id"]]
np.ravel(y)
y2 = df["Id"].values.tolist()
y3 = df["Nombre"].values.tolist()
y4 = df["Abreviatura"].values.tolist()
X_test= df[l1]
y_test = df[["Id"]]
psymptoms = []
global y6

def show_pdf(viruscode):
    st.markdown(f'<embed src="https://drive.google.com/viewerng/viewer?embedded=true&url=https://github.com/anabeleex/virolab-interfaz/raw/main/Fichas/{viruscode}.pdf" width="700" height="700">', unsafe_allow_html=True)


def NaiveBayes(disease):
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    # print(accuracy_score(y_test, y_pred))
    # print(accuracy_score(y_test, y_pred,normalize=False))
    
    #TENGO QUE MODIFICAR COMO CONSEGUIR LOS SINTOMAS
    # psymptoms.append(l1[sintomas.index(Symptom1.get())])
    # psymptoms.append(l1[sintomas.index(Symptom2.get())])
    # psymptoms.append(l1[sintomas.index(Symptom3.get())])
    # psymptoms.append(l1[sintomas.index(Symptom4.get())])
    # psymptoms.append(l1[sintomas.index(Symptom5.get())])

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = gnb.predict(inputtest)
    # st.write(pearsonr(X_test.iloc[0:1],np.ravel(inputtest)))
    predicted=predict[0]
    h='no'

    possible = []
    for a in range(0,len(y)):
        if(predicted == y2[a]):
            h='yes'
            possible.append(a)


    if (h=='yes'):
        for g in range(0,len(possible)):
            #st.write("En base a los sintomas elegidos, la predicción principal es:")
            #st.markdown("### ***" + y3[possible[g]] + " 🌱" +"***" )
            disease = possible[g]
            #show_pdf(y4[possible[g]])
            #t3.insert(END, y3[possible[g]])
            
    else:
        st.write("Not Found")
    #     t3.delete("1.0", END)
    #     t3.insert(END, "Not Found")
    return disease

st.set_page_config(page_title="Aproximación de Detección de Virus en plantas de Tomate",page_icon="🍅",layout="centered",initial_sidebar_state="expanded")
icon = Image.open("./utils/cicese.png")
st.sidebar.image(
        icon, use_column_width=True, caption="DeteccionVirus v2.3"
    )

st.sidebar.write('## Colaboradores del proyecto:')
st.sidebar.write('**Versión 1**. Hecha por:')
st.sidebar.write('*Marco Ibrim Rodríguez Sánchez*')
st.sidebar.write('**Versión 2**. Hecha por:')
st.sidebar.write('*Anabelee Ochoa Ritchie* \n\n\n\n\n-------------------------')

st.sidebar.write("## Referencias de imágenes utilizadas:")
st.sidebar.write("Áfidos, Recuperado de: https://www.flickr.com/photos/gonzalezcarducci/5350233895")
st.sidebar.write("Trips, Recuperado de: https://www.mijardin.es/problemas/plagas/trips/")
st.sidebar.write("Nemátodos, Recuperado de: https://macrobacter.com/nematodos-parasitos-de-plantas-en-suelos-agricolas/")
st.sidebar.write("Chicharritas, Recuperado de: https://ecoregistros.org/site/imagen.php?id=305951")
st.sidebar.write("Mosquita blanca, Recuperado de: https://www.agrotox.com.ar/plagas/mosca-blanca")
st.sidebar.write("Propagación Vegetativa, Recuperado de: https://blog.gardencenterejea.com/cultivar-tomates/")
st.sidebar.write("Semillas de Tomate, Recuperado de: https://www.huertos.org/2015/09/guardando-semillas-de-tomate-por-el-metodo-de-fermentacion/")
st.sidebar.write("Polen, Recuperado de: https://es.m.wikipedia.org/wiki/Archivo:Ipomoea_purpurea_pollen.jpg")
st.sidebar.write("Abejorros, Recuperado de: https://www.redagricola.com/pe/abejorros-son-selectivos-y-memorizan-la-ubicacion-de-las-mejores-flores/")
st.sidebar.write("Orosius argentatus, Recuperado de: https://en.wikipedia.org/wiki/Common_brown_leafhopper#/media/File:Orosius_orientalis.jpg")

st.title("Sistema de Aproximación de Virus de Plantas de Tomate")
st.markdown("### Centro de Investigación Científica y de Educación Superior de Ensenada")
st.caption("Hecho por: Anabelee Ochoa Ritchie, Supervisado por: Dra. Jimena Carrillo Tripp")



form = st.form(key="annotation")
with form:
    options = st.multiselect(
        'Seleccione los síntomas presentados por su planta:',
        ["Manchas marrón oscuro en las hojas","Manchas verde oscuro/claro en las hojas","Manchas amarillas en las hojas","Deformación de la hoja","Clorosis","Coloración púrpura en las hojas","Presencia de anillos color verde en el fruto","Presencia de anillos color amarillo o decoloración en el fruto","Tamaño reducido del fruto","Se detiene el crecimiento de la planta","Pardeamiento del fruto","Enrollamiento de la hoja","Tallo con manchas color marrón","Disminución en el número de frutos","Deformación en el fruto","Necrosis"], help = "Escoja una opción...")

    submitted2 = st.form_submit_button(label="Conozco el modo de transmisión")
    submitted3 = st.form_submit_button(label="No lo conozco")

    if submitted2:
        img = image_select("Modo de transmisión:", ["./utils/afidos.jpg", "./utils/trips.jpg", "./utils/nematodos.jpg","./utils/chicharrita.jpg","./utils/mosquitasb.jpg","./utils/propagacion.jpg","./utils/transmision.jpg","./utils/semillas.jpg","./utils/polen.jpg","./utils/abejorros.jpg","./utils/orosius.png"] ,captions=["Áfidos", "Trips", "Nemátodos","Chicharritas","Mosquitas blancas","Propagación vegetativa","Transmisión mecánica","Semillas","Polen","Abejorros","Orosius argentatus"])
    

    submitted = st.form_submit_button(label="Calcular")



if submitted and options:
    for j in range(0,len(options)):
        psymptoms.append(l1[sintomas.index(options[j])])

    if submitted2:
        img = img.removesuffix('.jpg').removesuffix('.png')
        img = img.removeprefix('./utils/')
        psymptoms.append(img)
    
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    disease = NaiveBayes(disease)
    # st.bar_chart(np.sum(X_test[psymptoms],1), use_container_width=True)
    chart_data = pd.DataFrame(np.sum(X_test[psymptoms],1))


    porcentajes = {}
    for valor in range(0,len(X_test['manchas_marron'])):
        a = [str(x) for x in X_test.loc[valor]]
        b = [str(x) for x in l2]
        a_string = ''.join(a)
        b_string = ''.join(b)
        porcentajes[valor] = difflib.SequenceMatcher(None,b_string,a_string).ratio()
    
    
    porcentajes_sorted = sorted(porcentajes.items(), key=lambda x:x[1],reverse=True)
    print(porcentajes_sorted)
    print(porcentajes_sorted[0][0])
    print(porcentajes_sorted[0][1])
    print(disease)

    st.write("Se presenta el mayor porcentaje de coincidencia para los siguientes 3 virus:")


    if(disease == porcentajes_sorted[0][0]):
        col1, col2, col3 = st.columns(3)
        col1.metric(y3[porcentajes_sorted[0][0]], numpy.format_float_positional(porcentajes_sorted[0][1]*100, precision = 2) + " %")
        col2.metric(y3[porcentajes_sorted[1][0]], numpy.format_float_positional(porcentajes_sorted[1][1]*100, precision = 2) + " %")
        col3.metric(y3[porcentajes_sorted[2][0]], numpy.format_float_positional(porcentajes_sorted[2][1]*100, precision = 2) + " %")
        st.write("En base a los sintomas elegidos, las predicciones principales son:")
        st.markdown("### ***" + y3[disease] + " 🌱" +"***" )
        show_pdf(y4[disease])

        st.markdown("### ***" + y3[porcentajes_sorted[1][0]] + " 🌱" +"***" )
        show_pdf(y4[porcentajes_sorted[1][0]])

        st.markdown("### ***" + y3[porcentajes_sorted[2][0]] + " 🌱" +"***" )
        show_pdf(y4[porcentajes_sorted[2][0]])
    elif(disease == porcentajes_sorted[1][0]):
        col1, col2, col3 = st.columns(3)
        col1.metric(y3[disease], numpy.format_float_positional(porcentajes_sorted[0][1]*100, precision = 2) + " %")
        col2.metric(y3[porcentajes_sorted[2][0]], numpy.format_float_positional(porcentajes_sorted[1][1]*100, precision = 2) + " %")
        col3.metric(y3[porcentajes_sorted[3][0]], numpy.format_float_positional(porcentajes_sorted[2][1]*100, precision = 2) + " %")
        st.write("En base a los sintomas elegidos, las predicciones principales son:")
        st.markdown("### ***" + y3[disease] + " 🌱" +"***" )
        show_pdf(y4[disease])

        st.markdown("### ***" + y3[porcentajes_sorted[2][0]] + " 🌱" +"***" )
        show_pdf(y4[porcentajes_sorted[2][0]])

        st.markdown("### ***" + y3[porcentajes_sorted[3][0]] + " 🌱" +"***" )
        show_pdf(y4[porcentajes_sorted[3][0]])
    elif(disease == porcentajes_sorted[2][0]):
        col1, col2, col3 = st.columns(3)
        col1.metric(y3[disease], numpy.format_float_positional(porcentajes_sorted[0][1]*100, precision = 2) + " %")
        col2.metric(y3[porcentajes_sorted[1][0]], numpy.format_float_positional(porcentajes_sorted[1][1]*100, precision = 2) + " %")
        col3.metric(y3[porcentajes_sorted[3][0]], numpy.format_float_positional(porcentajes_sorted[2][1]*100, precision = 2) + " %")
        st.write("En base a los sintomas elegidos, las predicciones principales son:")
        st.markdown("### ***" + y3[disease] + " 🌱" +"***" )
        show_pdf(y4[disease])

        st.markdown("### ***" + y3[porcentajes_sorted[1][0]] + " 🌱" +"***" )
        show_pdf(y4[porcentajes_sorted[1][0]])

        st.markdown("### ***" + y3[porcentajes_sorted[3][0]] + " 🌱" +"***" )
        show_pdf(y4[porcentajes_sorted[3][0]])
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric(y3[disease], numpy.format_float_positional(porcentajes_sorted[0][1]*100, precision = 2) + " %")
        col2.metric(y3[porcentajes_sorted[0][0]], numpy.format_float_positional(porcentajes_sorted[1][1]*100, precision = 2) + " %")
        col3.metric(y3[porcentajes_sorted[1][0]], numpy.format_float_positional(porcentajes_sorted[2][1]*100, precision = 2) + " %")
        st.write("En base a los sintomas elegidos, las predicciones principales son:")
        st.markdown("### ***" + y3[disease] + " 🌱" +"***" )
        show_pdf(y4[disease])

        st.markdown("### ***" + y3[porcentajes_sorted[0][0]] + " 🌱" +"***" )
        show_pdf(y4[porcentajes_sorted[0][0]])

        st.markdown("### ***" + y3[porcentajes_sorted[1][0]] + " 🌱" +"***" )
        show_pdf(y4[porcentajes_sorted[1][0]])



    
    #st.write("La distribución para la base de datos completa:")
    res = {}
    for key in range(0,len(X_test[psymptoms])):
        for value in y3:
            res[key] = value
            y3.remove(value)
            break
    df_new = chart_data.rename(index=res)
    sorteddf = df_new.sort_values(by = 0, ascending=False)
    #sm=difflib.SequenceMatcher(None,s1,s2)
    #sm.ratio()


    #st.bar_chart(df_new, use_container_width= True)
    

    
    
    
    


elif submitted and not options:
    st.write("Porfavor seleccione al menos dos síntomas de la lista.")
                
        #SÍNTOMAS EN FORMA DE LISTA
            # st.write("Seleccione los síntomas presentados por su planta:")
            # st.markdown("**Defectos en las hojas:**")
            # manchas_marron = st.checkbox('Manchas marrón oscuro en las hojas')
            # manchas_verde = st.checkbox("Manchas verde oscuro/claro en las hojas")
            # manchas_amarillo = st.checkbox("Manchas amarillas en las hojas")
            # deformacion_hoja = st.checkbox("Deformación de la hoja")
            # purpura_hoja = st.checkbox("Coloración purpura de la hoja")
            # enrollamiento = st.checkbox("Enrollamiento de las hojas")

            # st.write("**Defectos en el fruto:**")
            # anillos_verde = st.checkbox("Presencia de anillos color verde en el fruto")
            # anillos_amarillo = st.checkbox("Presencia de anillos color amarillo o decoloración en el fruto")
            # fruto_reducido = st.checkbox("Tamaño reducido del fruto")
            # crecimiento = st.checkbox("Se detiene el crecimiento de la planta")
            # # deformacion_hoja = st.checkbox("Manchas amarillas en las hojas")
            # # deformacion_hoja = st.checkbox("Manchas amarillas en las hojas")
            # # deformacion_hoja = st.checkbox("Manchas amarillas en las hojas")
            # # deformacion_hoja = st.checkbox("Manchas amarillas en las hojas")
            # # deformacion_hoja = st.checkbox("Manchas amarillas en las hojas")
            # # deformacion_hoja = st.checkbox("Manchas amarillas en las hojas")
            # # deformacion_hoja = st.checkbox("Manchas amarillas en las hojas")

            # st.write("**Otros síntomas:**")
            # clorosis = st.checkbox("Clorosis")

#st.write('You selected:', options)
#def preprocess():
