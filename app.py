from flask import Flask, render_template_string, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['student_database']
collection = db['student_collection']

# HTML templates as strings
index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Application Form</title>
</head>
<body>
    <h1>Student Application Form</h1>
    <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <!-- Add more form fields as needed -->

        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

success_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Application Submitted Successfully</h1>
    <p>Thank you, {{ name }}, for submitting your application!</p>
</body>
</html>
'''

# Flask routes
@app.route('/')
def index():
    # Render the index page
    return render_template_string(index_html)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Extract form data from the request
        name = request.form['name']
        email = request.form['email']
        # Add more form fields as needed

        # Perform backend processing here
        # Save the form data to MongoDB
        student_data = {
            'name': name,
            'email': email,
            # Add more fields as needed
        }

        # Store data in MongoDB
        collection.insert_one(student_data)

        # Render the success page with the processed data
        return render_template_string(success_html, name=name)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
