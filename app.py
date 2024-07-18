import streamlit as st
import pandas as pd
from insurancePP.pipeline.prediction import PredictionPipeline
import asyncio
from insurancePP.logging import logger
import os


st.title('Insurance Premium Prediction')

# async def async_task():
#     # executing main.py
#     try:
#         os.system("python main.py")
#         logger.info("Training Successful!")
#     except Exception as e:
#         logger.info(f"Error occured {e}")



def main():
    
    def callback_search():
        #   Destroying old sessions
        st.session_state['search_btn'] = False

    # Extracting features from the webpage
    # capturing the selected age
    option_age = st.selectbox(
            'select the age',
            [i for i in range(15, 65)],
            on_change=callback_search
        )
    # print(option_age)

    # capturing the selected gender
    option_gender = st.selectbox(
            'select the gender',
            ['female', 'male'],
            on_change=callback_search
        )

    option_bmi = st.text_input(
            'enter the bmi (values should be in range 15-60)',
            on_change=callback_search
        )


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
            ['yes', 'no'],
            on_change=callback_search
        )
    # print(option_smoker)

    # capturing the region
    option_region = st.selectbox(
            'select the region',
            ['southwest', 'southeast', 'northwest', 'northeast'],
            on_change=callback_search
        )


    custom_data = {
        'age': [option_age],
        'sex': [option_gender],
        'bmi': [option_bmi],
        'children': [option_children],
        'smoker': [option_smoker],
        'region': [option_region]
    }



    prediction = st.button('Predict')
    # adding session state for 'prediction' button
    if st.session_state.get('search_btn') != True:
        st.session_state['search_btn'] = prediction

    # prediction and printing the output
    if st.session_state['search_btn']:
        data_df = pd.DataFrame(custom_data)
        data_df['bmi'] = data_df['bmi'].astype(float)

        # print(data_df.dtypes)
        pipe = PredictionPipeline()
        result = pipe.predicting_result(data_df)
        st.write('The Predicted Expense is: ')
        st.write(result)

if __name__ == '__main__':
   
    os.system("python main.py")
    logger.info("Training Successful!")
    main()

