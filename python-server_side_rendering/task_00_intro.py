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

    i = 0
    for person in attendees:
        i += 1
        filename = f"output_{i}.txt"
        text = template
        for key, value in person.items():
            try:
                if value is None:
                    raise ValueError
            except ValueError:
                value = "N/A"
            key = f"{{{key}}}"
            text = text.replace(key, value)

        try:
            if os.path.exists(filename):
                print(f"{filename} already exists.")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            raise Exception(e)
