from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
projects = [
    {"name": "Project 1", "description": "A cool project.", "github": "https://github.com/yourprofile/project1"},
    {"name": "Project 2", "description": "Another cool project.", "github": "https://github.com/yourprofile/project2"}
]



@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # You can log or email this data
    print(f"New contact from {name} ({email}): {message}")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
