# Day63 Virtual Bookshelf

## Learn to use database to store data

First we need to install Flask-SQLAlchemy

```python
pip install -U Flask-SQLAlchemy
```

## Challenges

- It is a bit difficult to read from the db to html using jinja. It tooks me so long to check this condition
  
  ```jinja2
  {% if books != [] %}
  ```
