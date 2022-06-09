from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story,excited_story,storySelection

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/home")
def get_prompts():
    """gets promts from user"""
    prompts = silly_story.prompts

    return render_template("questions.html", prompts=prompts)

@app.get("/story")
def make_story():
    """unpacks prompts and prompt values and creates answers, then passes in
    answers to Story.generate"""

    story = silly_story.generate(request.args)

    return render_template("story.html",story=story)

@app.get("/choice")
def choose_story():
    """allow user to pick madlib story"""
    stories = storySelection
    return render_template("storyChoice.html", stories=stories)