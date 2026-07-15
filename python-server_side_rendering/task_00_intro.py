"""Module for intro to Server-Side Rendering"""

import os


def generate_invitations(template, attendees):
    """Function to generate invitations"""
    if type(template) is not str:
        print("Template is not a string, no output files generated.")
        return
    if (not isinstance(attendees, list)
            or not all(isinstance(x, dict) for x in attendees)):
        print("Data provided is not a dict, no output files generated.")
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i in range(len(attendees)):
        filename = "output_X.txt"
        filename = filename.replace("X", str(i))

        text = template
        for (key, value) in attendees[i].items():
            if value is None:
                value = "N/A"
            key = "{" + key + "}"
            text = text.replace(key, value)

        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as file:
                file.write(text)
