from flask import Flask

import Utils
import os

app = Flask(__name__)


def get_score():
    try:
        if os.path.exists(Utils.SCORES_FILE_NAME):
            file = open(Utils.SCORES_FILE_NAME, "r")
            score = file.readline()
            file.close()
            return score
        else:
            return -2
    except BaseException as e:
        return Utils.BAD_RETURN_CODE


@app.route("/")
def score_server():
    score = get_score()
    html_content = ""
    if (int(score) > -1):

        html_content = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    else:
        if (score == -2):
            score = "File not Found"
        html_content = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                
                <h1><div  style="color:red">error: </div></h1>
                <h2><div id="score" style="color:red">{score}</div></h2>
            </body>
        </html>
        """
    return html_content


app.run()
