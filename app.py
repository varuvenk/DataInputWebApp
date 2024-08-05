from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        input_text = request.form.get("user_input", "")
        return redirect(url_for("display_input", input_text=input_text))
    return '''
    <h1>Input Page</h1>
    <p>Please enter some data in the field below:</p>
    <form action="/" method="POST">
        <input name="user_input" placeholder="Enter your data here">
        <input type="submit" value="Submit!">
    </form>
    '''

@app.route("/display_input/<input_text>", methods=["GET"])
def display_input(input_text):
    return f"<h1>You entered: {input_text}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
