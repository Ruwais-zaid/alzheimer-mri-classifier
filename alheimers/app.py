import streamlit as st
import torch
from torchvision import transforms
from PIL import Image


st.set_page_config(page_title="Alzheimer's MRI Classifier", layout="centered")


classes = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented']

@st.cache_resource
def load_model():
    model = torch.load("resnetmodel.pt", map_location=torch.device("cpu"))
    model.eval()
    return model

model = load_model()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])


st.title("🧠 Alzheimer's Stage Classifier")
st.write("Upload an MRI image to detect the stage of Alzheimer's disease using a ResNet50 model.")

uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)


    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)
        _, predicted = torch.max(output, 1)

    
    if predicted.item() < len(classes):
        predicted_class = classes[predicted.item()]
    else:
        predicted_class = f"Unknown class (index {predicted.item()})"

    st.success(f"🧠 **Predicted Class:** {predicted_class}")
