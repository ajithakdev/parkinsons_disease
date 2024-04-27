import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def parkinsons_prediction(input_data):
    # Define the input data
    input_data = np.array(input_data, dtype=float)
    # Reshape the input data
    input_data_reshaped = input_data.reshape(1, -1)

    # Define and fit a StandardScaler on the input data
    scaler = StandardScaler()
    scaler.fit(input_data_reshaped)

    # Transform the input data
    std_data = scaler.transform(input_data_reshaped)

    # Make a prediction using the loaded model and the scaled input data
    prediction = loaded_model.predict(std_data)

    if prediction[0] == 0:
        return "The Person does not have Parkinson's Disease"
    else:
        return "The Person has Parkinson's"

def main():
    #sidebar for navigate
    with st.sidebar:
        selected = option_menu('Parkinsons Disease Prediction',
                                ['About parkinsons', 'Prediction', 'Contact us'],
                                icons=['file-earmark-person-fill', 'search', 'envelope'],
                                default_index=0)  # means firstly it shows index 0th code ie.,About parkinson

    # About parkinson page
    if selected == 'About parkinsons':
        # Display the content

    if selected == 'Contact us':
        # Display the content

    if selected == 'Prediction':
        # Getting the input data from the user
        st.title('Parkinson Prediction WebApp')
        # Add code for input fields

        input_data = [
            # Get input data from fields or uploaded file
        ]

        # code for prediction
        if st.button('Parkinson Test Result'):
            if input_data:
                result = parkinsons_prediction(input_data)
                st.success(result)
            else:
                st.warning('Please provide input data')

if __name__ == '__main__':
    main() 
