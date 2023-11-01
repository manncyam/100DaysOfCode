# Day69 Adding Users to Our Blog

## Bootstrap-flask

- Use [render_form](https://bootstrap-flask.readthedocs.io/en/stable/macros/#render-form)
- To validate email, we need to install email_validator
  
  ```python
  pip install email_validator
  ```

## [Werkzeug](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#module-werkzeug.security)

- Use ```generate_password_hash(password, method='pbkdf2', salt_length=16)``` to hash and salt password before inserting into a database.
- Use ```check_password_hash(pwhash, password)``` to verify password.

## [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

- flask [login_required](https://flask.palletsprojects.com/en/2.3.x/patterns/viewdecorators/) function decorator
  
## Flask Message

- Use [message flashing](https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/) from flask to give user feedback
