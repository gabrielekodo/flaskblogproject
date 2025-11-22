from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
# Create a Flask app instance
app = Flask(__name__, static_url_path='/static')
# Configure the database URI (e.g., for SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ekogab.db'
db=SQLAlchemy(app)


class User(db.Model):
    # Set the table name (optional, Flask-SQLAlchemy will pluralize the class name by default)
    __tablename__ = 'users'

    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstName = db.Column(db.String(64), unique=True, nullable=False)
    lastName = db.Column(db.String(64), unique=True, nullable=False)
    avatar = db.Column(db.String(64), unique=True, nullable=True)
    aboutMe = db.Column(db.String(1024), unique=True, nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    phone = db.Column(db.String(64), unique=True, nullable=False)
    street = db.Column(db.String(64), unique=True, nullable=False)
    zipCode = db.Column(db.String(64))
    city = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    linkedin = db.Column(db.String(64), unique=True, nullable=False)
    twitter = db.Column(db.String(64), unique=True, nullable=False)
    facebook = db.Column(db.String(64), unique=True, nullable=False)
    instagram = db.Column(db.String(64), unique=True, nullable=False)
    hobbies = db.Column(db.String(300), nullable=False)
    blogs = db.relationship('Blog', backref='owned_user', lazy=True)

    # A __repr__ method is good practice for debugging
    def __repr__(self):
        return f'<User {self.username}>'


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.String(64), nullable=False)
    ownerId = db.Column(db.Integer())
    likes = db.Column(db.Integer(), default=0)
    shares = db.Column(db.Integer(), default=0)
    createdAt = db.Column(db.DateTime())
    comments = db.Column(db.String())
    tags = db.Column(db.String(64))
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    # A __repr__ method is good practice for debugging
    def __repr__(self):
        return f'<User {self.username}>'




blogs=[
  {
    "id": 1,
    "title": "Sample Blog Title 1",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 9,
    "comments": [
      11
    ],
    "likes_counts": 352,
    "shares": 68,
    "tags": [
      "gKqzKLnGMNyssq",
      "TTdVQWkaadzUePdFWxSPxMCjz",
      "MyznSDjUoIZVAFgvMitCHFO",
      "QMFgKYFDfTidZbJLcBOQivLowq"
    ],
    "created_at": "2024-02-05"
  },
  {
    "id": 2,
    "title": "Sample Blog Title 2",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 34,
    "comments": [],
    "likes_counts": 153,
    "shares": 142,
    "tags": [
      "IDLPcdQGchPeOlgncw"
    ],
    "created_at": "2020-10-21"
  },
  {
    "id": 3,
    "title": "Sample Blog Title 3",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 14,
    "comments": [
      34,
      16,
      37,
      49,
      32,
      2
    ],
    "likes_counts": 352,
    "shares": 132,
    "tags": [
      "KyYYFCzMCdEu"
    ],
    "created_at": "2024-01-15"
  },
  {
    "id": 4,
    "title": "Sample Blog Title 4",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 31,
    "comments": [
      2
    ],
    "likes_counts": 181,
    "shares": 105,
    "tags": [
      "oilXOJvjOUYBn"
    ],
    "created_at": "2021-11-10"
  },
  {
    "id": 5,
    "title": "Sample Blog Title 5",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 22,
    "comments": [
      32,
      6,
      28,
      31,
      21,
      23
    ],
    "likes_counts": 52,
    "shares": 100,
    "tags": [
      "rvXmtkTKOnjPqWrQSiDo"
    ],
    "created_at": "2021-11-20"
  },
  {
    "id": 6,
    "title": "Sample Blog Title 6",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 40,
    "comments": [
      17,
      3
    ],
    "likes_counts": 402,
    "shares": 121,
    "tags": [
      "xLiDPUJkYToHkmg",
      "PtXXelfQEWwqOdKpfyyavcDkmrgF",
      "eUOm",
      "AbcfcHnRXiozbGTmENPExzyrepXSw"
    ],
    "created_at": "2025-08-16"
  },
  {
    "id": 7,
    "title": "Sample Blog Title 7",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 31,
    "comments": [
      32,
      24,
      24,
      6,
      14,
      8
    ],
    "likes_counts": 231,
    "shares": 33,
    "tags": [
      "wDCqdgnXmBUHQDhxt"
    ],
    "created_at": "2024-01-31"
  },
  {
    "id": 8,
    "title": "Sample Blog Title 8",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 22,
    "comments": [
      17,
      48
    ],
    "likes_counts": 161,
    "shares": 80,
    "tags": [
      "ZHMGsdKyNYhNSXqWXhYFHMsPu"
    ],
    "created_at": "2023-06-13"
  },
  {
    "id": 9,
    "title": "Sample Blog Title 9",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 20,
    "comments": [
      44,
      21,
      24,
      21
    ],
    "likes_counts": 157,
    "shares": 144,
    "tags": [
      "IYUvILzTWEYrbuHVBdOZpeGV",
      "fcjXdhynDeiWBkmGZB",
      "QdZKBciBoKLuSBiM"
    ],
    "created_at": "2024-04-05"
  },
  {
    "id": 10,
    "title": "Sample Blog Title 10",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 21,
    "comments": [
      44,
      16,
      33,
      39,
      2,
      34
    ],
    "likes_counts": 302,
    "shares": 136,
    "tags": [
      "OnSIeEapbdLacglZntUjDcl"
    ],
    "created_at": "2020-11-09"
  },
  {
    "id": 11,
    "title": "Sample Blog Title 11",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 41,
    "comments": [
      31,
      26,
      3,
      40
    ],
    "likes_counts": 384,
    "shares": 19,
    "tags": [
      "VkvfIDNclFqVPCKFPlgTMUAQcIpU",
      "NWJAOtePHCCsMIZdbVUiGpZBf",
      "twIrMqhGhIvitQfaKabkxfcoq"
    ],
    "created_at": "2023-09-21"
  },
  {
    "id": 12,
    "title": "Sample Blog Title 12",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 7,
    "comments": [],
    "likes_counts": 101,
    "shares": 24,
    "tags": [
      "fiWOkjHNKdEOcNCQvaUkEkVyg",
      "tgmLkzCHocIWv",
      "EolUbRMqjLgS",
      "OuDrSdIFfsVDhJKPcgFJht"
    ],
    "created_at": "2025-11-01"
  },
  {
    "id": 13,
    "title": "Sample Blog Title 13",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 16,
    "comments": [
      5,
      34,
      38,
      13,
      13
    ],
    "likes_counts": 183,
    "shares": 142,
    "tags": [
      "aqXYr",
      "dIwrlexZcQJZ",
      "mDynFKhCPYmy"
    ],
    "created_at": "2022-05-16"
  },
  {
    "id": 14,
    "title": "Sample Blog Title 14",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 44,
    "comments": [
      35
    ],
    "likes_counts": 356,
    "shares": 97,
    "tags": [
      "NvplGhZMsrXZhkZIQsoAwrGfXKUk",
      "pag",
      "fTrXaVBImQ",
      "cqyFICaIGnQAHXukesmrPfWvHW"
    ],
    "created_at": "2023-11-18"
  },
  {
    "id": 15,
    "title": "Sample Blog Title 15",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 45,
    "comments": [
      14
    ],
    "likes_counts": 5,
    "shares": 136,
    "tags": [
      "UeyLYudSNVgNywMRRbOJQBEZU",
      "lfVZUqxigCqRuoGJyxgTVxhCEzFN"
    ],
    "created_at": "2023-06-09"
  },
  {
    "id": 16,
    "title": "Sample Blog Title 16",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 32,
    "comments": [
      34
    ],
    "likes_counts": 123,
    "shares": 102,
    "tags": [
      "OoSCzwhMotAbjPLZjlCrLVfb",
      "vaAbhscilqZQPMqcZHZ",
      "eOfAGhzoQqvivdY",
      "rfvqegHqsxeZqqsO"
    ],
    "created_at": "2020-03-09"
  },
  {
    "id": 17,
    "title": "Sample Blog Title 17",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 37,
    "comments": [
      10,
      24
    ],
    "likes_counts": 57,
    "shares": 176,
    "tags": [
      "vqLEjLmblanYkTqjOYixsUdUdrjRs",
      "sGuMUsVbjAoKxaawnverNhlWfaj",
      "DmKYFEmCPZwLRxUPd"
    ],
    "created_at": "2020-05-31"
  },
  {
    "id": 18,
    "title": "Sample Blog Title 18",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 21,
    "comments": [
      8,
      4
    ],
    "likes_counts": 322,
    "shares": 127,
    "tags": [
      "kCVxuJMoDjcchuCVY",
      "SZyaEwsopBEFIGDqzWcvyAEXVN",
      "cKK",
      "axqtDqch"
    ],
    "created_at": "2020-12-18"
  },
  {
    "id": 19,
    "title": "Sample Blog Title 19",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 12,
    "comments": [
      1,
      50,
      29
    ],
    "likes_counts": 269,
    "shares": 80,
    "tags": [
      "ETzoUgavZVMtUqMbTajDrcFIBQiJ"
    ],
    "created_at": "2023-05-25"
  },
  {
    "id": 20,
    "title": "Sample Blog Title 20",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 11,
    "comments": [
      48,
      15,
      34,
      45
    ],
    "likes_counts": 396,
    "shares": 198,
    "tags": [
      "sDXGqNnRMXkdw",
      "iadRnzEzQm",
      "DnQZKgXYfUs"
    ],
    "created_at": "2020-07-20"
  },
  {
    "id": 21,
    "title": "Sample Blog Title 21",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 49,
    "comments": [
      15,
      34,
      50,
      31
    ],
    "likes_counts": 411,
    "shares": 175,
    "tags": [
      "DscwsQDYijocsxEKGlEmG",
      "tkDpsWATvFBrNMaYNBRgsDm",
      "dSdVmHJBbEkVbyhtcIGXOGCa",
      "kBPCvjGJzvrECQzJYVcTREahWQ"
    ],
    "created_at": "2022-02-22"
  },
  {
    "id": 22,
    "title": "Sample Blog Title 22",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 35,
    "comments": [
      31,
      47,
      29,
      3
    ],
    "likes_counts": 394,
    "shares": 31,
    "tags": [
      "UHAZVo"
    ],
    "created_at": "2021-04-29"
  },
  {
    "id": 23,
    "title": "Sample Blog Title 23",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 24,
    "comments": [
      36
    ],
    "likes_counts": 268,
    "shares": 170,
    "tags": [
      "McKQBxgiEqacSoddG",
      "tiogscRdPymagNmYDkXf",
      "ZVezg"
    ],
    "created_at": "2020-06-21"
  },
  {
    "id": 24,
    "title": "Sample Blog Title 24",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 16,
    "comments": [
      21,
      1
    ],
    "likes_counts": 421,
    "shares": 96,
    "tags": [
      "CrCFWWgicZTxElTemsxlMcY",
      "YBemzGaCFS",
      "uPGJTlDVWVqToojXdlamZTC"
    ],
    "created_at": "2023-10-23"
  },
  {
    "id": 25,
    "title": "Sample Blog Title 25",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 27,
    "comments": [
      34,
      9
    ],
    "likes_counts": 362,
    "shares": 4,
    "tags": [
      "mqdSoP",
      "ZNFKGpyaXEewayXCButBbXJ"
    ],
    "created_at": "2025-09-15"
  },
  {
    "id": 26,
    "title": "Sample Blog Title 26",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 6,
    "comments": [],
    "likes_counts": 424,
    "shares": 148,
    "tags": [
      "pdbZNMn",
      "xgTfLbClkgROTFZxoeIMpE"
    ],
    "created_at": "2023-02-11"
  },
  {
    "id": 27,
    "title": "Sample Blog Title 27",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 24,
    "comments": [
      13,
      45,
      11
    ],
    "likes_counts": 20,
    "shares": 127,
    "tags": [
      "TykZLgwzvhtnuOHewuWYHLVR",
      "jfbXxBthOn",
      "XSdaawwV",
      "QdxbvwWgCxWfpvlDZBlVRNomM"
    ],
    "created_at": "2021-09-30"
  },
  {
    "id": 28,
    "title": "Sample Blog Title 28",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 11,
    "comments": [
      12,
      13
    ],
    "likes_counts": 67,
    "shares": 33,
    "tags": [
      "xIJmbXgXMEErSQw",
      "wAUZgwTUPBSAcGBLnOQjikrJnPf"
    ],
    "created_at": "2020-09-09"
  },
  {
    "id": 29,
    "title": "Sample Blog Title 29",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 25,
    "comments": [
      9,
      36,
      43
    ],
    "likes_counts": 385,
    "shares": 43,
    "tags": [
      "knkvssURnRmOKBnkEQZhy"
    ],
    "created_at": "2024-07-22"
  },
  {
    "id": 30,
    "title": "Sample Blog Title 30",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 27,
    "comments": [
      39,
      30,
      36,
      19,
      50,
      2
    ],
    "likes_counts": 187,
    "shares": 40,
    "tags": [
      "fxVswBrfMijfdrhZLzNZjdlr",
      "BrqFOmkWnmTLvlqfvCWwVflsucyl"
    ],
    "created_at": "2024-02-28"
  },
  {
    "id": 31,
    "title": "Sample Blog Title 31",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 17,
    "comments": [
      22,
      34
    ],
    "likes_counts": 443,
    "shares": 70,
    "tags": [
      "UODnKjdtbXbGqWpqvUF"
    ],
    "created_at": "2020-01-18"
  },
  {
    "id": 32,
    "title": "Sample Blog Title 32",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 7,
    "comments": [
      10,
      43
    ],
    "likes_counts": 253,
    "shares": 189,
    "tags": [
      "GRVSJJwyOYZsYHinQssSGtERu",
      "JSFDkZ",
      "yxDmSEOjDJuLSMaW",
      "ecFrlG"
    ],
    "created_at": "2025-09-04"
  },
  {
    "id": 33,
    "title": "Sample Blog Title 33",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 44,
    "comments": [
      30,
      6,
      14,
      4,
      33
    ],
    "likes_counts": 48,
    "shares": 69,
    "tags": [
      "LWEzpEqWaiztIlR",
      "IaqKZUAIZJGhilTrFCCjwVXQ",
      "WZCL",
      "ndJLsSkyAwM"
    ],
    "created_at": "2025-05-14"
  },
  {
    "id": 34,
    "title": "Sample Blog Title 34",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 21,
    "comments": [
      35,
      49,
      44,
      21,
      40
    ],
    "likes_counts": 274,
    "shares": 93,
    "tags": [
      "VpMw",
      "yBOeLADSWXZ"
    ],
    "created_at": "2023-03-26"
  },
  {
    "id": 35,
    "title": "Sample Blog Title 35",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 48,
    "comments": [
      21,
      1,
      35
    ],
    "likes_counts": 360,
    "shares": 127,
    "tags": [
      "bKhkVHvBRfrhVGditzFiCkpzwgEqe"
    ],
    "created_at": "2020-04-10"
  },
  {
    "id": 36,
    "title": "Sample Blog Title 36",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 50,
    "comments": [],
    "likes_counts": 498,
    "shares": 66,
    "tags": [
      "anHAKddPERqChMoEAOSV",
      "FanJIaf",
      "uqaxDfuln",
      "skAJsyDOWaIe"
    ],
    "created_at": "2022-01-21"
  },
  {
    "id": 37,
    "title": "Sample Blog Title 37",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 37,
    "comments": [
      36,
      47,
      30,
      20,
      45
    ],
    "likes_counts": 29,
    "shares": 60,
    "tags": [
      "cEQLAoluAbjVPAx",
      "ZLfsGnU",
      "lHdvobovQv"
    ],
    "created_at": "2022-04-24"
  },
  {
    "id": 38,
    "title": "Sample Blog Title 38",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 37,
    "comments": [
      40,
      27,
      25,
      3,
      21,
      41
    ],
    "likes_counts": 72,
    "shares": 134,
    "tags": [
      "AodQhbhTSaMuLISUfvkgUDbMVP"
    ],
    "created_at": "2022-09-16"
  },
  {
    "id": 39,
    "title": "Sample Blog Title 39",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 48,
    "comments": [
      39
    ],
    "likes_counts": 173,
    "shares": 147,
    "tags": [
      "BEKLNBkvqgjRmtM",
      "mCM"
    ],
    "created_at": "2020-05-29"
  },
  {
    "id": 40,
    "title": "Sample Blog Title 40",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 44,
    "comments": [
      1,
      30
    ],
    "likes_counts": 149,
    "shares": 27,
    "tags": [
      "euyCusNbmWRSnSkvAU",
      "OGmwDIlpiJOeOwLd",
      "hlIzVpTHxpx"
    ],
    "created_at": "2021-06-26"
  },
  {
    "id": 41,
    "title": "Sample Blog Title 41",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 33,
    "comments": [
      36
    ],
    "likes_counts": 88,
    "shares": 150,
    "tags": [
      "jJwSxeCgk",
      "jJvJmGqe"
    ],
    "created_at": "2025-05-26"
  },
  {
    "id": 42,
    "title": "Sample Blog Title 42",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 18,
    "comments": [
      23
    ],
    "likes_counts": 185,
    "shares": 5,
    "tags": [
      "YTIBehDsjKnaXxPS",
      "IEjsEKoeiD",
      "hwRHnfUOTYdT"
    ],
    "created_at": "2023-01-07"
  },
  {
    "id": 43,
    "title": "Sample Blog Title 43",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 28,
    "comments": [
      31,
      24,
      10
    ],
    "likes_counts": 485,
    "shares": 141,
    "tags": [
      "VLojPQCPOaGPubfYVJcalqQumAS"
    ],
    "created_at": "2020-01-19"
  },
  {
    "id": 44,
    "title": "Sample Blog Title 44",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 37,
    "comments": [
      50
    ],
    "likes_counts": 460,
    "shares": 12,
    "tags": [
      "yMqkElXiRlLwVeGIFEkJSj",
      "OBnfmtuyJYJNipfXEHTQEYtF",
      "TvvPXff"
    ],
    "created_at": "2025-06-13"
  },
  {
    "id": 45,
    "title": "Sample Blog Title 45",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 11,
    "comments": [],
    "likes_counts": 451,
    "shares": 157,
    "tags": [
      "gMHLEpqNdVfMDVrIqFLV",
      "CggjBnMEFZwfhYurXfaqfZsNo"
    ],
    "created_at": "2023-12-08"
  },
  {
    "id": 46,
    "title": "Sample Blog Title 46",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 39,
    "comments": [
      18
    ],
    "likes_counts": 224,
    "shares": 63,
    "tags": [
      "OGPlg"
    ],
    "created_at": "2022-03-04"
  },
  {
    "id": 47,
    "title": "Sample Blog Title 47",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 11,
    "comments": [],
    "likes_counts": 114,
    "shares": 47,
    "tags": [
      "vBHktIlrY",
      "ttboQpilxdBxfQm",
      "aSXTH"
    ],
    "created_at": "2024-09-09"
  },
  {
    "id": 48,
    "title": "Sample Blog Title 48",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 5,
    "comments": [
      5,
      45,
      12,
      2,
      10,
      12
    ],
    "likes_counts": 19,
    "shares": 187,
    "tags": [
      "DJHnVQkipQyMppuQefvHtoO",
      "bhiipO",
      "ryPApdlEo"
    ],
    "created_at": "2024-02-11"
  },
  {
    "id": 49,
    "title": "Sample Blog Title 49",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 31,
    "comments": [
      19,
      34,
      24,
      4
    ],
    "likes_counts": 248,
    "shares": 130,
    "tags": [
      "jVhyDAeuPkRrWJLzxGMvVaihTeky",
      "uRpcuhPnteyFkKjilbH",
      "RFUQIq",
      "REJRSSFpXGozHNlCtF"
    ],
    "created_at": "2022-01-24"
  },
  {
    "id": 50,
    "title": "Sample Blog Title 50",
    "body": "This is a detailed blog body intended to exceed the minimum character requirement of 250 characters. It includes multiple sentences to ensure that the total length is well above the threshold. The purpose of this generated text is to populate the JSON file with realistic content for testing or development environments. Each blog entry maintains structure, clarity, and consistency for reliable application behavior.",
    "owner_id": 44,
    "comments": [],
    "likes_counts": 386,
    "shares": 171,
    "tags": [
      "ayVOPS"
    ],
    "created_at": "2020-04-05"
  }
]

# fetching data
def list_user():
    users=User.query.all()
    return users
current_user=[]
# print(current_user)




@app.context_processor
def inject_global_vars():
    current_user=list_user()[0]

    if len(current_user['about_me']) > 200:
        truncated_text = current_user['about_me'][:200 - 3] + "..."  # -3 for the ellipsis
    else:
        truncated_text = current_user['about_me']
    return dict(site_name="Ekogab Blogs", about_me=truncated_text,logged_user=current_user)





@app.route('/createUser',methods=['GET'])
def add_blogs():
    print(datetime.datetime.now())





    return 'user added'




@app.route('/')
@app.route('/home')
def home_page():

    return 'hello ..............'


    # return render_template('home.html',logged_user=current_user, blog_posts=blogs,blogs=[])


@app.route('/about')
def about_page():
    return render_template('about.html',logged_user=current_user)

@app.route('/blog')
def blog_page():
    # userblogs=[blog for blog in logged_user_blogs]
    return render_template('blog.html',logged_user=current_user, blogs=logged_user_blogs)

@app.route('/contact')
def contact_page():
    return render_template('contact.html',logged_user=current_user)


@app.route('/blog/<int:blog_id>')
def singleblog_page(blog_id):
    return render_template('single.html',blog_id=blog_id)


# Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')