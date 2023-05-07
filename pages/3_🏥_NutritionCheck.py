import pyrebase
from datetime import datetime
from streamlit_ws_localstorage import injectWebsocketCode, getOrCreateUID

import streamlit as st
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model
import requests
from bs4 import BeautifulSoup

model = load_model('FV.h5')
labels = {0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot',
          7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger',
          14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
          19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple',
          26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn',
          32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}

fruits = ['Apple', 'Banana', 'Bello Pepper', 'Chilli Pepper', 'Grapes', 'Jalepeno', 'Kiwi',
          'Lemon', 'Mango', 'Orange', 'Paprika', 'Pear', 'Pineapple', 'Pomegranate', 'Watermelon']
vegetables = ['Beetroot', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Corn', 'Cucumber', 'Eggplant', 'Ginger',
              'Lettuce', 'Onion', 'Peas', 'Potato', 'Raddish', 'Soy Beans', 'Spinach', 'Sweetcorn', 'Sweetpotato',
              'Tomato', 'Turnip']


# Fetch Calories
def fetch_calories(prediction):
    try:
        url = 'https://www.google.com/search?&q=calorie in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return calories
    except Exception as e:
        # st.error("Can't able to fetch the Calories")
        print(e)

# Fetch protein


def fetch_protein(prediction):
    try:
        url = 'https://www.google.com/search?&q=protein in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        protein = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return protein
    except Exception as e:
        # st.error("Can't able to fetch the Calories")
        print(e)

# Fetch carbs


def fetch_carbs(prediction):
    try:
        url = 'https://www.google.com/search?&q=carbs in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        carbs = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return carbs
    except Exception as e:
        # st.error("Can't able to fetch the Calories")
        print(e)

# Fetch Fat


def fetch_fat(prediction):
    try:
        url = 'https://www.google.com/search?&q=fat in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        fat = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return fat
    except Exception as e:
        # st.error("Can't able to fetch the Calories")
        print(e)

# Fetch Cholesterol


def fetch_chol(prediction):
    try:
        url = 'https://www.google.com/search?&q=fat in ' + prediction
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        chol = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return chol
    except Exception as e:
        # st.error("Can't able to fetch the Calories")
        print(e)


def processed_img(img_path):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()


def run():
    st.title("Nutrition Check👨‍⚕️")
    # st.sidebar.success("Select a page")
    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_column_width=False)
        save_image_path = './upload_images/' + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        # if st.button("Predict"):
        if img_file is not None:
            result = processed_img(save_image_path)
            cal = fetch_calories(result)
            pro = fetch_protein(result)
            carbs = fetch_carbs(result)
            fat = fetch_fat(result)
            cholesterol = fetch_chol(result)

            yes = True
            if pro:
                yes = True
            else:
                yes = False

            if yes == False:
                st.info('** Image cannot be recognized!!')
                return

            print(result)
            if result in vegetables:
                st.info('**Category : Vegetables**')
            else:
                st.info('**Category : Fruit**')
            st.success("**Predicted : " + result + '**')

            if cal:
                st.warning('**' + 'Calories : ' +
                           cal + '(100 grams)**')
            if (pro):
                st.warning('**' + 'Protein : ' + pro + '(100 grams)**')
            if (carbs):
                st.warning('**' + 'Carbs : ' + carbs + '(100 grams)**')
            if (fat):
                st.warning('**' + 'Fat : ' + fat + '(100 grams)**')
            if (cholesterol):
                st.warning('**' + 'Cholesterol : ' +
                           cholesterol + '(100 grams)**')


conn = injectWebsocketCode(hostPort='linode.liquidco.in', uid=getOrCreateUID())
if (conn.getLocalStorageVal(key='isLoggedIn') == 'True'):
    run()
    submit = st.sidebar.button("Logout")
    if submit:
        conn.setLocalStorageVal(key='isLoggedIn', val='False')
        st.experimental_rerun()
else:
    firebaseConfig = {
        'apiKey': "AIzaSyB0ezU_NyXciC0VAK9c7K8ACuahv2iMww0",
        'authDomain': "nutrition-assitant.firebaseapp.com",
        'projectId': "nutrition-assitant",
        'databaseURL': "https://nutrition-assitant-default-rtdb.asia-southeast1.firebasedatabase.app/",
        'storageBucket': "nutrition-assitant.appspot.com",
        'messagingSenderId': "726121613752",
        'appId': "1:726121613752:web:f3d50fef349accbe90e74d",
        'measurementId': "G-WRWSDV256T"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    # Database

    db = firebase.database()
    storage = firebase.storage()

    st.title("Register / Login")

    # Authentication

    choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
    email = st.text_input("Please enter your email address")
    password = st.text_input("Please enter your password", type="password")

    if choice == 'Sign up':
        handle = st.text_input(
            'Please input app handle name', value='Default')
        submit = st.button('Create my account')

        if submit:
            user = auth.create_user_with_email_and_password(email, password)
            st.success('Your account is create successfully')
            st.balloons()
            # sign in
            user = auth.sign_in_with_email_and_password(email, password)
            ret = conn.setLocalStorageVal(key='isLoggedIn', val='True')
            st.experimental_rerun()

    if choice == 'Login':
        submit = st.button('Login')
        if submit:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.balloons()
                ret = conn.setLocalStorageVal(key='isLoggedIn', val='True')
                st.experimental_rerun()
            except Exception:
                st.error("Please provide correct credentials!")

            # Fetch colories
