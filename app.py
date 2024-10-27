from flask import Flask, render_template, request, jsonify
import openai


openai.api_key = "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"

app = Flask(__name__)

def chatbot(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Free tier model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for processing chatbot requests
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
