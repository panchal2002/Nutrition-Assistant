from bs4 import BeautifulSoup
import requests
import streamlit as st


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def fetch_DietPlan(prediction):
    try:
        query = "diet plan for " + prediction + " people"
        num_results = 10
        url = f"https://www.google.com/search?q={query}&num={num_results}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all the search results
        search_results = soup.find_all("div", class_="g")
        # Loop through each search result and print the title and URL
        for result in search_results:
            # Get the title and URL
            title = result.find("h3").get_text()
            url = result.find("a")["href"]
            if url.startswith("/url?"):
                url = url.split("=")[1]

            # Print the title and URL
            st.info(title)
            st.warning(url)
            st.write()

    except Exception as e:
        # st.error("Can't able to fetch the Calories")
        print(e)


def app():
    st.title("BMI Calculator")

    weight = st.number_input("What is your weight (in kg)?")
    height = st.number_input("What is your height (in m)?")

    if (weight > 0 and height > 0):
        bmi = calculate_bmi(weight, height)
        bmi_classification = classify_bmi(bmi)

        st.write("Your BMI is:", bmi)
        st.write("Your BMI classification is:", bmi_classification)
        fetch_DietPlan(bmi_classification)

    else:
        st.warning("Please Enter your age and height.")


app()
