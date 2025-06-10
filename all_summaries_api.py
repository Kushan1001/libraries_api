from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

excel_df = pd.read_excel('all-20k-summaries.xlsx')

output_list = []

for idx, row in excel_df.iterrows():
    summary_obj = {}
    summary_obj['nid'] = row['nid']
    summary_obj['title'] = row['title']
    summary_obj['summary'] = row['summaries']

    output_list.append(summary_obj)

@app.get('/rest/api/all-summaries')
def all_summaries():
    return jsonify({'results': output_list}), 200


