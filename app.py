import streamlit as st
from PIL import Image
import os
import cloudinary
import cloudinary.uploader
import urllib.parse

# **Cloudinary Configuration**
CLOUD_NAME = "dq7j4ap5z"
API_KEY = "517785911665488"
API_SECRET = "hRnP04PHuHjAWJ711S8jHvmYn-U"

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET
)

# **Image Resize Dimensions**
SIZES = {
    "300x250": (300, 250),
    "728x90": (728, 90),
    "160x600": (160, 600),
    "300x600": (300, 600),
}

# **Streamlit UI**
st.title("🖼️ Image Resizer & Twitter Auto Post")

# **Upload Image**
uploaded_file = st.file_uploader("Upload an image (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # **Display Original Image**
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Original Image", use_container_width=True)

    # **Create Folder for Resized Images**
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    # **Resize & Upload Images to Cloudinary**
    uploaded_urls = []
    tweet_content = "📢 Check out these awesome resized images! 👇\n\n"

    for i, (name, size) in enumerate(SIZES.items(), start=1):
        resized = image.resize(size)
        save_path = os.path.join(output_dir, f"{name}.png")
        resized.save(save_path)

        # **Upload to Cloudinary**
        upload_result = cloudinary.uploader.upload(save_path)
        image_url = upload_result["secure_url"]
        uploaded_urls.append(image_url)

        # **Show resized images**
        st.image(resized, caption=f"✅ Resized: {name}", use_container_width=True)

        # **Format the Tweet Text**
        tweet_content += f"📌 **Image {i} ({name})**: {image_url}\n\n"

    # **Encode for Twitter URL**
    encoded_tweet = urllib.parse.quote(tweet_content.strip())

    # **Generate Twitter Post Link**
    twitter_url = f"https://twitter.com/intent/tweet?text={encoded_tweet}"

    # **Show Twitter Post Button**
    st.markdown(f"""
    ### 📢 [**Post on Twitter**]({twitter_url})
    """, unsafe_allow_html=True)

    st.success("🎉 Images Resized & Uploaded Successfully! Click the button to post on Twitter.")
