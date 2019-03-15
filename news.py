from flask import render_template, Flask
import json

app = Flask(__name__)

@app.route('/')
@app.route('/news')
def news():
    with open("E:\Projects\web_project\WorkItemByWeek.json", "rt", encoding="utf8") as f:
        workitem_list = json.loads(f.read())
    return render_template('news.html', news=workitem_list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')