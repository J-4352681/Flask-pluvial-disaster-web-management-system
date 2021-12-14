from flask import session, url_for

def url_or_home(permit, home="home", **params):
  print(permit, params, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
  if permit in session["user_permits"]:
    if params: return url_for(permit,  **params)
    else: return url_for(permit)
  else: return url_for(home)