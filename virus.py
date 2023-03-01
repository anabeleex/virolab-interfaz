import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import plotly.figure_factory as ff
from scipy.stats.stats import pearsonr
import base64


#List of the symptoms is listed here in list l1.
l1=['manchas_marron','manchas_verde','manchas_amarillo','deformacion_hoja','clorosis','purpura_hoja',
'anillos_verde','anillos_amarillo','fruto_reducido','crecimiento','pardeamiento_fruto','enrollamiento',
'tallo_marron','menos_frutos','deformacion_fruto','necrosis']

#List of Diseases is listed in list disease.
disease=['AYVV','AMV','ANSV','ArMV','BCTV','CaCV','ChiLCV','CdTV','CEVd','CLVd','CMV','ETBTV','PMoV','PZSV','PepMV','PepGMV','PSTVd','PVY','TbCSV','TEV','TYDV','ToALCV','TASVd','TAV','TBRV','ToBMV','ToBRFV','TBSV','ToCLPV','ToCV','TCDVd','TCSV','ToChSV','ToCSV','ToDLV','TGMV','ToMarV','ToMIMV','ToMMoV','TMV','ToNDV','TomNSV','ToSLCV','ToSRV','TSWV','ToTV','TYLCV','TuYV','TZSV','ToYVSV','ToYSV','TYRV']

sintomas = ["Manchas marrón oscuro en las hojas","Manchas verde oscuro/claro en las hojas","Manchas amarillas en las hojas","Deformación de la hoja","Clorosis","Coloración púrpura en las hojas","Presencia de anillos color verde en el fruto","Presencia de anillos color amarillo o decoloración en el fruto","Tamaño reducido del fruto","Se detiene el crecimiento de la planta","Pardeamiento del fruto","Enrollamiento de la hoja","Tallo con manchas color marrón","Disminución en el número de frutos","Deformación en el fruto","Necrosis"]

l2=[]
for i in range(0,len(l1)):
    l2.append(0)

df=pd.read_csv("VIRUS2.csv")
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

def show_pdf(file_path):
    with open(file_path,"rb") as f:
          base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

def NaiveBayes():
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
            st.write("En base a los sintomas elegidos, la predicción principal es:")
            st.markdown("### ***" + y3[possible[g]] + " 🌱" +"***" )
            show_pdf("./Fichas/" + y4[possible[g]]+ ".pdf")
    #         t3.insert(END, y3[possible[g]])
            
    else:
        st.write("Not Found")
    #     t3.delete("1.0", END)
    #     t3.insert(END, "Not Found")

st.set_page_config(page_title="Detección de Virus en plantas de Tomate",page_icon="🍅",layout="centered",initial_sidebar_state="expanded")
icon = Image.open("./utils/cicese.png")
st.sidebar.image(
        icon, use_column_width=True, caption="DeteccionVirus v1.2"
    )

st.title("Sistema de Detección de Plantas de Tomate")
st.markdown("### Centro de Investigación Científica y de Educación Superior de Ensenada")
st.caption("Hecho por: Anabelee Ochoa Ritchie, Supervisado por: Dra. Jimena Carrillo Tripp")



form = st.form(key="annotation")
with form:
    options = st.multiselect(
        'Seleccione los síntomas presentados por su planta:',
        ["Manchas marrón oscuro en las hojas","Manchas verde oscuro/claro en las hojas","Manchas amarillas en las hojas","Deformación de la hoja","Clorosis","Coloración púrpura en las hojas","Presencia de anillos color verde en el fruto","Presencia de anillos color amarillo o decoloración en el fruto","Tamaño reducido del fruto","Se detiene el crecimiento de la planta","Pardeamiento del fruto","Enrollamiento de la hoja","Tallo con manchas color marrón","Disminución en el número de frutos","Deformación en el fruto","Necrosis"], help = "Escoja una opción...")
        
    submitted = st.form_submit_button(label="Calcular")

if submitted and options:
    for j in range(0,len(options)):
        psymptoms.append(l1[sintomas.index(options[j])])
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    NaiveBayes()
    # st.bar_chart(np.sum(X_test[psymptoms],1), use_container_width=True)
    chart_data = pd.DataFrame(np.sum(X_test[psymptoms],1))
    res = {}
    for key in range(0,len(X_test[psymptoms])):
        for value in y3:
            res[key] = value
            y3.remove(value)
            break
    df_new = chart_data.rename(index=res)
    st.bar_chart(df_new, use_container_width= True)
    
    
    


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




