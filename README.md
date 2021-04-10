# NER-on-Wiki-Scraped-Data
Named Entity Recognition is a way of information extraction that seeks to locate and classify named entities in text into pre-defined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.
NER is used in Natural Language Processing for labelling the word with different pre-defined entities.

## Demo
![](app.gif)

## Live Application
Check out my App: [Click here](http://bit.ly/Streamlitapp)

## Objective
This app is developed using [Streamlit](https://streamlit.io/). Streamlit is an open-source app framework for Machine Learning and Data Science teams. It's a really easy and convenient way to design and get sharable web apps using Python in Streamlit framework.
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

## Data Scraping from Wikipedia-API
> [Wikipedia-API](https://pypi.org/project/Wikipedia-API/) is easy to use Python wrapper for Wikipedias’ API. It supports extracting texts, sections, links, categories, translations, etc from Wikipedia.
After insalling API, we simply import it in our python programme in our required language format.
```
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
```
Wikipedia API offers different ways to retrieve information from Website using URL,Title etc. I have used Title to fetch the whole page in text format. 
```
page_py=wiki_wiki.page(Article_Name)  #For getting the page with Article Name
page_py.text  # Returns whole summary and text of the page
```

## Named Entity Recognition
This technique is used to label named *real world-objects* like Person, Date, Money etc. A python library spaCy was used for performing this.
[spaCy](https://spacy.io/usage/spacy-101) is a free open-source library for advanced NLP in Python.
- First of all, I have imported a trained pipeline for NLP
```
nlp = spacy.load('en_core_web_sm')
```
- Using the above pipeline, we can process our scapped data and tokenize it.
```
docx= nlp(raw_data)
```
- We need to have spacy_streamlit for visualising the NER & then using visualize_ner, we can see the labelled objects.
``` 
spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)
```
## Implementation
I have used [Streamlit Public Sharing](https://docs.streamlit.io/en/stable/deploy_streamlit_app.html) to host my application. I have pushed my project on Git and added a [requirement.txt](https://github.com/nitinsanatan/NER-on-Wiki-Scraped-Data/blob/main/requirements.txt) file to assist streamlit install dependencies.

## Contact me  [![Twitter][1.2]][1]  [![LinkedIn][2.2]][2]


[1.2]: http://i.imgur.com/wWzX9uB.png
[2.2]: https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/linkedin-3-16.png

[1]: https://twitter.com/SanatanShukla58
[2]: https://www.linkedin.com/in/nitinsanatan/
