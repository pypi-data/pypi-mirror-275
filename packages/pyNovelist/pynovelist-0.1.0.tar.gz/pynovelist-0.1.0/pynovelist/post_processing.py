import os
import subprocess
import sys
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import spacy
from transformers import pipeline
from narrative_tracker.tracker import NarrativeTracker
import logging

logging.basicConfig(level=logging.INFO)

narrative_tracker = NarrativeTracker()
nlp = spacy.load("en_core_web_sm")
sentiment_analysis = pipeline("sentiment-analysis")

def edit_file(filename):
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(filename)
        elif os.name == 'posix':  # For macOS and Linux
            if sys.platform == 'darwin':
                subprocess.call(['open', filename])
            else:
                subprocess.call(['xdg-open', filename])
    except FileNotFoundError:
        logging.error(f"File {filename} not found.")
    except PermissionError:
        logging.error(f"Permission denied to open file {filename}.")
    except Exception as e:
        logging.error(f"Failed to open file {filename}: {e}")

def measure_metrics_and_regenerate(content):
    metrics = analyze_style(content)
    inconsistencies = check_contextual_consistency(content)
    repetitions = detect_repetition(content)
    
    # Display metrics to the user
    logging.info("Metrics:")
    logging.info(f"Average Sentence Length: {metrics['avg_sentence_length']}")
    logging.info(f"Word Frequency: {metrics['word_frequency']}")
    logging.info(f"Readability Score: {metrics['readability_score']}")
    logging.info(f"Sentiment: {metrics['sentiment']}")
    logging.info(f"Lexical Diversity: {metrics['lexical_diversity']}")
    
    # Display inconsistencies to the user
    if inconsistencies:
        logging.info("Inconsistencies found:")
        for inconsistency in inconsistencies:
            logging.info(inconsistency)
    
    # Display repetitions to the user
    if repetitions:
        logging.info("Repetitions found:")
        for repetition_type, repetition_list in repetitions.items():
            logging.info(f"{repetition_type.capitalize()}: ")
            for item, count in repetition_list.items():
                logging.info(f"{item} (repeated {count} times)")
    
    # Allow user to review and modify content
    with open("chapter_review.txt", "w") as f:
        f.write(content)
    logging.info("Content written to 'chapter_review.txt'. Please review and modify the content before proceeding.")
    edit_file("chapter_review.txt")
    
    # Load modified content
    with open("chapter_review.txt", "r") as f:
        modified_content = f.read()
    
    # Regenerate content with feedback
    if metrics["readability_score"] < 60:
        modified_content = rephrase(modified_content)
    if inconsistencies:
        modified_content = handle_repetition(modified_content)
    
    # Handle inconsistencies
    for inconsistency in inconsistencies:
        modified_content = resolve_inconsistency(modified_content, inconsistency)
    
    # Analyze themes using scikitlearn
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([modified_content])
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
    
    # Create a DataFrame for analysis
    df = pd.DataFrame({"Sentences": sent_tokenize(modified_content), "Words": [word_tokenize(sentence) for sentence in sent_tokenize(modified_content)]})
    
    # Perform named entity recognition
    doc = nlp(modified_content)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Perform sentiment analysis
    sentiments = [sentiment_analysis(sentence)[0] for sentence in sent_tokenize(modified_content)]
    
    # Update narrative tracker with the modified content
    narrative_tracker.track_characters(modified_content)
    narrative_tracker.track_locations(modified_content)
    narrative_tracker.track_plot_points(modified_content, "current_chapter")
    narrative_tracker.track_themes(modified_content)
    narrative_tracker.track_relationships(modified_content)
    narrative_tracker.track_emotional_arcs(modified_content)
    narrative_tracker.track_foreshadowing(modified_content, "current_chapter")
    narrative_tracker.track_world_changes(modified_content, "current_chapter")
    
    return modified_content
