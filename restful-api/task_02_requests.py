#!/usr/bin/python3
"""Module for simple requests library"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch from JSONPlaceholder and print titles"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    """Fetch from JSONPlaceholder and save to a list of dictionaries"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        posts = r.json()
        data = []
        for post in posts:
            data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="") as file:
            fn = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames = fn)
            writer.writeheader()
            writer.writerows(data)

