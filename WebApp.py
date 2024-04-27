#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler

# Load the saved model

loaded_model = pickle.load(open('trained_model.sav', 'rb'))


def parkinsons_prediction(input_data):
    input_data = np.array(input_data, dtype=float)
    input_data_reshaped = input_data.reshape(1, -1)
    scaler = StandardScaler()
    scaler.fit(input_data_reshaped)
    std_data = scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(std_data)
    if prediction[0] == 0:
        return "The Person does not have Parkinson's Disease"
    else:
        return "The Person has Parkinson's"


def main():
    with st.sidebar:
        selected = option_menu('Parkinsons Disease Prediction',
                               ['About parkinsons', 'Prediction',
                               'Contact us'],
                               icons=['file-earmark-person-fill',
                               'search', 'envelope'], default_index=0)

           # means firstly it shows index 0th code ie.,About parkinson

    # About parkinson page

    if selected == 'About parkinsons':
        st.markdown("""
<h1 style='font-family: Comic Sans MS,Courier;font-size: 25px;'>About Parkinson's Diseases</h1>
""",
                    unsafe_allow_html=True)

       # Display the paragraph and image side by side
       # Create two columns

        (col1, col2) = st.columns([3, 1])

# Add content to the columns

        with col1:

            # Add the paragraph with custom font name and font size

            st.write("""
<p style='font-family: Comic Sans MS,Courier; font-size: 16px;'>
Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder also may cause stiffness or slowing of movement.
In the early stages of Parkinson's disease, your face may show little or no expression. Your arms may not swing when you walk. Your speech may become soft or slurred. Parkinson's disease symptoms worsen as your condition progresses over time.
Although Parkinson's disease can't be cured, medicines might significantly improve your symptoms. Occasionally, a health care professional may suggest surgery to regulate certain regions of your brain and improve your symptoms.
</p>
""",
                     unsafe_allow_html=True)

        with col2:
            st.image('pd.png',
                     width=360)

        st.markdown("""
<div style='font-family: Comic Sans MS, Courier; font-size: 16px;'>
<b style='font-size: 24px;'>Symptoms</b>

- **Tremor:** Rhythmic shaking, called tremor, usually begins in a limb, often your hand or fingers. You may rub your thumb and forefinger back and forth. This is known as a pill-rolling tremor. Your hand may tremble when it's at rest. The shaking may decrease when you are performing tasks.

- **Slowed movement (bradykinesia):** Over time, Parkinson's disease may slow your movement, making simple tasks difficult and time-consuming. Your steps may become shorter when you walk. It may be difficult to get out of a chair. You may drag or shuffle your feet as you try to walk.

- **Rigid muscles:** Muscle stiffness may occur in any part of your body. The stiff muscles can be painful and limit your range of motion.

- **Impaired posture and balance:** Your posture may become stooped. Or you may fall or have balance problems as a result of Parkinson's disease.

- **Loss of automatic movements:** You may have a decreased ability to perform unconscious movements, including blinking, smiling, or swinging your arms when you walk.

- **Speech changes:** You may speak softly or quickly, slur, or hesitate before talking. Your speech may be more of a monotone rather than have the usual speech patterns.

- **Writing changes:** It may become hard to write, and your writing may appear small.


<b style='font-size: 24px;'>When to see a doctor:</b><br>
See a health care professional if you have any of the symptoms associated with Parkinson's disease \xe2\x80\x94 not only to diagnose your condition but also to rule out other causes for your symptoms.
</div>
""",
                    unsafe_allow_html=True)

        st.markdown("""
  <div style='font-family: Comic Sans MS, Courier; font-size: 16px;'>
  <b style='font-size: 24px;'>Prevention</b><br>
There are no proven ways to prevent the disease.

Some research has shown that regular aerobic exercise might reduce the risk of Parkinson's disease.

Some other research has shown that people who consume caffeine \xe2\x80\x94 which is found in coffee, tea and cola \xe2\x80\x94 get Parkinson's disease less often than those who don't drink it. Green tea also is related to a reduced risk of developing Parkinson's disease. However, it is still not known whether caffeine protects against getting Parkinson's or is related in some other way. Currently there is not enough evidence to suggest that drinking caffeinated beverages protects against Parkinson's.
  </div>
  """,
                    unsafe_allow_html=True)

    if selected == 'Contact us':

        st.markdown("""
<h1 style='font-family: Comic Sans MS,Courier;font-size: 25px;'>Contact Us</h1>
""",
                    unsafe_allow_html=True)
        st.write('Please enter your <span style="font-family: Comic Sans MS, Courier; font-size: 16px;">contact information</span> below:'
                 , unsafe_allow_html=True)

        name = st.text_input('Name')
        email = st.text_input('Email')
        message = st.text_area('Message', height=200)

        if st.button('Submit'):

        # Process the contact information (e.g., send an email, store in a database, etc.)

            st.success('Thank you for your message! We will get back to you soon.'
                       )

    if selected == 'Prediction':

        # Getting the input data from the user

        st.title('Parkinson Prediction WebApp')

        (col1, col2, col3, col4, col5) = st.columns(5)

        with col1:
            MDVP_Fo_Hz = st.text_input('Enter MDVP:Fo(Hz)')
        with col2:
            MDVP_Fhi_Hz = st.text_input('Enter MDVP:Fhi(Hz)')
        with col3:
            MDVP_Flo_Hz = st.text_input('Enter MDVP:Flo(Hz)')
        with col4:
            MDVP_Jitter_percent = st.text_input('Enter MDVP:Jitter(%)')
        with col5:
            MDVP_Jitter_Abs = st.text_input('Enter MDVP:Jitter(Abs)')
        with col1:
            MDVP_RAP = st.text_input('Enter MDVP:RAP')
        with col2:
            MDVP_PPQ = st.text_input('Enter MDVP:PPQ')
        with col3:
            Jitter_DDP = st.text_input('Enter Jitter:DDP')
        with col4:
            MDVP_Shimmer = st.text_input('Enter MDVP:Shimmer')
        with col5:
            Shimmer_dB = st.text_input('Enter Shimmer:dB')
        with col1:
            Shimmer_APQ3 = st.text_input('Enter Shimmer:APQ3')
        with col2:
            Shimmer_APQ5 = st.text_input('Enter Shimmer:APQ5')
        with col3:
            MDVP_APQ = st.text_input('Enter MDVP:APQ')
        with col4:
            Shimmer_DDA = st.text_input('Enter Shimmer:DDA')
        with col5:
            NHR = st.text_input('Enter NHR')
        with col1:
            HNR = st.text_input('Enter HNR')
        with col2:
            RPDE = st.text_input('Enter RPDE')
        with col3:
            DFA = st.text_input('Enter DFA')
        with col4:
            spread1 = st.text_input('Enter spread1')
        with col5:
            spread2 = st.text_input('Enter spread2')
        with col1:
            D2 = st.text_input('Enter D2')
        with col2:
            PPE = st.text_input('Enter PPE')
        st.text('Or')
        datas = st.file_uploader('File Uploader...')

        # code for prediction

        if st.button('Parkinson Test Result'):
            input_data = [
                MDVP_Fo_Hz,
                MDVP_Fhi_Hz,
                MDVP_Flo_Hz,
                MDVP_Jitter_percent,
                MDVP_Jitter_Abs,
                MDVP_RAP,
                MDVP_PPQ,
                Jitter_DDP,
                MDVP_Shimmer,
                Shimmer_dB,
                Shimmer_APQ3,
                Shimmer_APQ5,
                MDVP_APQ,
                Shimmer_DDA,
                NHR,
                HNR,
                RPDE,
                DFA,
                spread1,
                spread2,
                D2,
                PPE,
                ]

            if any(not value for value in input_data):
                st.error('Please provide data for all input fields.')
            else:
                input_data = [float(value) for value in input_data]  # Convert to floats
                prediction_message = parkinsons_prediction(input_data)

                if prediction_message \
                    == "The Person does not have Parkinson's Disease":
                    no_parkinsons_page()
                else:
                    st.success(prediction_message)


def no_parkinsons_page():
    st.title("Great News! You Don't Have Parkinson's Disease")

    st.balloons()  # Celebrate the good news!

    st.write("We are thrilled to share this positive outcome with you. While you don't have Parkinson's, it's always important to prioritize your health and well-being."
             )

    st.header('Tips for Maintaining a Healthy Lifestyle:')

    # Use columns for better organization

    (col1, col2) = st.columns(2)

    with col1:
        st.write('- Engage in regular physical activity: Aim for at least 150 minutes of moderate-intensity exercise or 75 minutes of vigorous-intensity exercise per week. Find activities you enjoy, such as brisk walking, swimming, or dancing.'
                 )

        st.write('- Prioritize a balanced and nutritious diet: Focus on whole foods like fruits, vegetables, whole grains, and lean protein. Limit processed foods, sugary drinks, and unhealthy fats.'
                 )

    with col2:
        st.write('- Get enough sleep: Aim for 7-8 hours of quality sleep each night. Establish a regular sleep schedule and create a relaxing bedtime routine.'
                 )
        st.write('- Manage stress effectively: Practice relaxation techniques like deep breathing, meditation, or yoga. Engage in activities you find enjoyable and spend time with loved ones.'
                 )

    st.header('Additional Resources:')

    st.write('Here are some reliable sources for health information and support:'
             )
    st.write('- World Health Organization (WHO): https://www.who.int/')
    st.write('- Centers for Disease Control and Prevention (CDC): https://www.cdc.gov/'
             )

    # ... (Add more resources as needed) ...

    st.write('Remember, maintaining a healthy lifestyle is an ongoing journey. By incorporating these suggestions and staying informed, you can continue to prioritize your well-being and reduce your risk of future health issues.'
             )


if __name__ == '__main__':
    main()
