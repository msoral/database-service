from src import db

social_links = ["twitter", "reddit", "instagram"]


class AssetMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    ticker = db.Column(db.String(4), nullable=False)
    website = db.Column(db.String)
    social = db.Column(db.JSON)
