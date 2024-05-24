from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_KEY, organization='org-pQMFdz3Snb6IkARxsvmZ5FzJ')

def generate_synopsis(prompt_text):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI trained to improve novel synopses based on the book details provided"},
            {"role": "user", "content": prompt_text},
            {"role": "user", "content": "Please provide a detailed synopsis including the main plot, subplots, character arcs, themes, and any foreshadowing elements."}
        ],
        model="gpt-4",
        temperature=0.5,
        max_tokens=2058,
        top_p=0.9
    ).choices[0].message.content.strip()
    
    return response








