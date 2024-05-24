import json

def collect_inputs():
    inputs = {}
    inputs['title'] = 'Book Title: ' +input("Enter the title of your novel: ")
    inputs['genre'] ='Genre: ' + input("Enter the genre of your novel: ")
    synopsis = 'Synopsis' + input("Enter a synopsis of your novel: ")
    characters = 'Characters' +input("Enter details about the characters: ")
    inputs['locations'] = 'Locations: ' + input("Enter details about the locations: ")
    inputs['chapters'] = 'Chapters: ' + input("Enter details about the chapters: ")
    inputs['key_events'] = 'Key Events: ' + input("Enter details about the key events: ")
    inputs['plot'] = 'Plot: ' + input("Enter details about the plot: ")
    inputs['themes'] = 'Themes: ' + input("Enter details about the themes: ")
    inputs['pov'] = 'Point of View: ' + input("Enter details about the point of view: ")
    inputs['reader'] = 'Intended Audience: ' + input("Enter details about the intended reader: ")
    inputs['writing_style'] = 'Writing Style: ' + input("Enter the writing style: ")
    inputs['num_chapters'] = 'Number of chapters: ' + input("Enter the number of desired chapters: ")
    inputs['num_words'] = 'Word Count per Chapter: ' + input("Enter the number of words per chapter: ")
    # Add more prompts as needed
    return inputs, synopsis, characters


# def validate_inputs(inputs):
#     required_fields = [inputs['title'], inputs[genre]]
#     for field in required_fields:
#         if field not in inputs or not inputs[field].strip():
#             raise ValueError(f"Missing or empty required field: {field}")
#     return True



def serialize_inputs(inputs, synopsis, characters):
    return json.dumps(inputs, indent=4)

