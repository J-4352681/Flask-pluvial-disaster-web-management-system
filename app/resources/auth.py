import json
from os import environ
from flask import redirect, render_template, request, url_for, abort, session, message_flashed, flash
from oauthlib.oauth2 import WebApplicationClient
import requests

from app.models.user import User
from config import config


env = environ.get("FLASK_ENV", "development")

def get_google_provider_cfg():
    return requests.get(config[env].GOOGLE_DISCOVERY_URL).json()

client = WebApplicationClient(config[env].GOOGLE_CLIENT_ID)


def login():
    return render_template("auth/login.html")

def google_login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=config[env].GOOGLE_REDIRECT_URI,
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

def authenticate():
    params = request.form

    user = User.can_login_with_email_and_password(params["email"], params["password"])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))
    
    if not user.approved:
        flash("Usuario esta esperando aprovacion.")
        return redirect(url_for("auth_login"))

    return login_user(user)

def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(config[env].GOOGLE_CLIENT_ID, config[env].GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        users_first_name = userinfo_response.json()["given_name"]
        users_last_name = userinfo_response.json()["family_name"]
    else:
        return "User email not available or not verified by Google.", 400
        
    user = User.find_by_id(unique_id)

    # Doesn't exist? Add it to the database.
    if not user:
        User.create_social(id=unique_id, email=users_email, fist_name=users_first_name, last_name=users_last_name)

    # Begin user session by logging the user in
    return login_user(user)

def logout():
    del session["user"]
    del session["user_permits"]
    del session["navigation_actions"]
    session.clear()

    return redirect(url_for("auth_login"))

def login_user(user):
    session["user"] = user
    session["user_permits"] = user.get_permits()
    return redirect(url_for("home"))