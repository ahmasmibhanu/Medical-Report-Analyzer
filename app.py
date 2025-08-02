import streamlit as st
from ocr_agent import OCRParserAgent
from interpreter_agent import HealthDataInterpreterAgent
from summary_agent import SummaryGeneratorAgent

import os
from pdf2image import convert_from_bytes
from PIL import Image

st.title("🧾 Medical Report Analyzer")
st.write("Upload a **blood report (PDF or image)** to get a simple explanation of your results.")

uploaded_file = st.file_uploader("Upload a PDF or image file", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    st.success("✅ File uploaded. Processing...")

    # This converts PDF to image if needed
    if uploaded_file.type == "application/pdf":
        images = convert_from_bytes(uploaded_file.read())
        image = images[0]  # Takes first page only
    else:
        image = Image.open(uploaded_file)

    # It saves image temporarily
    temp_image_path = "temp_image.png"
    image.save(temp_image_path)

    with st.spinner("🔍 Extracting text from image..."):
        ocr = OCRParserAgent()
        text = ocr.extract_text_from_image(temp_image_path)
        st.text_area("📝 Extracted Text", text, height=200)

    with st.spinner("🧠 Interpreting medical values..."):
        interpreter = HealthDataInterpreterAgent()
        interpreted = interpreter.interpret(text)
        st.write("📊 Interpreted Results:")
        for item in interpreted:
            st.markdown(f"- {item}")

    with st.spinner("💬 Generating plain-language summary..."):
        summarizer = SummaryGeneratorAgent()
        summary = summarizer.generate_summary(interpreted)
        st.markdown("### 🗣️ Patient-Friendly Summary")
        st.write(summary)

    os.remove(temp_image_path)