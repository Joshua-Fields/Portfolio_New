from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use TLS instead of SSL
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USE_SSL'] = False  # Disable SSL
app.config['MAIL_USERNAME'] = 'joshuafields.dev@gmail.com'
app.config['MAIL_PASSWORD'] = 'ozau zvjd tgmt gxnc'  # Your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'joshuafields.dev@gmail.com'  # Must match MAIL_USERNAME

mail = Mail(app)

# Sample project data
projects = [
    {
        "name": "Cloud-Native E-commerce Platform",
        "description": "This project is a cloud-native e-commerce platform built using Flask, Docker, and Google Kubernetes Engine (GKE).",
        "github": "https://github.com/Joshua-Fields/cloud-native-ecommerce"
    },
    {
        "name": "RFIQD Flattening & Mock-File Reducer",
        "description": "This repository provides tools to reduce the size of .rfiqd files by creating 'mock' copies with limited data.",
        "github": "https://github.com/Joshua-Fields/RFIQD-Compression"
    },
    {
        "name": "Distributed Mandelbrot Fractal Renderer",
        "description": "Demonstrates distributed processing by rendering the Mandelbrot fractal across multiple Dask workers.",
        "github": "https://github.com/Joshua-Fields/Monte-Carlo/tree/main"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, github="https://github.com/Joshua-Fields", linkedin="https://www.linkedin.com/in/joshua-fields-/")

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message_body = request.form.get('message')

    msg = Message(
        subject=f"New Contact Request from {name}",
        sender=app.config['MAIL_DEFAULT_SENDER'],  # Always send from your Gmail
        recipients=["JoshuaFields.dev@gmail.com"]
    )
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        print(f"Error sending email: {e}")  # Print full error message to logs
        flash(f"Failed to send message: {str(e)}", "danger")

    return redirect(url_for('home'))



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Railway assigns dynamic port
    app.secret_key = os.urandom(24)  # Enables flash messages
    app.run(host="0.0.0.0", port=port, debug=True)  # Binds to Railway's port
