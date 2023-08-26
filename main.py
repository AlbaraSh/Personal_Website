import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="My Website", page_icon=":tada:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#loading in images
welcome = load_lottieurl("https://lottie.host/7939cfd7-fab2-4d7f-a6b9-580552ebd562/HsnIuKtLY7.json")
pomodoro = load_lottieurl("https://lottie.host/8d8348de-aaa1-4a57-afef-2e1bac845516/5TyHH67HVv.json")
studying = load_lottieurl("https://lottie.host/3b13ebd0-046d-4c41-a220-a6566e9f970b/FEu46xcZEL.json")
stocks = load_lottieurl("https://lottie.host/7995fb03-35f1-47ce-801e-52072e28ffc8/EsEPs3owdo.json")
flashcard = load_lottieurl("https://lottie.host/4e5d8cb2-f57c-45b9-a83c-0115ff1036c0/7F2mCs9znY.json")
volleyball = load_lottieurl("https://lottie.host/417a7248-5234-4e4b-9d1b-f21eb66074ff/FdzDnVGbHL.json")
movie = load_lottieurl("https://lottie.host/d140bcb4-4ade-42e4-8ecf-d526fa3474d7/yoZF1gb31U.json")
contact = load_lottieurl("https://lottie.host/bf4e1330-6111-41cf-9d05-51e3395abb74/qURuRCoHzn.json")

# header section
with st.container():
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st_lottie(welcome, height=400, key="welcome")
    with right_column:
        st.subheader("Hi  :wave:")
        st.title(":orange[I am Albara Shoukri]")
        st.write(
            """
            I'm a computer science student, navigating the world of technology with genuine interest and a 
            willingness to learn. My journey kicked off by tinkering with a basic 'Hello, World!' program, and since 
            then, I've been steadily immersing myself in the realm of coding and problem-solving. \n
            
            While I'm not claiming to be a tech prodigy, I find satisfaction in understanding intricate algorithms 
            and designing user interfaces that make sense. I'm here to improve my craft and, one day, make important 
            contributions that positively impact our society and communities.
            """
            )
        st.write("[CV >](https://docs.google.com/document/d/1uxTuRRZHiznvDFyRXQDgJ5Q6yMi61nMy/edit?usp=sharing&ouid=105884513977280338650&rtpof=true&sd=true)")

# my background
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2, gap='small')
    with left_column:
        st.title(":blue[Background]")
        st.write("##")
        st.write(
            """
                As you are already aware, my name is Albara Shoukri, and I am a Palestinian-British student aspiring 
                to become a significant figure in the world of technology. I am the oldest of four children and 
                the son of two loving parents. While I was born in London, at the age of 12, we made the decision 
                to relocate to Qatar, embarking on a new chapter of our lives.\n

                My family has consistently supported and encouraged me to pursue education and explore new 
                opportunities. Though my experiences might not be extravagant, they have ingrained within me a robust 
                work ethic, a sense of humility, and a curiosity that extends beyond my familiar surroundings.\n

                Now, as I embark on my journey as a computer science student, I carry with me the values 
                and lessons instilled in me since childhood. These principles continue to guide me as I seek to 
                enhance my knowledge and make meaningful contributions.
            """
        )
    with right_column:
        st_lottie(studying, height=350, key="coding")

# hobbies
with st.container():
    st.write("---")
    st.title(":blue[Hobbies]")
    image_column, text_column = st.columns((1, 2), gap="large")
    with image_column:
        st_lottie(volleyball, height=300, key="volleyball")
        st.caption("_This is a picture of my school volleyball team in Qatar. I am number 20 at the bottom right._")
    with text_column:
        st.subheader(":orange[Volleyball]")
        st.write(
            """
                Volleyball is a hobby I really like. It's a fun sport that I enjoy playing with friends. 
                When we're on the court together, it feels like we're a team working towards a common 
                goal. Figuring out how to play well as a group is really interesting.\n

                Playing volleyball has also helped me make new friends and improve my social skills. Working 
                together during the game and celebrating small victories with high-fives and cheers brings us closer.\n

                In high school, I joined the school volleyball team, and it was a great experience. 
                We participated in all the local school tournaments and spent a lot of time every week 
                training. Throughout the time I spent playing volleyball, I got a lot closer to my teammates and 
                a lot more connected to the sport.

            """
        )

# media
with st.container():
    image_column, text_column = st.columns((1, 2), gap="large")
    with image_column:
        st_lottie(movie, height=300, key="movie")
    with text_column:
        st.subheader(":orange[Entertainment & Media]")
        st.write(
            """
                I really love entertainment media. It's my way of taking a break from regular life. 
                Whether I'm watching TV shows, reading books, or enjoying movies, I get lost in these exciting 
                worlds. Creators can tell such interesting stories that make me feel happy, sad, or excited.
                Each story becomes a part of me, leaving memories that I cherish.\n

                Engaging with entertainment media has been a source of personal growth for me, as I've absorbed 
                valuable life lessons and gained insights into different cultures and issues. Whether through 
                characters' experiences or expanding my knowledge, it's shaped me into a more empathetic and 
                informed individual.\n

                Entertainment media isn't just a pastime; it's a passport to countless experiences 
                that enrich my imagination and offer a break from the ordinary.

            """
        )

# Pomodoro Project
with st.container():
    st.write("---")
    st.title(":blue[My Projects]")
    image_column, text_column = st.columns((1, 2), gap="large")
    with image_column:
        st_lottie(pomodoro, height=300, key="pomodoro")
    with text_column:
        st.subheader(":orange[Pomodoro Project]")
        st.write(
            """
                In this project, I built my own version of a Pomodoro timer using Tkinter and the Turtle module. 
                A Pomodoro timer is a time management tool that alternates between focused work sessions 
                and short breaks to enhance productivity.\n
    
                I utilized the Tkinter module to design the user interface, including the timer display, background 
                image, and start/reset buttons. Additionally, I employed the Turtle module to enable users to customize 
                the durations of their work and break sessions.\n
    
                This project not only honed my UI design skills but also underscored the importance of prioritizing 
                user convenience when creating an interface.

            """
        )
        st.markdown("[GitHub Link](https://github.com/AlbaraSh/pomodoro_project)")  # add GitHub link to my project

# Stocks Project
with st.container():
    image_column, text_column = st.columns((1, 2), gap="large")
    with image_column:
        st_lottie(stocks, height=300, key="stock")
    with text_column:
        st.subheader(":orange[Stock News Project]")
        st.write(
            """
                In this project, I developed a Python script that displays the percentage difference in a company's
                stock based on the previous day's data, along with delivering the top 3 news articles related 
                to that company for the day. This was accomplished using the TKinter and Requests modules.

                I utilized the TKinter module to construct the user interface, incorporating 
                components such as the current stock label, user input field, and confirm/send info buttons.

                This project marked my introduction to working with APIs. I gained proficiency in 
                accessing APIs via their endpoints and API keys, as well as integrating API data into my 
                project. While I encountered various challenges when dealing with APIs, I effectively 
                resolved them with the assistance of documentation and other online resources.

            """
        )
        st.markdown("[GitHub Link](https://github.com/AlbaraSh/Stock_News_Project)")

# Flashcard Project
with st.container():
    image_column, text_column = st.columns((1, 2), gap="large")
    with image_column:
        st_lottie(flashcard, height=300, key="flashcard")
    with text_column:
        st.subheader(":orange[Language Flashcard Project]")
        st.write(
            """
                The purpose of this project was to create a Python script to aid in learning French.\n
                
                To achieve this, I developed a Flashcard script that presented a French word to the user and provided 
                the answer after a brief delay. Once they received the answer, they could click the 
                appropriate button to indicate if they had answered correctly or not. The words the user 
                answered incorrectly were added to the "words_to_learn" file, allowing them to review it later.\n

                This project marked my initial attempt at utilizing the pandas module, as well as my first 
                experience with try-except blocks.
            """
        )
        st.markdown("[GitHub Link](https://github.com/AlbaraSh/Language_Flashcard)")

# contacts
with st.container():
    st.write("---")
    st.title(":blue[Contact Me]")
    image_column, text_column = st.columns((1, 2), gap="large")
    with image_column:
        st_lottie(contact, height=300, key="contact")
    with text_column:
        st.subheader("Feel free to contact me for any further information.")
        st.write(
            """
                Gmail: albarashoukri1234@gmail.com\n
                Phone: +44 7898551733
            """
        )
        st.markdown("[GitHub Profile](https://github.com/AlbaraSh)")
        