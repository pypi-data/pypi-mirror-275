from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_KEY, organization='org-pQMFdz3Snb6IkARxsvmZ5FzJ')

def generate_beats(prompt_text, preceding_chapters, planned_chapters):
    context = f"Preceding Chapters: {preceding_chapters}\n\nPrompt Text: {prompt_text}\n\nPlanned Chapters: {planned_chapters}"
    beats = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI trained to generate story beats."},
            {"role": "user", "content": context},
            {"role": "user", "content": "Please provide the beats in the following format:\n\nBeat {number}:\nTitle: {title}\nSummary: {summary}\nKey Events: {key_events}\nCharacters: {characters}\nLocations: {locations}\nThemes: {themes}\nConflicts: {conflicts}\nForeshadowing: {foreshadowing}"}
        ],
        model="gpt-4-turbo",
        temperature=0.4,
        max_tokens=4096,
        top_p=0.9
    ).choices[0].message.content.strip()
    
    # Assign attributes to each beat
    beat_list = beats.split('Beat')
    beat_attributes = []
    for beat in beat_list:
        if beat.strip():
            lines = beat.strip().split('\n')
            attributes = {
                "title": lines[0].replace("Title: ", "").strip() if "Title: " in lines[0] else "",
                "summary": lines[1].replace("Summary: ", "").strip() if "Summary: " in lines[1] else "",
                "key_events": lines[2].replace("Key Events: ", "").strip().split(',') if "Key Events: " in lines[2] else [],
                "characters": lines[3].replace("Characters: ", "").strip().split(',') if "Characters: " in lines[3] else [],
                "locations": lines[4].replace("Locations: ", "").strip().split(',') if "Locations: " in lines[4] else [],
                "themes": lines[5].replace("Themes: ", "").strip().split(',') if "Themes: " in lines[5] else [],
                "conflicts": lines[6].replace("Conflicts: ", "").strip().split(',') if "Conflicts: " in lines[6] else [],
                "foreshadowing": lines[7].replace("Foreshadowing: ", "").strip().split(',') if "Foreshadowing: " in lines[7] else []
            }
            beat_attributes.append(attributes)
    
    # Iterate over the beat outline multiple times with various analysis methods
    for _ in range(3):  # Example: iterate 3 times
        for beat in beat_attributes:
            # Perform various analysis methods to improve the quality
            beat["summary"] = enhance_clarity(beat["summary"])
            beat["key_events"] = optimize_pacing(beat["key_events"])
            beat["characters"] = enrich_vocabulary(beat["characters"])
            beat["locations"] = ensure_consistency(beat["locations"])
            beat["themes"] = improve_coherence(beat["themes"])
            beat["conflicts"] = enhance_clarity(beat["conflicts"])
            beat["foreshadowing"] = optimize_pacing(beat["foreshadowing"])
    
    return beat_attributes
