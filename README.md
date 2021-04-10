# NER-on-Wiki-Scraped-Data
Named Entity Recognition is a way of information extraction that seeks to locate and classify named entities in text into pre-defined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.
NER is used in Natural Language Processing for labelling the word with different pre-defined entities.

## Objective
This app is developed using Streamlit. Streamlit is an open-source app framework for Machine Learning and Data Science teams. It's a really easy and convenient way to design and get sharable web apps using Python in Streamlit framework.
The main objective of this application is scraping data from Wikipedia and performing Named Entity Recognition on the fetched data.
I have used Wikipedia-API to get the pages from Wiki and spaCy library of Python is used for performing NER operations on the data.

## Install Dependencies
```
pip install streamlit
pip install spacy
pip install spacy-streamlit
pip install Wikipedia-API
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0-py3-none-any.whl 
```

## Demo
![](app.gif)
