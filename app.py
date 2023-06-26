# importing dependencies
import pickle
import streamlit as st
import pandas as pd

# reading binary files (trained label encoders and model file)
le_gender = pickle.load(open('le_gender.pkl', 'rb'))
le_region = pickle.load(open('le_region.pkl', 'rb'))
le_smoker = pickle.load(open('le_smoker.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Insurance Premium Prediction')

# saving label encoder keys to present it in user interface
le_gender_mapping = dict(zip(le_gender.classes_, le_gender.transform(le_gender.classes_)))
le_smoker_mapping = dict(zip(le_smoker.classes_, le_smoker.transform(le_smoker.classes_)))
le_region_mapping = dict(zip(le_region.classes_, le_region.transform(le_region.classes_)))
# print(le_name_mapping.keys())
def callback_search():
    #   Destroying old sessions
    st.session_state['search_btn'] = False

# capturing the selected age
option_age = st.selectbox(
        'select the age',
        [i for i in range(15, 80)],
        on_change=callback_search
    )
# print(option_age)

# capturing the selected gender
option_gender = st.selectbox(
        'select the gender',
        le_gender_mapping.keys(),
        on_change=callback_search
    )
option_gender = le_gender.transform([option_gender])[0]
# print(option_gender)

# capturing the bmi
option_bmi = st.text_input(
        'enter the bmi',
        on_change=callback_search
    )
# print(option_bmi)

# capturing the number of children
option_children = st.selectbox(
        'select number of children',
        [i for i in range(6)],
        on_change=callback_search
    )
# print(option_children)

# capturing the smoker
option_smoker = st.selectbox(
        'is the candidate smoker',
        le_smoker_mapping.keys(),
        on_change=callback_search
    )
option_smoker = le_smoker.transform([option_smoker])[0]
# print(option_smoker)

# capturing the region
option_region = st.selectbox(
        'select the region',
        le_region_mapping.keys(),
        on_change=callback_search
    )
option_region = le_region.transform([option_region])[0]
# print(option_region)

prediction = st.button('Predict')

# adding session state fot 'prediction' button
if st.session_state.get('search_btn') != True:
    st.session_state['search_btn'] = prediction

# prediction and printing the output
if st.session_state['search_btn']:
    st.write('The Predicted Expense is: ')
    st.write(model.predict([[option_age, option_gender, option_bmi, option_children, option_smoker, option_region]])[0])