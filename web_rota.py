from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    workers = ['Pat', 'Dan', 'Yulian', 'Kyle']
    now = datetime.datetime.now()
    week_number = (now.date() - datetime.date(now.year, 1, 1)).days // 7
    worker_index = week_number % len(workers)
    current_worker = workers[worker_index]
    start_date = now.date() + datetime.timedelta(days=(4 - now.weekday()))
    end_date = start_date + datetime.timedelta(days=6)
    prev_worker_index = (worker_index - 1) % len(workers)
    prev_worker = workers[prev_worker_index]
    next_worker_index = (worker_index + 1) % len(workers)
    next_worker = workers[next_worker_index]
    return render_template("index.html", current_worker=current_worker, start_date=start_date, end_date=end_date, prev_worker=prev_worker, next_worker=next_worker)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
