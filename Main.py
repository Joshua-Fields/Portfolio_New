from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
#2J64EYC8LH5HN5CE3PB6V9NA recovery code
# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use TLS instead of SSL
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USE_SSL'] = False  # Disable SSL
app.config['MAIL_USERNAME'] = 'joshuafields.dev@gmail.com'
app.config['MAIL_PASSWORD'] = 'fill in your gmail app password'  # Your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'joshuafields.dev@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'joshuafields.dev@gmail.com'  # Must match MAIL_USERNAME

mail = Mail(app)

# Sample data
projects = [
    {"name": "Cloud-Native E-commerce Platform", "This project is a cloud-native e-commerce platform built using Flask, Docker, and Google Kubernetes Engine (GKE).": "Cloud-Native E-commerce Platform", "github": "https://github.com/Joshua-Fields/cloud-native-ecommerce"},
    {"name": "RFIQD Flattening & Mock-File Reducer", "This repository provides tools to reduce the size of .rfiqd files by creating “mock” copies with limited data.": "RFIQD Flattening & Mock-File Reducer", "github": "https://github.com/Joshua-Fields/RFIQD-Compression"},
    {"name": "Distributed Mandelbrot Fractal Renderer", "Demonstrates distributed processing by rendering the Mandelbrot fractal across multiple Dask workers.": "Distributed Mandelbrot Fractal Renderer", "github": "https://github.com/Joshua-Fields/Monte-Carlo/tree/main"}
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, github="https://github.com/Joshua-Fields", linkedin="https://www.linkedin.com/in/joshua-fields-/")

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message_body = request.form.get('message')

    # Compose email
    msg = Message(f"New Contact Request from {name}",
                  sender=email,
                  recipients=["JoshuaFields.dev@gmail.com"])  # Your work email
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Failed to send message: {str(e)}", "danger")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.secret_key = os.urandom(24)  # Enables flash messages
    app.run(debug=True)
