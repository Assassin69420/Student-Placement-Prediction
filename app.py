import streamlit as st
import pandas as pd

count=0
st.write("""# STUDENT PLACEMENT PREDICTION
""")
name = st.text_input("Enter your Name")
CGPA = st.number_input("Enter your CGPA",min_value=0.0,max_value=10.0)
st.write("Branch")

if st.checkbox('CSE',key=3):
    st.checkbox('ME',disabled=True,key=4)
elif st.checkbox('ME'):
    st.checkbox('CSE',disabled=True,key=3)

if st.button('submit'):
    count=489
    dcount=512
    res=(float(CGPA)/10)*count/dcount*100
    st.write('# PREDICTION')
    st.write("Your Placement Chances are : ",res,'%')