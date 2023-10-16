from flask import Flask, render_template
from flask.json import jsonify

JOBS = [
    {
      'id': 1,
      'title': 'Python Developer',
      'location': 'New York',
      'salary': '$100,000'
    },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'San Francisco',
    'salary': '$120,000'
  },
  {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Chicago',
    'salary': '$110,000'
  },
  {
    'id': 4,
    'title': 'Data Analyst',
    'location': 'Los Angeles',
    'salary': '$90,000'
  },
]

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def get_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)