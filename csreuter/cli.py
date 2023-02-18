import random
import webbrowser

import typer

app = typer.Typer()

FACTS = [
    # https://www.maine.gov/portal/about_me/facts.html
    "The population in 2010 was 1,328,361",
    "It has 16 counties",
    "Its land area is 30,843 square miles",
    "The length of its coastline is 3,500 miles",
    "It has 6,000 lakes and ponds",
    "It has 17 million acres of forest",
    "It has 43.1 persons per square mile",
    "Its largest city is Portland",
    "Its state capital is Augusta",
    "It became the 23rd State on March 15, 1820",
    "Chris Reuter is from Maine (did you know that?)",
]


@app.command()
def maine():
    """Random facts about Maine"""
    fact = random.choice(FACTS)
    print(f"Here's a random fact about Maine: {fact}")


@app.command()
def musings():
    """Quick access to words from a Mainer"""
    print("Let's get you some musings!")
    webbrowser.open_new_tab("https://chrisreuter.me/")


if __name__ == "__main__":
    app()
