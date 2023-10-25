from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
db = SQLAlchemy()

class Movie(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    description: Mapped[str] = mapped_column(db.String, nullable=False)
    rating: Mapped[float] = mapped_column(db.Float, nullable=True)
    ranking: Mapped[int] = mapped_column(db.Integer, nullable=True)
    review: Mapped[str] = mapped_column(db.String, nullable=True)
    img_url: Mapped[str] = mapped_column(db.String, nullable=False)