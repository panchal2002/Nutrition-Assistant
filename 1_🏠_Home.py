import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import webbrowser


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_nutrition = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_qxjbnrlu.json")
lottie_contact = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi, Welcome :wave:")
        st.title("Enjoy Your Healthy Delicious Food")
        st.write(
            "Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. Eum quas beatae cumque eum quaerat. Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. Eum quas beatae cumque eum quaerat."
        )
        url = 'http://localhost:8501/NutritionCheck'
        if st.button('Check Nutrition'):
            webbrowser.open(url)
    with right_column:
        video_file = open('media/Food.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_nutrition, height=300, key="codin")
    with right_column:
        st.header("Who We Are!")
        st.write("##")
        st.write(
            """
            Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. :
            - Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. 
            - aSed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. 
            - Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. 
            - Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. "
            Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. Sed autem laudantium dolores. Voluptatem itaque ea consequatur eveniet. 
            """
        )
        url = 'http://localhost:8501/Assistant'
        if st.button('Nutrition Assistant'):
            webbrowser.open(url)


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/rishabhpanchal2002@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_contact, height=300, key="contact")
