import streamlit as st
import pandas as pd
st.sidebar.title("Student Data ")
st.sidebar.selectbox("select deivision",["A1","A2","A3","A4","A5"])
name=st.sidebar.text_input("Enter your Name: ")
enroll=st.sidebar.number_input("Enter your enrollment number: ")
st.header("Student Data Analysis System")
c1,c2,c3,c4,c5=st.tabs(('Python','FSD','PS','DE','result'))

with c1:
   p1=[]
   a1,a2,a3,a4=st.columns(4)
   with a1:
        t1= st.number_input("Enter your T1 marks")
   with a2:
        t2= st.number_input("Enter your T2 marks")
   with a3:
        t3= st.number_input("Enter your T3 marks")
   with a4:
        t4= st.number_input("Enter your T4 marks")
   sb=st.button("submit1")
   if sb:
       
       p1.append(t1)
       p1.append(t2)
       p1.append(t3)
       p1.append(t4)
       data={"python":p1}
       df=pd.DataFrame(data,index=["t1","t2","t3","t4"])
       st.dataframe(df)
       psm=sum(p1)
    
    
  

with c2:
   p2=[]
   a1,a2,a3,a4=st.columns(4)
   with a1:
        t1= st.number_input("Enter your FT1 marks")
   with a2:
        t2= st.number_input("Enter your FT2 marks")
   with a3:
        t3= st.number_input("Enter your FT3 marks")
   with a4:
        t4= st.number_input("Enter your FT4 marks")
   sb=st.button("submit2")
   if sb:
       p2.append(t1)
       p2.append(t2)
       p2.append(t3)
       p2.append(t4)
       psm1=sum(p2)
       
with c3:
   p3=[]
   a1,a2,a3,a4=st.columns(4)
   with a1:
        t1= st.number_input("Enter your PST1 marks")
   with a2:
        t2= st.number_input("Enter your PST2 marks")
   with a3:
        t3= st.number_input("Enter your PST3 marks")
   with a4:
        t4= st.number_input("Enter your PST4 marks")
   sb=st.button("submit3")
   if sb:
       p3.append(t1)
       p3.append(t2)
       p3.append(t3)
       p3.append(t4)
       psm2=sum(p3)
    
       
with c4:
   p4=[]
   a1,a2,a3,a4=st.columns(4)
   with a1:
        t1= st.number_input("Enter your DET1 marks")
   with a2:
        t2= st.number_input("Enter your DET2 marks")
   with a3:
        t3= st.number_input("Enter your DET3 marks")
   with a4:
        t4= st.number_input("Enter your DET4 marks")
   sb=st.button("submit4")
   if sb:
       p4.append(t1)
       p4.append(t2)
       p4.append(t3)
       p4.append(t4)
       psm3=sum(p5)
       
