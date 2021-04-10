import streamlit as st
import spacy_streamlit
import spacy
import wikipediaapi


nlp = spacy.load('en_core_web_sm')

wiki_wiki = wikipediaapi.Wikipedia('en')
def get_text(topic):
    page_py = wiki_wiki.page(topic)
    return page_py.text


def main():
    st.title("NER from Wikipedia Data")

    menu= ["Home"]
    choice= st.sidebar.selectbox("Menu",menu)

    if choice== "Home":
        st.subheader("Named Entity Recognition")    
        topic=st.text_area("Wikipedia Search","Title of Article")
        raw_text=get_text(topic)
        docx= nlp(raw_text)
        if st.button("Extract & Analyze"):
            spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)


if __name__ == '__main__':
    main()    

