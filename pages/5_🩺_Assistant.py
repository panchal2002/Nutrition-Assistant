import requests
from bs4 import BeautifulSoup
from streamlit_lottie import st_lottie
import streamlit as st
import time


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_nutrition = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_0fhlytwe.json")


# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        # st.subheader("Hi, Welcome :wave:")
        st.title("Hey👋, Welcome to Health Assistant")
        st.write(
            "Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. Eum quas beatae cumque eum quaerat. Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. Eum quas beatae cumque eum quaerat."
        )

    with right_column:
        st_lottie(lottie_nutrition, height=300, key="codin")

    # Define a dictionary of URLs for different diseases
urls = {
    "None": "",
    "heart disease": "https://www.healthline.com/nutrition/heart-healthy-foods",
    "obesity": "https://www.healthline.com/nutrition/12-fat-burning-foods",
    "hypertension": "https://www.healthline.com/nutrition/foods-high-blood-pressure",
    "cancer": "https://www.healthline.com/nutrition/cancer-fighting-foods"
}

# Define the Streamlit app


def app():
    st.title("Healthy Food Suggestions")

    # Ask the user for their name, age, and disease
    name = st.text_input("What is your name?")
    if (len(name) > 0):
        age = st.number_input("What is your age?",
                              min_value=0, max_value=120)
        if (age > 0):
            disease = st.selectbox(
                "What disease do you have?", list(urls.keys()))
            if (disease != "None"):
                # Scrape the website for healthy food suggestions
                url = urls[disease]
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                foods = soup.find_all("h2")[1:]
                foods = [food.text for food in foods]

                # Display the results
                st.write(
                    f"Hello, {name}! Based on your age of {age} and disease of {disease}, we recommend the following healthy foods:")
                i = 1
                for food in foods[:8]:
                    st.info(str(i)+". " + food[3:])
                    i += 1
            else:
                st.info("Please select a disease!")


app()
