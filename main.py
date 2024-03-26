import streamlit as st
import os 
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import Markdown  
import PIL.Image 

# Load environment variables
load_dotenv()

# Configure generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    st.title("Emotions Recognition") 

    # Upload image
    uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        image = PIL.Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Generate content with vision model
        vision_model = genai.GenerativeModel('gemini-pro-vision')
        response = vision_model.generate_content(["what is the emotions on this images using keyword Happiness, Sadness, Anger, Surprise, Neutral, Anxiety , Disgust, Jealosuy, Guilt, Embarrassment", image])

        st.markdown(response.text)

if __name__ == "__main__":
    main()

