import streamlit as st
import pyllusion

illusions = ["Delboeuf","Ebbinghaus","MullerLyer","Ponzo","White","Contrast","VerticalHorizontal","Zollner"]

st.sidebar.title("Illusion picker")
selected_illusion = st.sidebar.selectbox("Pick an illusion:", illusions)
strength = st.sidebar.slider('Choose illusion strength:', 0, 30, 1)

if st.sidebar.button('Show Illusion'):
    if selected_illusion == "Delboeuf":
        #strength = st.slider('Choose illusion strength:', 0, 20, 1)
        delboeuf = pyllusion.Delboeuf(illusion_strength=strength)
        st.image(delboeuf.to_image())
        
    if selected_illusion == "Ebbinghaus":
        #strength = st.slider('Choose illusion strength:', 0, 20, 1)
        ebbinghaus = pyllusion.Ebbinghaus(illusion_strength=strength)
        st.image(ebbinghaus.to_image())
        
    if selected_illusion == "MullerLyer":
        #strength = st.slider('Choose illusion strength:', 0, 20, 1)
        mullerlyer = pyllusion.MullerLyer(illusion_strength=strength)
        st.image(mullerlyer.to_image())
    
    if selected_illusion == "Ponzo":
        #strength = st.slider('Choose illusion strength:', 0, 20, 1)
        ponzo = pyllusion.Ponzo(illusion_strength=strength)
        st.image(ponzo.to_image())
        
    if selected_illusion == "VerticalHorizontal":
        #strength = st.slider('Choose illusion strength:', 0, 20, 1)
        verticalhorizontal = pyllusion.VerticalHorizontal(illusion_strength=-90)
        st.image(verticalhorizontal.to_image())
        
    if selected_illusion == "Zollner":
        #strength = st.slider('Choose illusion strength:', 0, 20, 1)
        zollner = pyllusion.Zollner(illusion_strength=75)
        st.image(zollner.to_image())
        
    if selected_illusion == "Contrast":
        #strength = st.slider('Choose illusion strength:', 0, 20, 1)
        contrast = pyllusion.Contrast(illusion_strength=strength)
        st.image(contrast.to_image())
        
    if selected_illusion == "White":
        #strength = st.slider('Choose illusion strength:', 0, 20, 1)
        white = pyllusion.White(illusion_strength=strength)
        st.image(white.to_image())