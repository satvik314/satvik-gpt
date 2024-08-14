import streamlit as st
from langchain_openai import ChatOpenAI

# Title and description
st.title("🤖 Satvik-GPT")
st.markdown("🚀 Generate LinkedIn posts on Generative AI like [Satvik Paramkusham](https://www.linkedin.com/in/satvik-paramkusham/)") 
st.markdown("❤️ Powered by GPT-4o-mini fine-tuned model.")

# Text input for topic
topic = st.text_input("Please enter the topic")

st.code("""
            Try:
            Explain Transformers Architecture
            How does RAG work?
            """, language= None)

# Initialize the models
base_model = ChatOpenAI(model="gpt-4o-mini")
ft_model = ChatOpenAI(model="ft:gpt-4o-mini-2024-07-18:personal::9ootOJfn")

def generate_linkedin_post(prompt, base_model=base_model, ft_model=ft_model):
    response1 = base_model.invoke(prompt)
    response2 = ft_model.invoke(prompt)
    return response1.content, response2.content

if st.button("Generate Posts"):
    if topic:
        with st.spinner("Generating posts..."):
            base_response, ft_response = generate_linkedin_post(f"Generate a LinkedIn post about {topic}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Base Model (gpt-4o-mini) 🔗")
            st.markdown(f'<div class="output-text">{base_response}</div>', unsafe_allow_html=True)
        
        with col2:
            st.subheader("Satvik-GPT (Fine-tuned Model)")
            st.markdown(f'<div class="output-text">{ft_response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic before generating posts.")

