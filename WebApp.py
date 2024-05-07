#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
from newsapi import NewsApiClient
from streamlit_player import st_player
from streamlit_folium import st_folium
import folium
#from googlenews import GoogleNews

    # Define a dictionary of languages and their corresponding translations
    languages = {
        'English': 'en',
        'Spanish': 'es',
        'French': 'fr',
        'German': 'de',
        'Italian': 'it',
        # Add more languages as needed
    }
    
    # Create a dropdown list of languages
    language = st.selectbox('Select Language', list(languages.keys()))
    
    # Use the selected language to translate the text on the page
    if language == 'English':
        st.write('Hello, World!')
    elif language == 'Spanish':
        st.write('Hola, Mundo!')
    elif language == 'French':
        st.write('Bonjour, Monde!')
    elif language == 'German':
        st.write('Hallo, Welt!')
    elif language == 'Italian':
        st.write('Ciao, Mondo!')
    
    st.write('<button>Language</button>', unsafe_allow_html=True)
        
# Initialize News API client
newsapi = NewsApiClient(api_key='27f8f84410134cd6b060a9ad0170a78c')  # Replace 'YOUR_API_KEY' with your actual API key

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
        return "The Person has Parkinson's"
        #return "The Person does not have Parkinson's Disease"


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
    
        def fetch_news():
            # Fetch top headlines related to Parkinson's disease
            headlines = newsapi.get_top_headlines(q='Parkinson disease', language='en', country='us')
            articles = headlines['articles'][:6]  # Limiting to 6 articles for display
    
            return articles

        def recent_news_page():
            st.title("Recent News on Parkinson's Disease")
    
            articles = fetch_news()
    
            # Check if there are articles to display
            if not articles:
                st.error("No news articles found. Please try again later.")
                return
    
            # Display news articles in columns
            col1, col2, col3 = st.columns(3)
    
            for idx, article in enumerate(articles):
                with globals()[f"col{idx % 3 + 1}"]:
                    st.markdown(f"**{article['title']}**")
                    st.image(article['urlToImage'], use_column_width=True)
                    st.write(article['description'])
                    st.write(f"Source: {article['source']['name']}")
                    st.write(f"Published At: {article['publishedAt']}")
    
        if __name__ == '__main__':
            recent_news_page()


# below code is for treatment page ----------------------------------------------

    if selected == 'Treatment Options':

        def treatment_options_page():
            st.title("Treatment Options for Parkinson's Disease")
        
            st.markdown("""
            Parkinson's disease can be managed through various treatment options. Here are some common approaches:
            """)
            
            st.header("Medication")
        
            st.write("""
            Medications are often used to help manage the symptoms of Parkinson's disease. These may include:
            - Levodopa
            - Dopamine agonists
            - MAO-B inhibitors
            - Anticholinergics
            - Amantadine
            """)
            
            st.header("Deep Brain Stimulation (DBS)")
        
            st.write("""
            DBS is a surgical procedure that can help control Parkinson's symptoms. It involves implanting electrodes in specific areas of the brain and using a device similar to a pacemaker to deliver electrical impulses.
            """)
            
            st.header("Physical and Occupational Therapy")
        
            st.write("""
            Therapy sessions can help improve mobility, balance, and overall quality of life for Parkinson's patients. Exercises, stretching, and adaptive techniques are often part of these therapies.
            """)
            
            st.header("Speech and Swallowing Therapy")
        
            st.write("""
            Speech therapy can address difficulties with speech, swallowing, and communication that may arise in Parkinson's disease. Exercises and techniques are tailored to individual needs.
            """)
            
            st.header("Exercise and Nutrition")
        
            st.write("""
            Regular exercise, such as aerobic workouts, stretching, and strength training, can be beneficial for Parkinson's patients. A balanced diet rich in nutrients also supports overall health.
            """)
            
            st.header("Alternative Therapies")
        
            st.write("""
            Some individuals explore alternative therapies like acupuncture, massage, and yoga to complement traditional treatments. It's essential to consult healthcare professionals before trying any new therapies.
            """)
        
            st.markdown("""
            For personalized treatment plans and recommendations, always consult with your healthcare provider or a specialist familiar with Parkinson's disease.
            """)
        
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
                #st.balloons()
        
        if __name__ == '__main__':
            project_rating_page()


            
# below code is for source_license page ----------------------------------------------
    
    if selected == 'For Open Source License Contact Here':
        def open_source_license_page():
            st.title("Open Source License Information")
            
            st.markdown("""
            Open source projects are powered by collaboration and community contributions. They embody the spirit of sharing, innovation, and accessibility. At [Your Website], we deeply appreciate and support open source initiatives.
            """)
            
            st.markdown("""
            We believe in the principles of open source software, which include:
            - Transparency
            - Collaboration
            - Accessibility
            - Flexibility
            - Continuous improvement
            """)
            
            st.markdown("""
            Open source licenses play a crucial role in defining how software can be used, modified, and distributed. They provide legal frameworks that protect both developers and users.
            """)
        
            st.markdown("""
            If you'd like to learn more about open source licenses and their importance, you can [click here to visit Source License Information](https://www.autmdu.in/DEPARTMENTS/CSE/details.php?id=8).
            """)
        
            st.success("Explore the world of open source and contribute to meaningful projects!")
        
        if __name__ == '__main__':
            open_source_license_page()

        



# below code is for advice page ----------------------------------------------        

    if selected == 'Advices On Youtube':

        def advices_youtube_page():
            st.title("Advices on Parkinson's Disease - YouTube")
        
            # Define a list of YouTube video URLs related to Parkinson's disease
            video_urls = [
                	"https://www.youtube.com/watch?v=2YCLRTPzJs4&pp=ygUjcGFya2luc29uIGRpc2Vhc2UgZXhwbGFuYXRpb24gdGFtaWw%3D",
                        "https://www.youtube.com/watch?v=uzEcICmlmRI&pp=ygUjcGFya2luc29uIGRpc2Vhc2UgZXhwbGFuYXRpb24gdGFtaWw%3D",
                        "https://www.youtube.com/watch?v=TQjjiGegEHI&pp=ygUjcGFya2luc29uIGRpc2Vhc2UgZXhwbGFuYXRpb24gdGFtaWw%3D",
                        "https://www.youtube.com/watch?v=-0uBYZn8Ckw&pp=ygUjcGFya2luc29uIGRpc2Vhc2UgZXhwbGFuYXRpb24gdGFtaWw%3D",
                        "https://www.youtube.com/watch?v=qXCdPBFHp5A&pp=ygUjcGFya2luc29uIGRpc2Vhc2UgZXhwbGFuYXRpb24gdGFtaWw%3D"
                # Add more video URLs as needed
            ]
        
            # Create a DataFrame with the video URLs
            videos_df = pd.DataFrame({"YouTube Video": video_urls})
        
            # Add arrow buttons below the video to navigate
            col1, col2, col3 = st.columns([1, 8, 1])
            with col2:
                selected_video_index = st.session_state.get("selected_video_index", 0)
                if st.button("◄"):
                    selected_video_index = max(0, selected_video_index - 1)
                if st.button("►"):
                    selected_video_index = min(len(video_urls) - 1, selected_video_index + 1)
                st.session_state["selected_video_index"] = selected_video_index
        
            # Display the selected video using the st_player component
            st_player(videos_df.iloc[selected_video_index, 0])
        
        if __name__ == '__main__':
            advices_youtube_page()
        
# below code is for inspire page ----------------------------------------------
    
    if selected == 'Inspirational Perspectives':
    
         st.title("Inspirational Stories and Patient Perspectives")

         st.write("""
            Living with Parkinson's disease can be challenging, but many individuals have found strength, resilience, and hope in their journey. Here are some inspiring stories:
            
            - *John's Journey:* Despite his diagnosis, John continues to pursue his passion for painting and has even held exhibitions to raise awareness about Parkinson's disease.
            
            - *Maria's Mission:* Maria was diagnosed with Parkinson's at a young age but has since become a vocal advocate, raising funds and awareness for research.
            
            - *David's Determination:* David, a former athlete, has adapted his exercise routine to manage his symptoms and continues to lead an active lifestyle.
            
            These stories serve as a reminder that life with Parkinson's can still be fulfilling and meaningful, and that a positive attitude and support can make a difference.
            """)

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
            MDVP_Fo_Hz = st.text_input('Enter MDVP_Fo(Hz)')
        with col2:
            MDVP_Fhi_Hz = st.text_input('Enter MDVP_Fhi(Hz)')
        with col3:
            MDVP_Flo_Hz = st.text_input('Enter MDVP_Flo(Hz)')
        with col4:
            MDVP_Jitter_percent = st.text_input('Enter MDVP_Jitter(%)')
        with col5:
            MDVP_Jitter_Abs = st.text_input('Enter MDVP_Jitter(Abs)')
        with col1:
            MDVP_RAP = st.text_input('Enter MDVP_RAP')
        with col2:
            MDVP_PPQ = st.text_input('Enter MDVP_PPQ')
        with col3:
            Jitter_DDP = st.text_input('Enter Jitter_DDP')
        with col4:
            MDVP_Shimmer = st.text_input('Enter MDVP_Shimmer')
        with col5:
            Shimmer_dB = st.text_input('Enter Shimmer_dB')
        with col1:
            Shimmer_APQ3 = st.text_input('Enter Shimmer_APQ3')
        with col2:
            Shimmer_APQ5 = st.text_input('Enter Shimmer_APQ5')
        with col3:
            MDVP_APQ = st.text_input('Enter MDVP_APQ')
        with col4:
            Shimmer_DDA = st.text_input('Enter Shimmer_DDA')
        with col5:
            NHR = st.text_input('Enter_NHR')
        with col1:
            HNR = st.text_input('Enter_HNR')
        with col2:
            RPDE = st.text_input('Enter_RPDE')
        with col3:
            DFA = st.text_input('Enter_DFA')
        with col4:
            spread1 = st.text_input('Enter_spread1')
        with col5:
            spread2 = st.text_input('Enter_spread2')
        with col1:
            D2 = st.text_input('Enter_D2')
        with col2:
            PPE = st.text_input('Enter_PPE')
            

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

    #st.balloons()  # Celebrate the good news!

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
