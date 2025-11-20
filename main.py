from flask import Flask, render_template, Response, request, jsonify, redirect, url_for

# Create a Flask app instance
app = Flask(__name__, static_url_path='/static')

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
users=[
  {
    "id": 1,
    "firstName": "Elijah",
    "lastName": "Vance",
    "avatar": "https://avatar.iran.liara.run/username?username=Elijah+Vance",
    "age": 35,
    "email": "elijah.vance@inno-labs.com",
    "phone": "555-202-3001",
    "street": "100 Innovation Drive",
    "zip code": "02139",
    "city": "Cambridge",
    "country": "USA",
    "linkedin_url": "https://www.linkedin.com/in/elijahvance-ai",
    "twitter_url": "https://twitter.com/vance_dev",
    "instagram_url": "https://www.instagram.com/elijah.outdoors",
    "facebook_url": "https://www.facebook.com/elijah.vance.official",
    "about_me": "Elijah is a Senior AI Engineer specializing in Natural Language Processing and large-scale data modeling. With over a decade of experience, he has led multiple projects deploying machine learning solutions in financial technology and healthcare. His expertise includes TensorFlow, PyTorch, and cloud-native architecture on GCP. He is dedicated to ethical AI practices and ensuring model transparency and fairness. Beyond the server room, Elijah is an enthusiastic trail runner, believing that regular physical challenge fuels better problem-solving in his technical work. He mentors young professionals in data science and is currently writing a book on applied predictive analytics, focusing on real-world business impact and measurable ROI from complex models.",
    "hobbies": [
      "Trail Running",
      "Ethical AI Research",
      "Guitar",
      "Backpacking"
    ]
  },
  {
    "id": 2,
    "firstName": "Sofia",
    "lastName": "Chen",
    "avatar": "https://example.com/avatars/sofia.png",
    "age": 29,
    "email": "sofia.chen@globaldesign.co",
    "phone": "555-202-3002",
    "street": "78 Waterfront View",
    "zip code": "V6B 1C5",
    "city": "Vancouver",
    "country": "Canada",
    "linkedin_url": "https://www.linkedin.com/in/sofiachen-ux",
    "twitter_url": "https://twitter.com/sofia_ux",
    "instagram_url": "https://www.instagram.com/sofiachen.art",
    "facebook_url": "https://www.facebook.com/sofia.chen.design",
    "about_me": "Sofia is a leading UX/UI Designer known for her human-centered approach to digital product development. Her portfolio showcases successful projects ranging from complex enterprise software to intuitive mobile applications, always prioritizing accessibility and clean aesthetics. She champions iterative design, utilizing rapid prototyping and extensive user testing to validate concepts. Sofia believes that good design is invisible and focuses on solving core user problems with elegance. She has spoken at several international design conferences about the future of interaction design in augmented reality. To keep her creative mind sharp, she practices Japanese calligraphy and ceramic pottery, finding that analog creative pursuits significantly inform her digital work and attention to detail.",
    "hobbies": [
      "Ceramics",
      "UX Research",
      "Calligraphy",
      "Cycling"
    ]
  },
  {
    "id": 3,
    "firstName": "Mateo",
    "lastName": "Ramirez",
    "avatar": "https://example.com/avatars/mateo.jpg",
    "age": 41,
    "email": "mateo.ramirez@energyco.net",
    "phone": "555-202-3003",
    "street": "22 Solar Heights",
    "zip code": "94107",
    "city": "San Francisco",
    "country": "USA",
    "linkedin_url": "https://www.linkedin.com/in/mateoramirez-renewables",
    "twitter_url": "https://twitter.com/mateo_energy",
    "instagram_url": "https://www.instagram.com/mateo.sustainability",
    "facebook_url": "https://www.facebook.com/mateo.ramirez.green",
    "about_me": "Mateo is an Environmental Policy Analyst with a deep commitment to sustainable energy transition. His work involves modeling the economic and environmental impacts of renewable energy infrastructure, providing crucial data for legislative proposals. He holds a Ph.D. in Resource Economics and has consulted for various governmental and non-profit organizations on climate mitigation strategies. He is passionate about translating complex scientific data into accessible policy recommendations that drive meaningful change at both local and international levels. Mateo is an avid birdwatcher and often incorporates field research into his travels, seeing the direct impact of policy on natural ecosystems. He firmly advocates for market-based solutions integrated with robust regulatory frameworks to achieve net-zero targets globally.",
    "hobbies": [
      "Environmental Policy",
      "Birdwatching",
      "Chess",
      "Gardening"
    ]
  },
  {
    "id": 4,
    "firstName": "Chloe",
    "lastName": "Dubois",
    "avatar": "https://example.com/avatars/chloe.jpg",
    "age": 25,
    "email": "chloe.dubois@fashionhouse.fr",
    "phone": "555-202-3004",
    "street": "15 Rue de Rivoli",
    "zip code": "75004",
    "city": "Paris",
    "country": "France",
    "linkedin_url": "https://www.linkedin.com/in/chloedubois-creative",
    "twitter_url": "https://twitter.com/chloe_stylist",
    "instagram_url": "https://www.instagram.com/chloe.fashion_edit",
    "facebook_url": "https://www.facebook.com/chloe.dubois.style",
    "about_me": "Chloe is a rising star in digital content creation, specializing in high-fashion and lifestyle marketing. Her role involves directing photoshoots, managing social media campaigns across multiple luxury brands, and analyzing engagement metrics to refine strategy. She has a keen eye for emerging trends and a proven ability to translate brand identity into compelling visual narratives that resonate with a global audience. Chloe's philosophy centers on ethical and sustainable fashion consumption, which she actively promotes through her platforms. She is fluent in three languages and frequently travels for international events. In her free time, she enjoys vintage clothes hunting and learning contemporary dance, which she finds inspires her sense of movement and composition in her professional photography work.",
    "hobbies": [
      "Fashion Photography",
      "Contemporary Dance",
      "Vintage Shopping",
      "Baking"
    ]
  },
  {
    "id": 5,
    "firstName": "Kenji",
    "lastName": "Tanaka",
    "avatar": "https://example.com/avatars/kenji.png",
    "age": 38,
    "email": "kenji.tanaka@quantum-mech.jp",
    "phone": "555-202-3005",
    "street": "3-2-1 Akihabara",
    "zip code": "101-0021",
    "city": "Tokyo",
    "country": "Japan",
    "linkedin_url": "https://www.linkedin.com/in/kenjitanaka-robotics",
    "twitter_url": "https://twitter.com/kenji_robo",
    "instagram_url": "https://www.instagram.com/kenji.sushi_maker",
    "facebook_url": "https://www.facebook.com/kenji.tanaka.engineer",
    "about_me": "Kenji is a highly respected Robotics Engineer focused on developing advanced manipulation and locomotion algorithms for industrial automation. He holds several patents related to precision movement systems and is actively involved in academic research collaborations aimed at creating smarter, more adaptable factory environments. His work demands meticulous attention to detail and a deep understanding of control theory and hardware integration. Kenji is committed to advancing the field of human-robot interaction, ensuring seamless collaboration between humans and machines. When not in the lab, he is a dedicated practitioner of Kendo, the Japanese martial art, which he credits for instilling discipline and strategic thinking crucial to his engineering challenges. He also enjoys traditional Japanese woodworking.",
    "hobbies": [
      "Robotics",
      "Kendo",
      "Woodworking",
      "Science Fiction"
    ]
  },
  {
    "id": 6,
    "firstName": "Priya",
    "lastName": "Sharma",
    "avatar": "https://example.com/avatars/priya.jpg",
    "age": 31,
    "email": "priya.sharma@health-sys.in",
    "phone": "555-202-3006",
    "street": "45 Lotus Lane",
    "zip code": "110001",
    "city": "New Delhi",
    "country": "India",
    "linkedin_url": "https://www.linkedin.com/in/priyasharma-publichealth",
    "twitter_url": "https://twitter.com/priya_health",
    "instagram_url": "https://www.instagram.com/priya.wellness",
    "facebook_url": "https://www.facebook.com/priya.sharma.phd",
    "about_me": "Priya is a Public Health Researcher focused on maternal and child health initiatives in underserved communities. Her research utilizes geospatial data and community-based participatory methods to identify barriers to healthcare access and develop targeted intervention programs. She is a powerful advocate for policy changes that promote equitable health outcomes globally. Her rigorous academic background in epidemiology is complemented by a hands-on approach to community engagement, believing that lasting solutions must be co-created with the people they serve. Priya finds peace and perspective through classical Indian dance and meditation, activities that help her manage the emotional demands of her critical work. She is currently preparing a submission to a major international health journal, detailing the success of her latest pilot program.",
    "hobbies": [
      "Public Health Advocacy",
      "Classical Dance",
      "Meditation",
      "Cooking"
    ]
  },
  {
    "id": 7,
    "firstName": "Diego",
    "lastName": "Mendoza",
    "avatar": "https://example.com/avatars/diego.png",
    "age": 48,
    "email": "diego.mendoza@ocean-law.cl",
    "phone": "555-202-3007",
    "street": "10 Coastline Boulevard",
    "zip code": "8320000",
    "city": "Santiago",
    "country": "Chile",
    "linkedin_url": "https://www.linkedin.com/in/diegomendoza-maritimelaw",
    "twitter_url": "https://twitter.com/diego_law",
    "instagram_url": "https://www.instagram.com/diego.sailing",
    "facebook_url": "https://www.facebook.com/diego.mendoza.attorney",
    "about_me": "Diego is a distinguished Maritime Law specialist with over two decades of experience handling complex international cases involving trade, environmental protection, and sovereignty disputes in oceanic territories. His expertise is crucial for multinational shipping companies and governmental bodies navigating the intricate legal framework of the sea. He has successfully argued cases before international tribunals and is a recognized scholar in the Law of the Sea. Diego believes that a sustainable future depends on clear, enforceable international legal standards. He is a passionate sailor and often spends weekends on the water, where he gains firsthand appreciation for the environments he strives to protect through his legal practice. He enjoys collecting antique maps and studying naval history.",
    "hobbies": [
      "Sailing",
      "Maritime Law",
      "Collecting Antique Maps",
      "Naval History"
    ]
  },
  {
    "id": 8,
    "firstName": "Lara",
    "lastName": "Kovač",
    "avatar": "https://example.com/avatars/lara.jpg",
    "age": 33,
    "email": "lara.kovac@fintech-zagreb.hr",
    "phone": "555-202-3008",
    "street": "5 Dalmatian Square",
    "zip code": "10000",
    "city": "Zagreb",
    "country": "Croatia",
    "linkedin_url": "https://www.linkedin.com/in/larakovac-finops",
    "twitter_url": "https://twitter.com/lara_finops",
    "instagram_url": "https://www.instagram.com/lara.travels",
    "facebook_url": "https://www.facebook.com/lara.kovac.finance",
    "about_me": "Lara is a FinOps Manager with a strong background in optimizing cloud spending and driving financial accountability across technology teams. Her role is centered on implementing governance, improving efficiency, and ensuring predictable financial outcomes in highly scaled environments. She is a certified public accountant with a specialization in technology budgeting and forecasting for SaaS companies. Lara is a pragmatic leader who values clear communication and cross-functional collaboration. She frequently presents internal workshops on financial literacy for engineers. To unwind, Lara is a dedicated amateur astronomer, often traveling to remote locations to photograph the night sky, a hobby that requires the same precision and long-term planning she applies to her professional life.",
    "hobbies": [
      "FinOps Optimization",
      "Amateur Astronomy",
      "Hiking",
      "Learning Croatian History"
    ]
  },
  {
    "id": 9,
    "firstName": "Marcus",
    "lastName": "Jones",
    "avatar": "https://example.com/avatars/marcus.png",
    "age": 27,
    "email": "marcus.jones@game-studio.us",
    "phone": "555-202-3009",
    "street": "17 Pixel Alley",
    "zip code": "98101",
    "city": "Seattle",
    "country": "USA",
    "linkedin_url": "https://www.linkedin.com/in/marcusjones-gamedev",
    "twitter_url": "https://twitter.com/marcus_gamedev",
    "instagram_url": "https://www.instagram.com/marcus.dungeons",
    "facebook_url": "https://www.facebook.com/marcus.jones.games",
    "about_me": "Marcus is a talented Video Game Writer and Narrative Designer working on a critically acclaimed indie RPG title. He is responsible for crafting deep lore, developing engaging character backstories, and ensuring dialogue consistency across hundreds of hours of gameplay. His passion lies in creating immersive worlds that allow players to explore complex themes and moral choices. He holds a degree in Creative Writing and has a keen understanding of interactive storytelling principles. Marcus is also the Dungeon Master for a highly active weekly D&D group, a hobby that directly enhances his professional skills in improvisation and collaborative narrative construction. He believes that video games are the premier storytelling medium of the 21st century and constantly pushes the boundaries of player agency within narrative frameworks.",
    "hobbies": [
      "D&D (Dungeon Master)",
      "Interactive Storytelling",
      "Acoustic Guitar",
      "Competitive Gaming"
    ]
  },
  {
    "id": 10,
    "firstName": "Fatima",
    "lastName": "Ali",
    "avatar": "https://example.com/avatars/fatima.jpg",
    "age": 30,
    "email": "fatima.ali@space-aero.ae",
    "phone": "555-202-3010",
    "street": "9 Launch Pad Road",
    "zip code": "100001",
    "city": "Dubai",
    "country": "UAE",
    "linkedin_url": "https://www.linkedin.com/in/fatimaali-aerospace",
    "twitter_url": "https://twitter.com/fatima_space",
    "instagram_url": "https://www.instagram.com/fatima.stars",
    "facebook_url": "https://www.facebook.com/fatima.ali.engineer",
    "about_me": "Fatima is an Aerospace Systems Engineer focused on trajectory optimization for inter-planetary missions. She works on complex orbital mechanics calculations and ensures the safety and efficiency of propulsion systems for uncrewed exploration vehicles. Holding a Master's degree in Aeronautical Engineering, she is a strong advocate for increasing representation of women in STEM fields across the Middle East. Her work is highly collaborative, often involving coordination with international space agencies. She views every launch as a testament to global teamwork and scientific possibility. In her personal life, Fatima is an avid scuba diver, exploring the mysteries of the deep ocean, which provides a serene contrast to the high-stakes precision required in her aerospace career. She also enjoys digital painting, often rendering celestial bodies.",
    "hobbies": [
      "Scuba Diving",
      "Orbital Mechanics",
      "Digital Painting",
      "Mentoring STEM Students"
    ]
  },
  {
    "id": 11,
    "firstName": "Robert",
    "lastName": "Smith",
    "avatar": "https://example.com/avatars/robert11.jpg",
    "age": 55,
    "email": "robert.smith11@template.com",
    "phone": "555-202-3011",
    "street": "11 Placeholder Lane",
    "zip code": "P011Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/robertsmith11",
    "twitter_url": "https://twitter.com/robert_11",
    "instagram_url": "https://www.instagram.com/robert11",
    "facebook_url": "https://www.facebook.com/robert.smith11",
    "about_me": "This is a structured placeholder 'about me' section for Robert Smith. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Robert is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby A",
      "Placeholder Hobby B"
    ]
  },
  {
    "id": 12,
    "firstName": "Jennifer",
    "lastName": "Davis",
    "avatar": "https://example.com/avatars/jennifer12.jpg",
    "age": 29,
    "email": "jennifer.davis12@template.com",
    "phone": "555-202-3012",
    "street": "12 Placeholder Lane",
    "zip code": "P012Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/jenniferdavis12",
    "twitter_url": "https://twitter.com/jennifer_12",
    "instagram_url": "https://www.instagram.com/jennifer12",
    "facebook_url": "https://www.facebook.com/jennifer.davis12",
    "about_me": "This is a structured placeholder 'about me' section for Jennifer Davis. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Jennifer is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby C",
      "Placeholder Hobby D"
    ]
  },
  {
    "id": 13,
    "firstName": "Michael",
    "lastName": "Wilson",
    "avatar": "https://example.com/avatars/michael13.jpg",
    "age": 44,
    "email": "michael.wilson13@template.com",
    "phone": "555-202-3013",
    "street": "13 Placeholder Lane",
    "zip code": "P013Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/michaelwilson13",
    "twitter_url": "https://twitter.com/michael_13",
    "instagram_url": "https://www.instagram.com/michael13",
    "facebook_url": "https://www.facebook.com/michael.wilson13",
    "about_me": "This is a structured placeholder 'about me' section for Michael Wilson. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Michael is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby E",
      "Placeholder Hobby F"
    ]
  },
  {
    "id": 14,
    "firstName": "Sarah",
    "lastName": "Moore",
    "avatar": "https://example.com/avatars/sarah14.jpg",
    "age": 36,
    "email": "sarah.moore14@template.com",
    "phone": "555-202-3014",
    "street": "14 Placeholder Lane",
    "zip code": "P014Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/sarahmoore14",
    "twitter_url": "https://twitter.com/sarah_14",
    "instagram_url": "https://www.instagram.com/sarah14",
    "facebook_url": "https://www.facebook.com/sarah.moore14",
    "about_me": "This is a structured placeholder 'about me' section for Sarah Moore. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Sarah is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby G",
      "Placeholder Hobby H"
    ]
  },
  {
    "id": 15,
    "firstName": "David",
    "lastName": "Taylor",
    "avatar": "https://example.com/avatars/david15.jpg",
    "age": 50,
    "email": "david.taylor15@template.com",
    "phone": "555-202-3015",
    "street": "15 Placeholder Lane",
    "zip code": "P015Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/davidtaylor15",
    "twitter_url": "https://twitter.com/david_15",
    "instagram_url": "https://www.instagram.com/david15",
    "facebook_url": "https://www.facebook.com/david.taylor15",
    "about_me": "This is a structured placeholder 'about me' section for David Taylor. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. David is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby I",
      "Placeholder Hobby J"
    ]
  },
  {
    "id": 16,
    "firstName": "Laura",
    "lastName": "Anderson",
    "avatar": "https://example.com/avatars/laura16.jpg",
    "age": 24,
    "email": "laura.anderson16@template.com",
    "phone": "555-202-3016",
    "street": "16 Placeholder Lane",
    "zip code": "P016Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/lauraanderson16",
    "twitter_url": "https://twitter.com/laura_16",
    "instagram_url": "https://www.instagram.com/laura16",
    "facebook_url": "https://www.facebook.com/laura.anderson16",
    "about_me": "This is a structured placeholder 'about me' section for Laura Anderson. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Laura is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby K",
      "Placeholder Hobby L"
    ]
  },
  {
    "id": 17,
    "firstName": "James",
    "lastName": "Thomas",
    "avatar": "https://example.com/avatars/james17.jpg",
    "age": 39,
    "email": "james.thomas17@template.com",
    "phone": "555-202-3017",
    "street": "17 Placeholder Lane",
    "zip code": "P017Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/jamesthomas17",
    "twitter_url": "https://twitter.com/james_17",
    "instagram_url": "https://www.instagram.com/james17",
    "facebook_url": "https://www.facebook.com/james.thomas17",
    "about_me": "This is a structured placeholder 'about me' section for James Thomas. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. James is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby M",
      "Placeholder Hobby N"
    ]
  },
  {
    "id": 18,
    "firstName": "Linda",
    "lastName": "Jackson",
    "avatar": "https://example.com/avatars/linda18.jpg",
    "age": 47,
    "email": "linda.jackson18@template.com",
    "phone": "555-202-3018",
    "street": "18 Placeholder Lane",
    "zip code": "P018Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/lindajackson18",
    "twitter_url": "https://twitter.com/linda_18",
    "instagram_url": "https://www.instagram.com/linda18",
    "facebook_url": "https://www.facebook.com/linda.jackson18",
    "about_me": "This is a structured placeholder 'about me' section for Linda Jackson. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Linda is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby O",
      "Placeholder Hobby P"
    ]
  },
  {
    "id": 19,
    "firstName": "William",
    "lastName": "White",
    "avatar": "https://example.com/avatars/william19.jpg",
    "age": 31,
    "email": "william.white19@template.com",
    "phone": "555-202-3019",
    "street": "19 Placeholder Lane",
    "zip code": "P019Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/williamwhite19",
    "twitter_url": "https://twitter.com/william_19",
    "instagram_url": "https://www.instagram.com/william19",
    "facebook_url": "https://www.facebook.com/william.white19",
    "about_me": "This is a structured placeholder 'about me' section for William White. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. William is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby Q",
      "Placeholder Hobby R"
    ]
  },
  {
    "id": 20,
    "firstName": "Karen",
    "lastName": "Harris",
    "avatar": "https://example.com/avatars/karen20.jpg",
    "age": 40,
    "email": "karen.harris20@template.com",
    "phone": "555-202-3020",
    "street": "20 Placeholder Lane",
    "zip code": "P020Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/karenharris20",
    "twitter_url": "https://twitter.com/karen_20",
    "instagram_url": "https://www.instagram.com/karen20",
    "facebook_url": "https://www.facebook.com/karen.harris20",
    "about_me": "This is a structured placeholder 'about me' section for Karen Harris. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Karen is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby S",
      "Placeholder Hobby T"
    ]
  },
  {
    "id": 21,
    "firstName": "Joseph",
    "lastName": "Martin",
    "avatar": "https://example.com/avatars/joseph21.jpg",
    "age": 33,
    "email": "joseph.martin21@template.com",
    "phone": "555-202-3021",
    "street": "21 Placeholder Lane",
    "zip code": "P021Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/josephmartin21",
    "twitter_url": "https://twitter.com/joseph_21",
    "instagram_url": "https://www.instagram.com/joseph21",
    "facebook_url": "https://www.facebook.com/joseph.martin21",
    "about_me": "This is a structured placeholder 'about me' section for Joseph Martin. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Joseph is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby U",
      "Placeholder Hobby V"
    ]
  },
  {
    "id": 22,
    "firstName": "Nancy",
    "lastName": "Garcia",
    "avatar": "https://example.com/avatars/nancy22.jpg",
    "age": 28,
    "email": "nancy.garcia22@template.com",
    "phone": "555-202-3022",
    "street": "22 Placeholder Lane",
    "zip code": "P022Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/nancygarcia22",
    "twitter_url": "https://twitter.com/nancy_22",
    "instagram_url": "https://www.instagram.com/nancy22",
    "facebook_url": "https://www.facebook.com/nancy.garcia22",
    "about_me": "This is a structured placeholder 'about me' section for Nancy Garcia. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Nancy is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby W",
      "Placeholder Hobby X"
    ]
  },
  {
    "id": 23,
    "firstName": "Charles",
    "lastName": "Rodriguez",
    "avatar": "https://example.com/avatars/charles23.jpg",
    "age": 41,
    "email": "charles.rodriguez23@template.com",
    "phone": "555-202-3023",
    "street": "23 Placeholder Lane",
    "zip code": "P023Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/charlesrodriguez23",
    "twitter_url": "https://twitter.com/charles_23",
    "instagram_url": "https://www.instagram.com/charles23",
    "facebook_url": "https://www.facebook.com/charles.rodriguez23",
    "about_me": "This is a structured placeholder 'about me' section for Charles Rodriguez. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Charles is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby Y",
      "Placeholder Hobby Z"
    ]
  },
  {
    "id": 24,
    "firstName": "Donna",
    "lastName": "Lewis",
    "avatar": "https://example.com/avatars/donna24.jpg",
    "age": 32,
    "email": "donna.lewis24@template.com",
    "phone": "555-202-3024",
    "street": "24 Placeholder Lane",
    "zip code": "P024Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/donnalewis24",
    "twitter_url": "https://twitter.com/donna_24",
    "instagram_url": "https://www.instagram.com/donna24",
    "facebook_url": "https://www.facebook.com/donna.lewis24",
    "about_me": "This is a structured placeholder 'about me' section for Donna Lewis. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Donna is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby AA",
      "Placeholder Hobby BB"
    ]
  },
  {
    "id": 25,
    "firstName": "Richard",
    "lastName": "Lee",
    "avatar": "https://example.com/avatars/richard25.jpg",
    "age": 58,
    "email": "richard.lee25@template.com",
    "phone": "555-202-3025",
    "street": "25 Placeholder Lane",
    "zip code": "P025Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/richardlee25",
    "twitter_url": "https://twitter.com/richard_25",
    "instagram_url": "https://www.instagram.com/richard25",
    "facebook_url": "https://www.facebook.com/richard.lee25",
    "about_me": "This is a structured placeholder 'about me' section for Richard Lee. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Richard is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby CC",
      "Placeholder Hobby DD"
    ]
  },
  {
    "id": 26,
    "firstName": "Maria",
    "lastName": "Walker",
    "avatar": "https://example.com/avatars/maria26.jpg",
    "age": 26,
    "email": "maria.walker26@template.com",
    "phone": "555-202-3026",
    "street": "26 Placeholder Lane",
    "zip code": "P026Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/mariawalker26",
    "twitter_url": "https://twitter.com/maria_26",
    "instagram_url": "https://www.instagram.com/maria26",
    "facebook_url": "https://www.facebook.com/maria.walker26",
    "about_me": "This is a structured placeholder 'about me' section for Maria Walker. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Maria is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby EE",
      "Placeholder Hobby FF"
    ]
  },
  {
    "id": 27,
    "firstName": "Christopher",
    "lastName": "Hall",
    "avatar": "https://example.com/avatars/christopher27.jpg",
    "age": 49,
    "email": "christopher.hall27@template.com",
    "phone": "555-202-3027",
    "street": "27 Placeholder Lane",
    "zip code": "P027Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/christopherhall27",
    "twitter_url": "https://twitter.com/christopher_27",
    "instagram_url": "https://www.instagram.com/christopher27",
    "facebook_url": "https://www.facebook.com/christopher.hall27",
    "about_me": "This is a structured placeholder 'about me' section for Christopher Hall. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Christopher is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby GG",
      "Placeholder Hobby HH"
    ]
  },
  {
    "id": 28,
    "firstName": "Betty",
    "lastName": "Allen",
    "avatar": "https://example.com/avatars/betty28.jpg",
    "age": 34,
    "email": "betty.allen28@template.com",
    "phone": "555-202-3028",
    "street": "28 Placeholder Lane",
    "zip code": "P028Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/bettyallen28",
    "twitter_url": "https://twitter.com/betty_28",
    "instagram_url": "https://www.instagram.com/betty28",
    "facebook_url": "https://www.facebook.com/betty.allen28",
    "about_me": "This is a structured placeholder 'about me' section for Betty Allen. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Betty is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby II",
      "Placeholder Hobby JJ"
    ]
  },
  {
    "id": 29,
    "firstName": "Matthew",
    "lastName": "Young",
    "avatar": "https://example.com/avatars/matthew29.jpg",
    "age": 46,
    "email": "matthew.young29@template.com",
    "phone": "555-202-3029",
    "street": "29 Placeholder Lane",
    "zip code": "P029Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/matthewyoung29",
    "twitter_url": "https://twitter.com/matthew_29",
    "instagram_url": "https://www.instagram.com/matthew29",
    "facebook_url": "https://www.facebook.com/matthew.young29",
    "about_me": "This is a structured placeholder 'about me' section for Matthew Young. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Matthew is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby KK",
      "Placeholder Hobby LL"
    ]
  },
  {
    "id": 30,
    "firstName": "Helen",
    "lastName": "King",
    "avatar": "https://example.com/avatars/helen30.jpg",
    "age": 37,
    "email": "helen.king30@template.com",
    "phone": "555-202-3030",
    "street": "30 Placeholder Lane",
    "zip code": "P030Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/helenking30",
    "twitter_url": "https://twitter.com/helen_30",
    "instagram_url": "https://www.instagram.com/helen30",
    "facebook_url": "https://www.facebook.com/helen.king30",
    "about_me": "This is a structured placeholder 'about me' section for Helen King. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Helen is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby MM",
      "Placeholder Hobby NN"
    ]
  },
  {
    "id": 31,
    "firstName": "Daniel",
    "lastName": "Wright",
    "avatar": "https://example.com/avatars/daniel31.jpg",
    "age": 53,
    "email": "daniel.wright31@template.com",
    "phone": "555-202-3031",
    "street": "31 Placeholder Lane",
    "zip code": "P031Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/danielwright31",
    "twitter_url": "https://twitter.com/daniel_31",
    "instagram_url": "https://www.instagram.com/daniel31",
    "facebook_url": "https://www.facebook.com/daniel.wright31",
    "about_me": "This is a structured placeholder 'about me' section for Daniel Wright. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Daniel is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby OO",
      "Placeholder Hobby PP"
    ]
  },
  {
    "id": 32,
    "firstName": "Chloe",
    "lastName": "Scott",
    "avatar": "https://example.com/avatars/chloe32.jpg",
    "age": 22,
    "email": "chloe.scott32@template.com",
    "phone": "555-202-3032",
    "street": "32 Placeholder Lane",
    "zip code": "P032Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/chloescott32",
    "twitter_url": "https://twitter.com/chloe_32",
    "instagram_url": "https://www.instagram.com/chloe32",
    "facebook_url": "https://www.facebook.com/chloe.scott32",
    "about_me": "This is a structured placeholder 'about me' section for Chloe Scott. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Chloe is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby QQ",
      "Placeholder Hobby RR"
    ]
  },
  {
    "id": 33,
    "firstName": "Edward",
    "lastName": "Baker",
    "avatar": "https://example.com/avatars/edward33.jpg",
    "age": 60,
    "email": "edward.baker33@template.com",
    "phone": "555-202-3033",
    "street": "33 Placeholder Lane",
    "zip code": "P033Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/edwardbaker33",
    "twitter_url": "https://twitter.com/edward_33",
    "instagram_url": "https://www.instagram.com/edward33",
    "facebook_url": "https://www.facebook.com/edward.baker33",
    "about_me": "This is a structured placeholder 'about me' section for Edward Baker. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Edward is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby SS",
      "Placeholder Hobby TT"
    ]
  },
  {
    "id": 34,
    "firstName": "Amanda",
    "lastName": "Adams",
    "avatar": "https://example.com/avatars/amanda34.jpg",
    "age": 30,
    "email": "amanda.adams34@template.com",
    "phone": "555-202-3034",
    "street": "34 Placeholder Lane",
    "zip code": "P034Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/amandaadams34",
    "twitter_url": "https://twitter.com/amanda_34",
    "instagram_url": "https://www.instagram.com/amanda34",
    "facebook_url": "https://www.facebook.com/amanda.adams34",
    "about_me": "This is a structured placeholder 'about me' section for Amanda Adams. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Amanda is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby UU",
      "Placeholder Hobby VV"
    ]
  },
  {
    "id": 35,
    "firstName": "Kevin",
    "lastName": "Carter",
    "avatar": "https://example.com/avatars/kevin35.jpg",
    "age": 45,
    "email": "kevin.carter35@template.com",
    "phone": "555-202-3035",
    "street": "35 Placeholder Lane",
    "zip code": "P035Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/kevincarter35",
    "twitter_url": "https://twitter.com/kevin_35",
    "instagram_url": "https://www.instagram.com/kevin35",
    "facebook_url": "https://www.facebook.com/kevin.carter35",
    "about_me": "This is a structured placeholder 'about me' section for Kevin Carter. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Kevin is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby WW",
      "Placeholder Hobby XX"
    ]
  },
  {
    "id": 36,
    "firstName": "Sharon",
    "lastName": "Mitchell",
    "avatar": "https://example.com/avatars/sharon36.jpg",
    "age": 38,
    "email": "sharon.mitchell36@template.com",
    "phone": "555-202-3036",
    "street": "36 Placeholder Lane",
    "zip code": "P036Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/sharonmitchell36",
    "twitter_url": "https://twitter.com/sharon_36",
    "instagram_url": "https://www.instagram.com/sharon36",
    "facebook_url": "https://www.facebook.com/sharon.mitchell36",
    "about_me": "This is a structured placeholder 'about me' section for Sharon Mitchell. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Sharon is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby YY",
      "Placeholder Hobby ZZ"
    ]
  },
  {
    "id": 37,
    "firstName": "George",
    "lastName": "Perez",
    "avatar": "https://example.com/avatars/george37.jpg",
    "age": 51,
    "email": "george.perez37@template.com",
    "phone": "555-202-3037",
    "street": "37 Placeholder Lane",
    "zip code": "P037Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/georgeperez37",
    "twitter_url": "https://twitter.com/george_37",
    "instagram_url": "https://www.instagram.com/george37",
    "facebook_url": "https://www.facebook.com/george.perez37",
    "about_me": "This is a structured placeholder 'about me' section for George Perez. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. George is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1A",
      "Placeholder Hobby 1B"
    ]
  },
  {
    "id": 38,
    "firstName": "Jessica",
    "lastName": "Roberts",
    "avatar": "https://example.com/avatars/jessica38.jpg",
    "age": 29,
    "email": "jessica.roberts38@template.com",
    "phone": "555-202-3038",
    "street": "38 Placeholder Lane",
    "zip code": "P038Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/jessicaroberts38",
    "twitter_url": "https://twitter.com/jessica_38",
    "instagram_url": "https://www.instagram.com/jessica38",
    "facebook_url": "https://www.facebook.com/jessica.roberts38",
    "about_me": "This is a structured placeholder 'about me' section for Jessica Roberts. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Jessica is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1C",
      "Placeholder Hobby 1D"
    ]
  },
  {
    "id": 39,
    "firstName": "Steven",
    "lastName": "Turner",
    "avatar": "https://example.com/avatars/steven39.jpg",
    "age": 43,
    "email": "steven.turner39@template.com",
    "phone": "555-202-3039",
    "street": "39 Placeholder Lane",
    "zip code": "P039Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/steventurner39",
    "twitter_url": "https://twitter.com/steven_39",
    "instagram_url": "https://www.instagram.com/steven39",
    "facebook_url": "https://www.facebook.com/steven.turner39",
    "about_me": "This is a structured placeholder 'about me' section for Steven Turner. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Steven is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1E",
      "Placeholder Hobby 1F"
    ]
  },
  {
    "id": 40,
    "firstName": "Emily",
    "lastName": "Phillips",
    "avatar": "https://example.com/avatars/emily40.jpg",
    "age": 35,
    "email": "emily.phillips40@template.com",
    "phone": "555-202-3040",
    "street": "40 Placeholder Lane",
    "zip code": "P040Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/emilyphillips40",
    "twitter_url": "https://twitter.com/emily_40",
    "instagram_url": "https://www.instagram.com/emily40",
    "facebook_url": "https://www.facebook.com/emily.phillips40",
    "about_me": "This is a structured placeholder 'about me' section for Emily Phillips. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Emily is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1G",
      "Placeholder Hobby 1H"
    ]
  },
  {
    "id": 41,
    "firstName": "Mark",
    "lastName": "Campbell",
    "avatar": "https://example.com/avatars/mark41.jpg",
    "age": 52,
    "email": "mark.campbell41@template.com",
    "phone": "555-202-3041",
    "street": "41 Placeholder Lane",
    "zip code": "P041Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/markcampbell41",
    "twitter_url": "https://twitter.com/mark_41",
    "instagram_url": "https://www.instagram.com/mark41",
    "facebook_url": "https://www.facebook.com/mark.campbell41",
    "about_me": "This is a structured placeholder 'about me' section for Mark Campbell. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Mark is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1I",
      "Placeholder Hobby 1J"
    ]
  },
  {
    "id": 42,
    "firstName": "Susan",
    "lastName": "Parker",
    "avatar": "https://example.com/avatars/susan42.jpg",
    "age": 30,
    "email": "susan.parker42@template.com",
    "phone": "555-202-3042",
    "street": "42 Placeholder Lane",
    "zip code": "P042Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/susanparker42",
    "twitter_url": "https://twitter.com/susan_42",
    "instagram_url": "https://www.instagram.com/susan42",
    "facebook_url": "https://www.facebook.com/susan.parker42",
    "about_me": "This is a structured placeholder 'about me' section for Susan Parker. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Susan is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1K",
      "Placeholder Hobby 1L"
    ]
  },
  {
    "id": 43,
    "firstName": "Paul",
    "lastName": "Evans",
    "avatar": "https://example.com/avatars/paul43.jpg",
    "age": 47,
    "email": "paul.evans43@template.com",
    "phone": "555-202-3043",
    "street": "43 Placeholder Lane",
    "zip code": "P043Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/paulevans43",
    "twitter_url": "https://twitter.com/paul_43",
    "instagram_url": "https://www.instagram.com/paul43",
    "facebook_url": "https://www.facebook.com/paul.evans43",
    "about_me": "This is a structured placeholder 'about me' section for Paul Evans. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Paul is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1M",
      "Placeholder Hobby 1N"
    ]
  },
  {
    "id": 44,
    "firstName": "Taylor",
    "lastName": "Morris",
    "avatar": "https://example.com/avatars/taylor44.jpg",
    "age": 33,
    "email": "taylor.morris44@template.com",
    "phone": "555-202-3044",
    "street": "44 Placeholder Lane",
    "zip code": "P044Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/taylormorris44",
    "twitter_url": "https://twitter.com/taylor_44",
    "instagram_url": "https://www.instagram.com/taylor44",
    "facebook_url": "https://www.facebook.com/taylor.morris44",
    "about_me": "This is a structured placeholder 'about me' section for Taylor Morris. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Taylor is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1O",
      "Placeholder Hobby 1P"
    ]
  },
  {
    "id": 45,
    "firstName": "Gary",
    "lastName": "Peterson",
    "avatar": "https://example.com/avatars/gary45.jpg",
    "age": 56,
    "email": "gary.peterson45@template.com",
    "phone": "555-202-3045",
    "street": "45 Placeholder Lane",
    "zip code": "P045Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/garypeterson45",
    "twitter_url": "https://twitter.com/gary_45",
    "instagram_url": "https://www.instagram.com/gary45",
    "facebook_url": "https://www.facebook.com/gary.peterson45",
    "about_me": "This is a structured placeholder 'about me' section for Gary Peterson. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Gary is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1Q",
      "Placeholder Hobby 1R"
    ]
  },
  {
    "id": 46,
    "firstName": "Denise",
    "lastName": "Cooper",
    "avatar": "https://example.com/avatars/denise46.jpg",
    "age": 25,
    "email": "denise.cooper46@template.com",
    "phone": "555-202-3046",
    "street": "46 Placeholder Lane",
    "zip code": "P046Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/denisecooper46",
    "twitter_url": "https://twitter.com/denise_46",
    "instagram_url": "https://www.instagram.com/denise46",
    "facebook_url": "https://www.facebook.com/denise.cooper46",
    "about_me": "This is a structured placeholder 'about me' section for Denise Cooper. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Denise is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1S",
      "Placeholder Hobby 1T"
    ]
  },
  {
    "id": 47,
    "firstName": "Bruce",
    "lastName": "Bailey",
    "avatar": "https://example.com/avatars/bruce47.jpg",
    "age": 49,
    "email": "bruce.bailey47@template.com",
    "phone": "555-202-3047",
    "street": "47 Placeholder Lane",
    "zip code": "P047Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/brucebailey47",
    "twitter_url": "https://twitter.com/bruce_47",
    "instagram_url": "https://www.instagram.com/bruce47",
    "facebook_url": "https://www.facebook.com/bruce.bailey47",
    "about_me": "This is a structured placeholder 'about me' section for Bruce Bailey. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Bruce is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1U",
      "Placeholder Hobby 1V"
    ]
  },
  {
    "id": 48,
    "firstName": "Diana",
    "lastName": "Kelly",
    "avatar": "https://example.com/avatars/diana48.jpg",
    "age": 31,
    "email": "diana.kelly48@template.com",
    "phone": "555-202-3048",
    "street": "48 Placeholder Lane",
    "zip code": "P048Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/dianakelly48",
    "twitter_url": "https://twitter.com/diana_48",
    "instagram_url": "https://www.instagram.com/diana48",
    "facebook_url": "https://www.facebook.com/diana.kelly48",
    "about_me": "This is a structured placeholder 'about me' section for Diana Kelly. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Diana is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1W",
      "Placeholder Hobby 1X"
    ]
  },
  {
    "id": 49,
    "firstName": "Roger",
    "lastName": "Howard",
    "avatar": "https://example.com/avatars/roger49.jpg",
    "age": 54,
    "email": "roger.howard49@template.com",
    "phone": "555-202-3049",
    "street": "49 Placeholder Lane",
    "zip code": "P049Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/rogerhoward49",
    "twitter_url": "https://twitter.com/roger_49",
    "instagram_url": "https://www.instagram.com/roger49",
    "facebook_url": "https://www.facebook.com/roger.howard49",
    "about_me": "This is a structured placeholder 'about me' section for Roger Howard. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Roger is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. He works in Generic Solutions and enjoys the Placeholder Arts. His goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 1Y",
      "Placeholder Hobby 1Z"
    ]
  },
  {
    "id": 50,
    "firstName": "Evelyn",
    "lastName": "Flores",
    "avatar": "https://example.com/avatars/evelyn50.jpg",
    "age": 27,
    "email": "evelyn.flores50@template.com",
    "phone": "555-202-3050",
    "street": "50 Placeholder Lane",
    "zip code": "P050Z",
    "city": "Templateville",
    "country": "ZZZ",
    "linkedin_url": "https://www.linkedin.com/in/evelynflores50",
    "twitter_url": "https://twitter.com/evelyn_50",
    "instagram_url": "https://www.instagram.com/evelyn50",
    "facebook_url": "https://www.facebook.com/evelyn.flores50",
    "about_me": "This is a structured placeholder 'about me' section for Evelyn Flores. This string of text must not be less than 250 characters to fulfill the strict requirement of the data model. Evelyn is a placeholder data entry designed to complete the required count of 50 objects in the JSON array. All details are fictional and designed to be expanded upon by the user. She works in Generic Solutions and enjoys the Placeholder Arts. Her goal is to demonstrate the JSON structure accurately and efficiently, ensuring validation against all specified constraints, including the length of this biographical text. Please replace this generic content with unique and meaningful biographical data for your final production use case. This section is just a template filler to meet the required length for the data object. Always customize the data.",
    "hobbies": [
      "Placeholder Hobby 2A",
      "Placeholder Hobby 2B"
    ]
  }
]

updated_list=[{**user,'password':'123456','avatar':f'https://avatar.iran.liara.run/username?username={user["firstName"]}+{user["lastName"]}'} for user in users]
current_user=updated_list[30]

logged_user_blogs=[blog for blog in blogs if blog['owner_id']==current_user['id']]

@app.context_processor
def inject_global_vars():

    if len(current_user['about_me']) > 200:
        truncated_text = current_user['about_me'][:200 - 3] + "..."  # -3 for the ellipsis
    else:
        truncated_text = current_user['about_me']
    return dict(site_name="Ekogab Blogs", about_me=truncated_text,logged_user=current_user)



@app.route('/')
@app.route('/home')
def home_page():


    return render_template('home.html',logged_user=current_user, blog_posts=blogs,blogs=logged_user_blogs)


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
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')