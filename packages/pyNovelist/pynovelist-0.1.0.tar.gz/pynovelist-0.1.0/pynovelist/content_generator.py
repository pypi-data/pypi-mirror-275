import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import spacy
from transformers import pipeline
import config
from narrative_tracker.tracker import NarrativeTracker
from openai import OpenAI
import logging

logging.basicConfig(level=logging.INFO)

client = OpenAI(api_key=config.OPENAI_KEY, organization='org-pQMFdz3Snb6IkARxsvmZ5FzJ')
narrative_tracker = NarrativeTracker()
nlp = spacy.load("en_core_web_sm")
sentiment_analysis = pipeline("sentiment-analysis")

def generate_content(prompt_text, chapter):
    context = narrative_tracker.get_context()
    prompt_with_context = f"{prompt_text}\n\nContext:\n{context}"
    content = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI trained to generate detailed novel content."},
            {"role": "user", "content": prompt_with_context}
        ],
        model="gpt-4-turbo",
        temperature=0.4,
        max_tokens=4096,
        top_p=0.9
    ).choices[0].message.content.strip()
    
    # Tokenize content
    sentences = sent_tokenize(content)
    words = [word_tokenize(sentence) for sentence in sentences]
    
    # Analyze themes using scikitlearn
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([content])
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
    
    # Create a DataFrame for analysis
    df = pd.DataFrame({"Sentences": sentences, "Words": words})
    
    # Perform named entity recognition
    doc = nlp(content)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Perform sentiment analysis
    sentiments = [sentiment_analysis(sentence)[0] for sentence in sentences]
    
    # Update narrative tracker with the new content
    narrative_tracker.track_characters(content)
    narrative_tracker.track_locations(content)
    narrative_tracker.track_plot_points(content, chapter)
    narrative_tracker.track_themes(content)
    narrative_tracker.track_relationships(content)
    narrative_tracker.track_emotional_arcs(content)
    narrative_tracker.track_foreshadowing(content, chapter)
    narrative_tracker.track_world_changes(content, chapter)
    
    return content
