#AIzaSyBdAhvbIbfDhduU957FmYdU001xEIcfpQo


from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure the Gemini AI API
genai.configure(api_key="AIzaSyBdAhvbIbfDhduU957FmYdU001xEIcfpQo")
model_name = "gemini-1.5-flash"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the user's message from the frontend
        user_message = request.json.get("message")
        
        # Generate AI response
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(user_message)
        
        # Return the AI's response
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
