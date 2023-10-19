import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Model.pkl")
inputs = joblib.load("inputs.pkl")
def prediction(surgery,age,rectal_temp,pulse,respiratory_rate,temp_of_extremities,peripheral_pulse,mucous_membrane,capillary_refill_time,pain,peristalsis,abdominal_distention,nasogastric_tube,nasogastric_reflux,nasogastric_reflux_ph,rectal_exam_feces,abdomen,packed_cell_volume, total_protein,abdomo_appearance, abdomo_protein, surgical_lesion, lesion_1,cp_data):
    df = pd.DataFrame(columns=inputs)
    df.at[0,'surgery'] =surgery
    df.at[0,'age'] =age
    df.at[0,'rectal_temp'] =rectal_temp
    df.at[0,'pulse'] =pulse
    df.at[0,'respiratory_rate'] =respiratory_rate
    df.at[0,'temp_of_extremities'] =temp_of_extremities
    df.at[0,'peripheral_pulse'] =peripheral_pulse
    df.at[0,'mucous_membrane'] =mucous_membrane
    df.at[0,'capillary_refill_time'] =capillary_refill_time
    df.at[0,'pain'] =pain
    df.at[0,'peristalsis'] =peristalsis
    df.at[0,'abdominal_distention'] =abdominal_distention
    df.at[0,'nasogastric_tube'] =nasogastric_tube
    df.at[0,'nasogastric_reflux'] =nasogastric_reflux
    df.at[0,'nasogastric_reflux_ph'] =nasogastric_reflux_ph
    df.at[0,'rectal_exam_feces'] =rectal_exam_feces
    df.at[0,'abdomen'] =abdomen
    df.at[0,'packed_cell_volume'] =packed_cell_volume
    df.at[0,'total_protein'] =total_protein
    df.at[0,'abdomo_appearance'] =abdomo_appearance
    df.at[0,'abdomo_protein'] =abdomo_protein
    df.at[0,'surgical_lesion'] =surgical_lesion
    df.at[0,'lesion_1'] =lesion_1
    df.at[0,'cp_data'] =cp_data
    res = model.predict(df)
    return res[0]


def main() :
    st.title("Health check of Horses")
    age= st.selectbox("Age" , ['adult' ,'young'])
    surgery = st.selectbox("Surgery ?" , ['yes', 'no'] )
    rectal_temp = st.slider("Rectal temperature" , min_value=35.0,max_value=41.0,step = 0.1 , value = 38.0)
    pulse = st.slider("Pulse" , min_value=30,max_value=185,step = 1 , value = 75)
    respiratory_rate = st.slider("Respiratory rate" ,min_value=7,max_value=97,step = 1 , value = 36)
    temp_of_extremities = st.selectbox("Temperature of extremities", ['cool' ,'cold' ,'normal', 'warm' ])
    peripheral_pulse = st.selectbox("Peripheral pulse",['reduced', 'normal', 'None','absent'])
    mucous_membrane = st.selectbox("Mucous membrane", ['dark_cyanotic','pale_cyanotic','pale_pink','normal_pink','bright_pink','bright_red'])
    capillary_refill_time = st.selectbox("Capillary refill time",['more_3_sec','less_3_sec'])
    pain = st.selectbox("Pain",['depressed','mild_pain','extreme_pain','alert','severe_pain'] )
    peristalsis= st.selectbox("Peristalsis",['absent','hypomotile','normal','hypermotile'])
    abdominal_distention = st.selectbox("Abdominal distention",['slight','moderate','none','severe'])
    nasogastric_tube = st.selectbox("Nasogastric tube",['slight','none','significant'])
    nasogastric_reflux = st.selectbox("Nasogastric reflux",['less_1_liter','more_1_liter','none'])
    nasogastric_reflux_ph = st.slider("Nasogastric reflux PH",min_value=0.0,max_value=8.0,step = 0.1 , value = 4.0)
    rectal_exam_feces = st.selectbox("Rectal examination feces",['decreased','absent','normal','increased' ])
    abdomen= st.selectbox("Abdomen",['distend_small','distend_large','normal','firm','other'])
    packed_cell_volume= st.slider("Packed cell volume",min_value=22,max_value=76,step = 1 , value = 57)
    total_protein = st.slider("total protein",min_value=3.0,max_value=90.0,step = 0.1 , value = 7.5)
    abdomo_appearance=st.selectbox("Abdominocentesis appearance",['serosanguious','cloudy','clear'])
    abdomo_protein=st.slider("Abdomcentesis total protein",min_value=0.0,max_value=10.0,step = 0.1 , value = 2.0)
    surgical_lesion = st.selectbox("surgical lesion ?" , ['yes' ,'no'])
    lesion_1 = st.selectbox("Type of lesion", [ 2209,2208,5124,0,3111,2207,3209,3205,2124,2206,31110,2205,7111,3207,4206,2113,3113,2112,4205,8300,1400,5400,7209,3115,11124,4207,9400,300,2111,3300,3112,400,2300,2322,3133,4300,3025,8400,1111,5206,11300,4124,12208,6112,7400,5000,5205,2202,3124,5111,6209,11400,6111,2305,21110,1124,41110])
    cp_data =st.selectbox("is pathology data present for this case ?", ['yes' ,'no'])
    if st.button("Predict"):
        result = prediction(surgery,age,rectal_temp,pulse,respiratory_rate,temp_of_extremities,peripheral_pulse,mucous_membrane,capillary_refill_time,pain,peristalsis,abdominal_distention,nasogastric_tube,nasogastric_reflux,nasogastric_reflux_ph,rectal_exam_feces,abdomen,packed_cell_volume, total_protein,abdomo_appearance, abdomo_protein, surgical_lesion, lesion_1,cp_data)
        res_list = ['died','euthanized','lived']
        st.text(res_list[result])
main()
