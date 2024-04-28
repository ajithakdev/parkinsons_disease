#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler

# Load the saved model

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# loaded scaller 
#loaded_scaler = pickle.load(open('trained_scaler.pkl', 'rb'))

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
        #return "The Person has Parkinson's"
        return "The Person does not have Parkinson's Disease"


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
            

        st.text("Or")
        uploaded_file = st.file_uploader('File Uploader...')  # Single file uploader 

        # code for prediction
        if st.button('Parkinson Test Result'):
            if uploaded_file is not None:
                try:
                    df = pd.read_csv(uploaded_file)
                    input_data = df.iloc[0].tolist()
                except Exception as e:
                    st.error("Error processing file: %s" % e)
                    return
            else:
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
                    == "The Person has Parkinson's":
                    early_stage_parkinsons_page()
                else:
                    #st.success(prediction_message)
                    no_parkinsons_page()
            
 #          if any(not value for value in input_data):
  #              st.error("Please provide data for all input fields or upload a CSV file.")
   #         else:
    #            input_data = [float(value) for value in input_data]
     #           input_data_reshaped = np.array(input_data).reshape(1, -1)
      #          std_data = loaded_scaler.transform(input_data_reshaped)  # Use the loaded scaler
       #     
        #        prediction_message = parkinsons_prediction(std_data)  # Make prediction on scaled dat
#
#
 #               if prediction_message == "The Person does not have Parkinson's Disease":
  #                  no_parkinsons_page()
   #             else:
    #                st.success(prediction_message) 


# Below code is for if NO Parkinson 
import streamlit as st

def no_parkinsons_page():
    st.title("Great News! You Don't Have Parkinson's Shit 😀 But ")

    st.balloons()  # Celebrate the good news!

    st.markdown("""
        <div style='font-size: 18px; color: green; text-align: center;'>
            We are thrilled to share this positive outcome with you. While you don't have Parkinson's, it's always important to prioritize your health and well-being.
        </div>
    """, unsafe_allow_html=True)

    st.header('Tips for Maintaining a Healthy Lifestyle:')

    # Use columns for better organization
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            <h3 style='color: #007bff;'>Engage in Regular Physical Activity</h3>
            <p>Aim for at least 150 minutes of moderate-intensity exercise or 75 minutes of vigorous-intensity exercise per week. Find activities you enjoy, such as brisk walking, swimming, or dancing.</p>
        """, unsafe_allow_html=True)

        st.write("""
            <h3 style='color: #007bff;'>Prioritize a Balanced Diet</h3>
            <p>Focus on whole foods like fruits, vegetables, whole grains, and lean protein. Limit processed foods, sugary drinks, and unhealthy fats.</p>
        """, unsafe_allow_html=True)

    with col2:
        st.write("""
            <h3 style='color: #007bff;'>Get Enough Sleep</h3>
            <p>Aim for 7-8 hours of quality sleep each night. Establish a regular sleep schedule and create a relaxing bedtime routine.</p>
        """, unsafe_allow_html=True)

        st.write("""
            <h3 style='color: #007bff;'>Manage Stress Effectively</h3>
            <p>Practice relaxation techniques like deep breathing, meditation, or yoga. Engage in activities you find enjoyable and spend time with loved ones.</p>
        """, unsafe_allow_html=True)

    st.header('Additional Resources:')

    st.write("""
        <p>Here are some reliable sources for health information and support:</p>
        <ul>
            <li><a href='https://www.who.int/' target='_blank'>World Health Organization (WHO)</a></li>
            <li><a href='https://www.cdc.gov/' target='_blank'>Centers for Disease Control and Prevention (CDC)</a></li>
            <li><a href='https://www.mayoclinic.org/' target='_blank'>Mayo Clinic</a></li>
            <!-- Add more resources as needed -->
        </ul>
    """, unsafe_allow_html=True)

    st.header('Relaxing Quotes:')
    st.markdown("""
        <blockquote style='font-size: 40px; text-align: center;'>
            "The greatest wealth is health." <br>
            <em>- Virgil</em>
        </blockquote>
    """, unsafe_allow_html=True)

    st.header('Encouraging Video:')
    st.markdown("""
        <div style='text-align: center;'>
            <iframe width="560" height="315" src="https://www.youtube.com/watch?v=ZXKw-7wHiz8" frameborder="0" allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)
    st.write("Watch this video for more encouragement and information.")

    st.write("""
        <p style='color: #007bff; text-align: center;'>
            Remember, maintaining a healthy lifestyle is an ongoing journey. By incorporating these suggestions and staying informed, you can continue to prioritize your well-being and reduce your risk of future health issues.
        </p>
    """, unsafe_allow_html=True)

# Test the function
#no_parkinsons_page()

# Below code is for if Parkinson result 
def early_stage_parkinsons_page():
    st.title("You Have Early Stage Parkinson's Disease")

    st.image('1234.png', width=200)  # Add an image for emotional connection

    st.markdown("""
    <div style='font-size: 18px; color: #FF5733; text-align: center;'>
    <b>We understand that receiving this diagnosis can be concerning, but it's important to know that early-stage Parkinson's can be manageable with proper care and support.</b>
    </div>
    """, unsafe_allow_html=True)

    # Add colorful and animated elements
    st.markdown("""
    <div style='font-size: 16px; color: #0066CC; text-align: center;'>
    <b>What You Can Do:</b>
    </div>
    """, unsafe_allow_html=True)

    # Animated checklist
    st.markdown("""
    <div style='display: flex; justify-content: center;'>
    <ul>
        <li style='color: #009900; font-size: 16px; animation: fadeIn 1s ease-in-out;'>
        <span style='margin-right: 10px;'>&#10003;</span> Consult a Specialist: Schedule an appointment with a neurologist or movement disorder specialist to discuss treatment options.
        </li>
        <li style='color: #009900; font-size: 16px; animation: fadeIn 1s ease-in-out 0.5s;'>
        <span style='margin-right: 10px;'>&#10003;</span> Medication Management: Follow your doctor's instructions for prescribed medications.
        </li>
        <li style='color: #009900; font-size: 16px; animation: fadeIn 1s ease-in-out 1s;'>
        <span style='margin-right: 10px;'>&#10003;</span> Physical Therapy: Engage in exercises to improve mobility and strength.
        </li>
        <li style='color: #009900; font-size: 16px; animation: fadeIn 1s ease-in-out 1.5s;'>
        <span style='margin-right: 10px;'>&#10003;</span> Speech Therapy: Consider sessions to maintain clear communication.
        </li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size: 16px; color: #0066CC; text-align: center;'>
    <b>Diet and Emotional Support:</b>
    </div>
    """, unsafe_allow_html=True)

    # Animated heart icons for emotional support
    st.markdown("""
    <div style='display: flex; justify-content: center;'>
    <span style='font-size: 30px; color: #FF5733; animation: heartbeat 1s infinite; margin-right: 10px;'>&#128151;</span>
    <span style='font-size: 30px; color: #FF5733; animation: heartbeat 1s infinite 0.5s; margin-right: 10px;'>&#128151;</span>
    <span style='font-size: 30px; color: #FF5733; animation: heartbeat 1s infinite 1s; margin-right: 10px;'>&#128151;</span>
    <span style='font-size: 30px; color: #FF5733; animation: heartbeat 1s infinite 1.5s; margin-right: 10px;'>&#128151;</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size: 16px; color: #0066CC; text-align: center;'>
    <b>Additional Resources:</b>
    </div>
    """, unsafe_allow_html=True)

    # List of resources with clickable links
    st.markdown("""
    <ul style='font-size: 16px;'>
        <li><a href="https://www.parkinson.org/" target="_blank" style='color: #009900;'>Parkinson's Foundation</a></li>
        <li><a href="https://www.michaeljfox.org/" target="_blank" style='color: #009900;'>Michael J. Fox Foundation</a></li>
        <li><a href="https://www.unitywalk.org/" target="_blank" style='color: #009900;'>Parkinson's Unity Walk</a></li>
        <li><a href="https://www.parkinsonsresources.org/" target="_blank" style='color: #009900;'>Parkinson's Resources</a></li>
        <li><a href="https://www.pdf.org/" target="_blank" style='color: #009900;'>Parkinson's Disease Foundation</a></li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size: 16px; color: #0066CC; text-align: center;'>
    <b>Remember, while a Parkinson's diagnosis may bring challenges, there are many resources and strategies available to help you lead a fulfilling life and manage your condition effectively.</b>
    </div>
    """, unsafe_allow_html=True)

    # Add more interactive and animated elements as needed


if __name__ == '__main__':
    main()
