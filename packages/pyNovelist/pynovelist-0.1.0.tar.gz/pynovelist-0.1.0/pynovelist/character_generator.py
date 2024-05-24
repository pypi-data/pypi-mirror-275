from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_KEY, organization='org-pQMFdz3Snb6IkARxsvmZ5FzJ')

def generate_character(user_inputs, synopsis, characters):
    context = f"Initial book details: {user_inputs}\n\nInitial character details: {characters}\n\nRefined synopsis: {synopsis}\n\nExpected response: A list of characters based on but not limited to the character details provided unless otherwise stated previously.  Each character should have a defined role, physical description, backstory, character arc, subplots, relationships, goals, fears, strengths, weaknesses, personality, and any other relevant details."
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an AI assistant to a novelist.  Your task is to generate a detailed character sheet encompassing all of the characters, and their attributes, for a novel based on the details provided.."},
            {"role": "user", "content": context}
        ],
        model="gpt-4-turbo",
        temperature=0.4,
        max_tokens=4096,
        top_p=0.9
    ).choices[0].message.content.strip()
    
    
    return response


