from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_KEY, organization='org-pQMFdz3Snb6IkARxsvmZ5FzJ')

def generate_outline(user_inputs, synopsis, characters):
    context = f"User Inputs: {user_inputs}\n\nSynopsis: {synopsis}\n\nCharacter Sheets: {characters}"
    outline = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI assistant to a novelist.  Your task is to generate a complete chapter outline of the novel based on the book details provided."},
            {"role": "user", "content": context},
            {"role": "user", "content": "Please provide the outline in the following format:\n\nChapter {number}:\nTitle: {title}\nSummary: {summary}\nKey Events: {key_events}\nCharacters: {characters}\nLocations: {locations}\nThemes: {themes}\nConflicts: {conflicts}\nForeshadowing: {foreshadowing}"}
        ],
        model="gpt-4-turbo",
        temperature=0.5,
        max_tokens=4096,
        top_p=0.9
    ).choices[0].message.content.strip()
    
    # Assign attributes to each chapter
    chapters = outline.split('Chapter')
    chapter_attributes = []
    for chapter in chapters:
        if chapter.strip():
            lines = chapter.strip().split('\n')
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
            chapter_attributes.append(attributes)
    
    # Iterate over the chapter outline multiple times with various analysis methods
    for _ in range(3):  # Example: iterate 3 times
        for chapter in chapter_attributes:
            # Perform various analysis methods to improve the quality
            chapter["summary"] = enhance_clarity(chapter["summary"])
            chapter["key_events"] = optimize_pacing(chapter["key_events"])
            chapter["characters"] = enrich_vocabulary(chapter["characters"])
            chapter["locations"] = ensure_consistency(chapter["locations"])
            chapter["themes"] = improve_coherence(chapter["themes"])
            chapter["conflicts"] = enhance_clarity(chapter["conflicts"])
            chapter["foreshadowing"] = optimize_pacing(chapter["foreshadowing"])
    
    return chapter_attributes
