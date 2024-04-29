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
                               ['About parkinsons', 'Prediction', 'Recent News On PD', 'Treatment Options', 'Advices On Youtube','Inspirational Perspectives',
                               'Contact us','Project Rating','For Open Source License Contact Here'],
                               icons=['file-earmark-person-fill',
                               'search','newspaper','prescription2','youtube','power','person-lines-fill','stars','sourceforge'], default_index=0)

           # means firstly it shows index 0th code ie.,About parkinson

    # About parkinson page
    
# below code is for recent news page ----------------------------------------------

    if selected == 'Recent News On PD':

        def recent_news_page():
            st.title("Recent News on Parkinson's Disease")
    
            # Add your content for recent news here
    
        if __name__ == '__main__':
            recent_news_page()

# below code is for treatment page ----------------------------------------------

    if selected == 'Treatment Options':

        def treatment_options_page():
            st.title("Treatment Options for Parkinson's Disease")
    
            # Add your content for treatment options here
    
        if __name__ == '__main__':
            treatment_options_page()

 # below code is for rating page ----------------------------------------------   

    if selected == 'Project Rating':



        
        # Define the emoji icons and their corresponding messages
        emojis = {
            1: ("😞", "Sorry to hear that. We'll work on improving."),
            2: ("😐", "Thanks for your feedback. We'll take it into account."),
            3: ("😊", "Glad you liked it! We appreciate your support."),
            4: ("🎉", "Awesome! We're thrilled you enjoyed it."),
            5: ("🌟", "You're a star! Thanks for the glowing review!"),
        }
        
        def project_rating_page():
            st.title("Project Rating")
            st.write("Rate our project:")
            rating = st.slider("Rate from 1 to 5", 1, 5)
            submitted = st.button("Submit Rating")
            
            if submitted:
                # Display the selected emoji and corresponding message after submission
                emoji, message = emojis[rating]
                st.write(f"You rated our project: {emoji} {rating} {emoji}")
                st.info(message)
        
                # Add animations or celebrations here after submission
                st.balloons()
        
        if __name__ == '__main__':
            project_rating_page()


            
# below code is for source_license page ----------------------------------------------
    
    if selected == 'For Open Source License Contact Here':
        st.markdown("[Click here to visit Source License Information](https://www.autmdu.in/DEPARTMENTS/CSE/index.php)")

        



# below code is for advice page ----------------------------------------------        

    if selected == 'Advices On Youtube':

        def advices_youtube_page():
            st.title("Advices on Parkinson's Disease - YouTube")
    
            # Add your content for YouTube advices here
    
        if __name__ == '__main__':
            advices_youtube_page()
        
# below code is for inspire page ----------------------------------------------
    
    if selected == 'Inspirational Perspectives':
    
        def inspirational_perspectives_page():
            st.title("Inspirational Perspectives on Parkinson's Disease")
    
            # Add your content for inspirational perspectives here
    
        if __name__ == '__main__':
            inspirational_perspectives_page()

# below code is for about page ----------------------------------------------

    
    if selected == 'About parkinsons':
    
        st.title("Understanding Parkinson's Disease")
    
        st.write("""
        Parkinson's disease is a neurological disorder that affects movement. It typically starts with subtle symptoms and progresses over time. Understanding the key aspects of Parkinson's can help individuals and caregivers manage the condition effectively.
        """)
    
        # Introduction Section
        st.header("Introduction")
            # Create columns for better organization
        col1, col2 = st.columns([2, 1])
    
        # Add the first image in the first column
        with col1:
            st.image('./images/br4.png', width=300, caption="Parkinson's Disease")
    
        # Add the second image in the second column
        with col2:
            st.image('./images/br5.png', width=300, caption="Brain Structure")
        st.write("""
        Parkinson's disease is characterized by tremors, stiffness, and difficulty with movement. It affects nerve cells in the brain that produce dopamine, a crucial chemical for movement control.
        """)
    
        # Symptoms Section
        st.header("Symptoms")
        st.write("""
        - **Tremor:** Involuntary shaking, often starting in the hands.
        - **Bradykinesia:** Slowed movement, making tasks challenging.
        - **Muscle Rigidity:** Stiffness and difficulty with flexibility.
        - **Postural Instability:** Balance problems and impaired posture.
        - **Loss of Automatic Movements:** Difficulty with unconscious actions like blinking or smiling.
        - **Speech and Writing Changes:** Soft speech, slurred words, and small handwriting.
        """)
        
        # Causes and Risk Factors Section
        st.header("Causes and Risk Factors")
        st.write("""
        The exact cause of Parkinson's is unknown, but it's believed to be a combination of genetic and environmental factors. Risk factors include aging, family history, and exposure to certain toxins.
        """)
    
        # Diagnosis and Treatment Section
        st.header("Diagnosis and Treatment")
        st.write("""
        Early diagnosis is crucial for managing Parkinson's effectively. Doctors use a combination of medical history, physical exams, and neurological tests for diagnosis. Treatment includes medications, physical therapy, and lifestyle changes.
        """)
    
        # Coping Strategies Section
        st.header("Coping Strategies")
        st.write("""
        Living with Parkinson's requires a holistic approach. It's essential to stay active, eat a balanced diet, manage stress, and engage in activities that promote mental well-being. Support groups and regular check-ups are also beneficial.
        """)
    
        # Conclusion and Resources
        st.header("Conclusion and Resources")
        st.write("""
        While Parkinson's presents challenges, advancements in treatment and support resources offer hope and improved quality of life. Stay informed, seek professional guidance, and connect with community resources for comprehensive care.
        """)
        st.markdown("""
        <div style='font-size: 16px; color: #007bff; text-align: center;'>
        <b>For more information, visit:</b><br>
        <a href="https://www.parkinson.org/" target="_blank">Parkinson's Foundation</a><br>
        <a href="https://www.michaeljfox.org/" target="_blank">Michael J. Fox Foundation</a><br>
        <a href="https://www.unitywalk.org/" target="_blank">Parkinson's Unity Walk</a><br>
        </div>
        """, unsafe_allow_html=True)
            # YouTube Video Section
        st.header("Parkinson's Disease Explained")
    
        # Add a YouTube video using st.video
        st.video("https://www.youtube.com/watch?v=833PhOsu-YE&pp=ygUjcGFya2luc29uIGRpc2Vhc2UgZXhwbGFuYXRpb24gdGFtaWw%3D")


    if selected == 'Contact us':      
        def contact_us_page():
            st.markdown("""
            <h1 style='font-family: Arial, sans-serif; font-size: 36px; color: #FFFFFF; text-align: center;'>Contact Us</h1>
            <p style='font-size: 18px; color: #555555; text-align: center;'>We'd love to hear from you! Please fill out the form below or reach out to us directly.</p>
            """, unsafe_allow_html=True)
        
            # Contact Form Section
            name = st.text_input('Name')
            email = st.text_input('Email')
            message = st.text_area('Message', height=200)
        
            # Check if all fields are filled
            if not name or not email or not message:
                st.warning('Please enter your name, email, and message.')
            else:
                submitted = st.button('Submit')
                
                if submitted:
                    # Process the contact information (e.g., send an email, store in a database, etc.)
                    st.success('Thank you for your message! We will get back to you soon.')
                    animate_button()
        
            # Direct Contact Information Section
            st.header("Direct Contact Information")
        
            st.markdown("""
            <div style='font-size: 16px; color: #555555;'>
            If you prefer to contact us directly, here is our contact information:
            </div>
            """, unsafe_allow_html=True)
        
            # Use columns for better organization
            col1, col2 = st.columns(2)
        
            with col1:
                st.markdown("""
                <div style='font-size: 16px; color: #007bff;'>
                <b>Email:</b> contact@example.com
                </div>
                """, unsafe_allow_html=True)
        
                st.markdown("""
                <div style='font-size: 16px; color: #007bff;'>
                <b>Phone:</b> +1 (123) 456-7890
                </div>
                """, unsafe_allow_html=True)
        
                st.markdown("""
                <div style='font-size: 16px; color: #007bff;'>
                <b>Social Media:</b>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                <div style='font-size: 16px; color: #007bff;'>
                <b>Facebook:</b> <a href="https://www.facebook.com/" target="_blank">Facebook Page</a>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                <div style='font-size: 16px; color: #007bff;'>
                <b>Twitter:</b> <a href="https://twitter.com/" target="_blank">Twitter Page</a>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown("""
                <div style='font-size: 16px; color: #007bff;'>
                <b>Address:</b> 123 Street, City, Country
                </div>
                """, unsafe_allow_html=True)
        
        def animate_button():
            # Add animation effects to the submit button
            st.button('Submit', key='submit_button', on_click=animate_button)
        
        if __name__ == '__main__':
            contact_us_page()




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
        <blockquote style='font-size: 30px; text-align: center;'>
            "The greatest wealth is health." <br>
            <em>- Virgil</em>
        </blockquote>
    """, unsafe_allow_html=True)

    st.header('Encouraging Video:')
    # Embedding a YouTube video using st.video()
    video_link = 'https://www.youtube.com/watch?v=rpcb9a3EsRA&pp=ygUUcGFya2luc29uIHByZXZlbnRpb24%3D'
    st.video(video_link)
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

    st.image('pd1.jpg', width=800)  # Add an image for emotional connection

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


    st.title("Relaxing Video for Parkinson's Patients")

    # Embedding a YouTube video using st.video()
    video_link = 'https://www.youtube.com/watch?v=9MIFX0w7At8&pp=ygUacGFya2luc29uIGRpc2Vhc2UgZXhlcmNpc2U%3D'
    st.video(video_link)
    st.write("Watch this video for more encouragement and information.")

        # Add a YouTube video with adjusted frame size
    #st.markdown("""
    #<div style='text-align: center;'>
    #    <iframe width="640" height="360" src="https://www.youtube.com/watch?v=9MIFX0w7At8&pp=ygUacGFya2luc29uIGRpc2Vhc2UgZXhlcmNpc2U%3D" frameborder="0" allowfullscreen></iframe>
    #</div>
    #""", unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size: 16px; color: #0066CC; text-align: center;'>
    <b>Remember, while a Parkinson's diagnosis may bring challenges, there are many resources and strategies available to help you lead a fulfilling life and manage your condition effectively.</b>
    </div>
    """, unsafe_allow_html=True)

    # Add more interactive and animated elements as needed


if __name__ == '__main__':
    main()
