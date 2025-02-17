import streamlit as st
from PIL import Image
import os

# Define image sizes
SIZES = {
    "300x250": (300, 250),
    "728x90": (728, 90),
    "160x600": (160, 600),
    "300x600": (300, 600),
}

# Streamlit UI
st.title("Image Resizer & Twitter Sharer")

# File uploader
uploaded_file = st.file_uploader("Upload an image (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Load and display original image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    # Create output folder if not exists
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    # Resize and save images
    resized_images = {}
    for name, size in SIZES.items():
        resized = image.resize(size)
        resized_images[name] = resized
        save_path = os.path.join(output_dir, f"{name}.png")
        resized.save(save_path)
        st.image(resized, caption=f"Resized {name}", use_container_width=True)

    st.success("Images Resized Successfully!")

    # Twitter sharing button
    public_image_url = "https://cdn.pixabay.com/photo/2015/12/13/05/46/mannequin-1090714_1280.jpg"  # Replace with actual uploaded image URL
    tweet_text = "Check out this awesome image!"
    twitter_url = f"https://twitter.com/intent/tweet?text={tweet_text}&url={public_image_url}"

    if st.button("Post on Twitter"):
        st.markdown(f"[Click here to tweet!]({twitter_url})", unsafe_allow_html=True)
