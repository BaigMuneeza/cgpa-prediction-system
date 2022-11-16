import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open('../ML_CEP(CS_19015,19,61)/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def load_model():
    # with open('C:/Users/dell/Desktop/Jupyter/ML_CEP/interface.pkl', 'rb') as file:
    with open('../ML_CEP(CS_19015,19,61)/interface.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_one = data["model1"]
regressor_two = data["model2"]
regressor_three= data["model3"]

def enc_lst(lst):
            df = pd.DataFrame(lst)
            df.replace({'A+': 4.0, 'A': 4.0, 'A-':3.7, 'B+':3.4, 'B':3.0 ,'B-':2.7, 'C+':2.4, 'C':2.0, 'C-':1.7, 'D+':1.4, 'D':1.0, 'F':0.0, 'WU':0.0, 'W':0.0, 'I':0.0},inplace=True)
            lst=df[0].values.tolist()
            return lst

def predict_cgpa(df1,reg, name):
    st.subheader('')
    y_pred1 = reg.predict(df1)
    if st.button('Predict CGPA'):
        p=round(y_pred1[0], 2)
        st.write("""### Your CGPA is """, str(p))


def show_predict_page():
    st.title("CGPA Prediction Model")
    st.write("""### Find out your Final Year's CGPA using our CGPA prediction model""")
    st.subheader('')
    st.subheader('Enter Information to proceed')


    Name_usr = st.text_input('Enter your name')
    Roll_usr = st.text_input('Enter your roll number')

    year = ("First Year", "First & Second Year", "First, Second & Third Year",)
    grades = ( "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F", "WU", "W", "I", )

    Year_model = st.selectbox("Select Year", year) 

        
    if Year_model=="First Year":
            st.subheader('')
            st.write('You can now fill out your grades')
            PH_121 = st.selectbox("PH_121", grades) 
            HS_101 = st.selectbox("HS_101", grades) 
            CY_105 = st.selectbox("CY_105", grades) 
            HS_105_12 = st.selectbox("HS_105_12", grades) 
            MT_111 = st.selectbox("MT_111", grades) 
            CS_105 = st.selectbox("CS_105", grades) 
            CS_106 = st.selectbox("CS_106", grades) 
            EL_102 = st.selectbox("EL_102", grades) 
            EE_119 = st.selectbox("EE_119", grades) 
            ME_107 = st.selectbox("ME_107", grades) 
            CS_107 = st.selectbox("CS_107", grades) 
            grade_list1=[]
            for element in [PH_121, HS_101, CY_105, HS_105_12, MT_111, CS_105, CS_106, EL_102, EE_119, ME_107, CS_107]:
                grade_list1.append(element)
            grade_list1=enc_lst(grade_list1)


            grade_list2=[]
            grade_list2.append(grade_list1)
            df1 = pd.DataFrame (grade_list2, columns = ['PH-121', 'HS-101','CY-105','HS-105/12','MT-111','CS-105','CS-106','EL-102','EE-119','ME-107', 'CS-107'])
            predict_cgpa(df1, regressor_one,Name_usr )


    elif Year_model=="First & Second Year":
            st.write('You can now proceed to fill your grades')

            st.write('')
            st.write('Enter Grades for First Year')
            PH_121 = st.selectbox("PH_121", grades) 
            HS_101 = st.selectbox("HS_101", grades) 
            CY_105 = st.selectbox("CY_105", grades) 
            HS_105_12 = st.selectbox("HS_105_12", grades) 
            MT_111 = st.selectbox("MT_111", grades) 
            CS_105 = st.selectbox("CS_105", grades) 
            CS_106 = st.selectbox("CS_106", grades) 
            EL_102 = st.selectbox("EL_102", grades) 
            EE_119 = st.selectbox("EE_119", grades) 
            ME_107 = st.selectbox("ME_107", grades) 
            CS_107 = st.selectbox("CS_107", grades) 

            st.write('')
            st.write('Enter Grades for Second Year')
            st.write('')

            HS_205_20 = st.selectbox("HS_205_20", grades) 
            MT_222 = st.selectbox("MT_222", grades) 
            EE_222 = st.selectbox("EE_222", grades) 
            MT_224 = st.selectbox("MT_224", grades) 
            CS_210 = st.selectbox("CS_210", grades) 
            CS_211 = st.selectbox("CS_211", grades) 
            CS_203 = st.selectbox("CS_203", grades) 
            CS_214 = st.selectbox("CS_214", grades) 
            EE_217 = st.selectbox("EE_217", grades) 
            CS_212 = st.selectbox("CS_212", grades) 
            CS_215 = st.selectbox("CS_215", grades)
        
            grade_list1=[]
            for element in [PH_121, HS_101, CY_105, HS_105_12, MT_111, CS_105, CS_106, EL_102, EE_119, ME_107, CS_107,
            HS_205_20, MT_222,EE_222, MT_224,CS_210,CS_211,CS_203,CS_214,EE_217,CS_212,CS_215]:
                grade_list1.append(element)

            grade_list1=enc_lst(grade_list1)
            
            grade_list2=[]
            grade_list2.append(grade_list1)
            df1 = pd.DataFrame (grade_list2, columns = ['PH-121', 'HS-101','CY-105','HS-105/12','MT-111','CS-105','CS-106','EL-102','EE-119','ME-107','CS-107','HS-205/20','MT-222','EE-222','MT-224','CS-210','CS-211','CS-203','CS-214','EE-217','CS-212','CS-215'])
      
            predict_cgpa(df1, regressor_two,Name_usr )

    elif Year_model=="First, Second & Third Year":
            st.write('You can now proceed to fill your grades')
            st.write('')
            st.write('Enter Grades for First Year')
            PH_121 = st.selectbox("PH_121", grades) 
            HS_101 = st.selectbox("HS_101", grades) 
            CY_105 = st.selectbox("CY_105", grades) 
            HS_105_12 = st.selectbox("HS_105_12", grades) 
            MT_111 = st.selectbox("MT_111", grades) 
            CS_105 = st.selectbox("CS_105", grades) 
            CS_106 = st.selectbox("CS_106", grades) 
            EL_102 = st.selectbox("EL_102", grades) 
            EE_119 = st.selectbox("EE_119", grades) 
            ME_107 = st.selectbox("ME_107", grades) 
            CS_107 = st.selectbox("CS_107", grades) 

            st.write('')
            st.write('Enter Grades for Second Year')
            st.write('')

            HS_205_20 = st.selectbox("HS_205_20", grades) 
            MT_222 = st.selectbox("MT_222", grades) 
            EE_222 = st.selectbox("EE_222", grades) 
            MT_224 = st.selectbox("MT_224", grades) 
            CS_210 = st.selectbox("CS_210", grades) 
            CS_211 = st.selectbox("CS_211", grades) 
            CS_203 = st.selectbox("CS_203", grades) 
            CS_214 = st.selectbox("CS_214", grades) 
            EE_217 = st.selectbox("EE_217", grades) 
            CS_212 = st.selectbox("CS_212", grades) 
            CS_215 = st.selectbox("CS_215", grades)

            st.write('')
            st.write('Enter Grades for Third Year')
            st.write('')


            MT_331 = st.selectbox("MT_331", grades) 
            EF_303 = st.selectbox("EF_303", grades) 
            HS_304 = st.selectbox("HS_304", grades) 
            CS_301 = st.selectbox("CS_301", grades) 
            CS_302 = st.selectbox("CS_302", grades) 
            TC_383 = st.selectbox("TC_383", grades) 
            EL_332 = st.selectbox("EL_332", grades) 
            CS_318 = st.selectbox("CS_318", grades) 
            CS_306 = st.selectbox("CS_306", grades) 
            CS_312 = st.selectbox("CS_312", grades) 
            CS_317 = st.selectbox("CS_317", grades)




            grade_list1=[]
            for element in [PH_121, HS_101, CY_105, HS_105_12, MT_111, CS_105, CS_106, EL_102, EE_119, ME_107,CS_107, 
            HS_205_20, MT_222,EE_222, MT_224,CS_210,CS_211,CS_203,CS_214,EE_217,CS_212,CS_215,
            MT_331,EF_303,HS_304,CS_301,CS_302,TC_383,EL_332,CS_318,CS_306,CS_312,CS_317]:
                grade_list1.append(element)
            grade_list1=enc_lst(grade_list1)

            grade_list2=[]
            grade_list2.append(grade_list1)
            df1 = pd.DataFrame (grade_list2, columns = ['PH-121', 'HS-101','CY-105','HS-105/12','MT-111','CS-105','CS-106','EL-102','EE-119','ME-107','CS-107','HS-205/20','MT-222','EE-222','MT-224','CS-210','CS-211','CS-203','CS-214','EE-217','CS-212','CS-215','MT-331','EF-303','HS-304','CS-301','CS-302','TC-383','EL-332','CS-318','CS-306','CS-312','CS-317'])
     
            predict_cgpa(df1, regressor_three,Name_usr )

    


show_predict_page()
