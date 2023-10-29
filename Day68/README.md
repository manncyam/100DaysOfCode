# Day68 Login with Authentication

## Encryption and Hashing

- [Cryptii](https://cryptii.com/)
- [Enigma Code](https://www.youtube.com/watch?v=V4V2bpZlqx8)

## Security

- [haveibeenpwned](https://haveibeenpwned.com/)
- [check your password strength](http://password-checker.online-domain-tools.com/)

## [Flask Login](https://flask-login.readthedocs.io/en/latest/)

```python
pip install flask-login
```

In the document, How it works, says we need to provide user_loader callback:

```python
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
```

This is just an example, so we need to do this instead:

```python
@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar_one_or_none()
    return user
```

user can be the object of User or None. Getting user from database is up to the developers' choice.

## flash.flash

[Message flashing](https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/) is also helpful to get the message out the template.
