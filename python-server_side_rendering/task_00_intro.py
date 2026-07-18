"""Module for intro to Server-Side Rendering"""

import os


def generate_invitations(template, attendees):
    """Function to generate invitations"""
    if type(template) is not str:
        print("Template is not a string, no output files generated.")
        return
    if (not isinstance(attendees, list)
            or not all(isinstance(x, dict) for x in attendees)):
        print("Data provided is not a list of dicts, no output files generated.")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    keys = [
        "name",
        "event_title",
        "event_date",
        "event_location"
    ]

    i = 0
    for person in attendees:
        i += 1
        filename = f"output_{i}.txt"
        text = template
        for key in keys:
            value = person.get(key)
            if value is None:
                value = "N/A"
            text = text.replace(
                "{" + key + "}",
                str(value)
            )

        try:
            if os.path.exists(filename):
                print(f"{filename} already exists.")
                continue
            with open(filename, "w", encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
