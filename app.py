import json
import openai
from dotenv import dotenv_values
from flask import Flask, render_template, request

config = dotenv_values(".env")

client = openai.OpenAI(
    api_key=config["OPENAI_API_KEY"],
)

app = Flask(__name__,
    template_folder='templates'
)

@app.route("/")
def index():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", 
            "content": "Give me a funny word: "}
        ],
    )
    return completion.choices[0].message.content
    # return render_template("index.html")

# @app.route("/palette", methods={"POST"})
# def prompt_to_palette():
    # OPEN AI COMPLETION CALL

    # RETURN LIST OF COLORS

if __name__=="__main__":
    app.run(debug=True)
