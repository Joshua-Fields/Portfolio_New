from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
import logging
import traceback  # Allows us to capture full error details
import re # Regex for email validation

app = Flask(__name__)

# Setup logging to write errors to a file (for Railway logs)
logging.basicConfig(filename="error.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s: %(message)s")

# Configure Flask-Mail with environment variables for security
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config['MAIL_PORT'] = int(os.getenv("MAIL_PORT", 587))
app.config['MAIL_USE_TLS'] = os.getenv("MAIL_USE_TLS", "True") == "True"
app.config['MAIL_USE_SSL'] = os.getenv("MAIL_USE_SSL", "False") == "True"
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME", "joshuafields.dev@gmail.com")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD", "ozau zvjd tgmt gxnc")
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

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
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message_body = request.form.get('message', '').strip()

        # Validate and sanitize user email
        def clean_email(email):
            return re.sub(r"\s", "", email)  # Remove spaces and newlines

        if not name or not email or not message_body:
            flash("❌ All fields are required.", "danger")
            return redirect(url_for('home'))

        # Prevent header injection attacks
        if "\n" in name or "\r" in name or "\n" in email or "\r" in email:
            flash("❌ Invalid characters in input.", "danger")
            return redirect(url_for('home'))

        # Use a fixed sender (Gmail requires the sender to be a registered address)
        sender_email = app.config.get("MAIL_DEFAULT_SENDER", "joshuafields.dev@gmail.com")

        msg = Message(
            subject=f"New Contact Request from {name}",
            sender=clean_email(sender_email),  # Ensure a valid sender
            recipients=["JoshuaFields.dev@gmail.com"]
        )
        msg.body = f"Name: {name}\nEmail: {clean_email(email)}\n\nMessage:\n{message_body}"

        mail.send(msg)
        flash("✅ Message sent successfully!", "success")
        return redirect(url_for('home'))

    except Exception as e:
        error_details = traceback.format_exc()
        print(f"❌ Email sending error: {error_details}")
        logging.error(f"❌ Email sending error: {error_details}")
        flash(f"❌ Failed to send message: {str(e)}", "danger")
        return redirect(url_for('home'))



@app.route('/test-email')
def test_email():
    try:
        sender_email = app.config.get("MAIL_DEFAULT_SENDER", "joshuafields.dev@gmail.com").strip()

        # Validate and sanitize email fields
        def clean_email(email):
            return re.sub(r"\s", "", email)  # Remove all spaces

        recipient_email = "JoshuaFields.dev@gmail.com"
        subject = "Test Email from Railway"

        # Ensure no invalid characters in subject
        if "\n" in subject or "\r" in subject:
            raise ValueError("Invalid subject header")

        msg = Message(
            subject=subject,
            sender=clean_email(sender_email),  # Ensure sender is properly formatted
            recipients=[clean_email(recipient_email)]
        )
        msg.body = "This is a test email from Railway."

        mail.send(msg)
        return "✅ Test email sent successfully!", 200

    except Exception as e:
        error_details = traceback.format_exc()
        print(f"❌ Email sending error: {error_details}")
        logging.error(f"❌ Email sending error: {error_details}")
        return f"❌ Email error:\n{error_details}", 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.secret_key = os.urandom(24)
    app.run(host="0.0.0.0", port=port, debug=True)
