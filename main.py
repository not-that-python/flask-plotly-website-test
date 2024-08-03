from flask import Flask, jsonify, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__, static_url_path='', static_folder='')

# Sample dataframe
data = {
  'name': ['Alice', 'Bob', 'Charlie', 'Denise'],
  'age': [12, 14, 13, 15]
}
df = pd.DataFrame(data)

# This can be removed when we figure out how to host it I think
@app.route('/')
def home():
  data_canada = px.data.gapminder().query("country == 'Canada'")
  fig = px.bar(data_canada, x='year', y='pop')

  # plotly_jinja_data = {"fig":fig.to_html(full_html=False)}
  return render_template('index_new.html', plot=fig.to_html(full_html=True))
  # pio.write_html(fig, '')
#  return render_template('index_old.html')

# Should return a JSON version of the sample df
@app.route('/api/data', methods=['GET'])
def get_data():
  print("hi")
  return jsonify(df.to_dict(orient='records'))

# Just an API I made to make sure it works
@app.route('/coolapi')
def works():
  print("it works")
  return {'message': 'it works'}

if __name__ == '__main__':
  app.run(debug=False)