import json
import openai
from dotenv import dotenv_values
from flask import Flask, render_template, request

config = dotenv_values(".env")

client = openai.OpenAI(
    api_key=config["OPENAI_API_KEY"],
)

app = Flask(__name__,
    template_folder='templates',
    static_url_path='',
    static_folder='static'
)

def get_colors(msg):
    prompt = f"""
You are a color palette generating assistant that responds to text prompts for color palettes
Your should generate color palettes that fit the theme, mood, or instructions in the prompt.
The palettes should be between 2 and 8 colors.

Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]

Desired Format: a JSON array of hexadecimal color codes

Q: Convert the following verbal description of a color palette into a list of colors: {msg}
A:
"""
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", 
            "content": prompt}
        ],
        max_tokens=200
    )
    return json.loads(completion.choices[0].message.content)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/palette", methods={"POST"})
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}

if __name__=="__main__":
    app.run(debug=True)
