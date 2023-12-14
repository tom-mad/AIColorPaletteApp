import openai
from dotenv import dotenv_values


if __name__ == "__main__":
    config = dotenv_values(".env")
    client = openai.OpenAI(
    api_key=config["OPENAI_API_KEY"],
    )

    prompt = """
You are a color palette generating assistant that responds to text prompts for coolor palettes

Desired Format: a JSON array of hexadecimal color codes
Text: a beatuiful sunset
"""
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", 
            "content": prompt}
        ],
        max_tokens=200
    )
    print(completion.choices[0].message.content)
