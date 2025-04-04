from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Functions
def get_all_asi_summaries():
    df = pd.read_csv('nid_mapped_asi.csv')
    nid_seen = []
    asi_list = []

    for id in df['nid']:
        if id not in nid_seen:
            asi_dict = {}
            row = df[df['nid'] == id]

            # print(row['title'].iloc[0]) # return series and why are fetching the first element
            
            asi_dict['nid'] = id
            asi_dict['title'] = row['title'].iloc[0]
            # asi_dict['folder'] = row['folder'].iloc[0]
            asi_dict['summary'] = row['summary'].iloc[0]
            asi_dict['pdf_path'] = row['pdf_path'].iloc[0]
            asi_dict['body'] = row['body'].iloc[0]

            asi_list.append(asi_dict)    
            nid_seen.append(id)
        else:
            same_nid_dict = [obj for obj in asi_list if obj['nid'] == id]
            same_nid_dict = same_nid_dict[0]
            same_nid_dict['summary'] += f"\n\n {same_nid_dict['summary']}"
            same_nid_dict['title'] += f", {same_nid_dict['title']}"
            same_nid_dict['pdf_path'] += f", {same_nid_dict['pdf_path']}"
    return asi_list


def get_all_dli_summaries():
    df = pd.read_csv(r'C:\Users\KushanSharma\OneDrive - Indian Culture Portal\Desktop\OCR Work\OCR Final Work\match_nids\nid_mapped_dli.csv')
    
    nid_seen = []
    dli_list = []

    for id in df['nid']:
        if id not in nid_seen:
            dli_dict = {}
            row = df[df['nid'] == id]

            # print(row['title'].iloc[0]) # return series and why are fetching the first element
            
            dli_dict['nid'] = id
            dli_dict['title'] = row['title'].iloc[0]
            dli_dict['summary'] = row['summary'].iloc[0]
            dli_dict['pdf_path'] = row['pdf_path'].iloc[0]

            dli_list.append(dli_dict)    
            nid_seen.append(id)
        else:
            same_nid_dict = [obj for obj in dli_list if obj['nid'] == id]
            same_nid_dict = same_nid_dict[0]
            same_nid_dict['summary'] += f"\n\n{same_nid_dict['summary']}"
            same_nid_dict['title'] += f", {same_nid_dict['title']}"
            same_nid_dict['pdf_path'] += f", {same_nid_dict['pdf_path']}"
    return dli_list


def get_all_csl_summaries():
    df = pd.read_excel(r'C:\Users\KushanSharma\OneDrive - Indian Culture Portal\Desktop\OCR Work\OCR Final Work\match_nids\csl-summaries.xlsx')

    csl_list = []
    nid_seen = []

    for id in df['nid']:
        row = row = df[df['nid'] == id]

        if id not in nid_seen:
            if len(row) > 1:
                csl_obj = {}
                for _, entry in row.iterrows():
                    if entry['nid'] not in nid_seen:
                        csl_obj['nid'] = str(entry['nid'])
                        csl_obj['title'] = entry['title']
                        csl_obj['pdf_path'] = entry['pdf_path']
                        csl_obj['summary'] = entry['summary']

                        csl_list.append(csl_obj)
                        nid_seen.append(entry['nid'])
                    else:
                        same_nid_dict = [obj for obj in csl_list if obj['nid'] == str(entry['nid'])][0]
                        same_nid_dict['title'] += f",  {entry['title']}"
                        same_nid_dict['pdf_path'] += f",  {entry['pdf_path']}"
                        same_nid_dict['summary'] += f"\n\n {entry['summary']}"         
            else:
                csl_obj = {}
                csl_obj['nid'] = str(row['nid'].iloc[0])
                csl_obj['title'] = row['title'].iloc[0]
                csl_obj['pdf_path'] = row['pdf_path'].iloc[0]
                csl_obj['summary'] = row['summary'].iloc[0]
                csl_list.append(csl_obj)
                nid_seen.append(row['nid'].iloc[0])

    return csl_list

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

# APIs
@app.post('/rest-v1/asi-summaries')
def asi_summaries():
    summaries = get_all_asi_summaries()

    if summaries:
        return jsonify(
            {'results': summaries}
        ), 200
    else:
        return jsonify({'message': 'Opeation Failed'}), 404


@app.post('/rest-v1/dli-summaries')
def dli_summaries():
    summaries = get_all_dli_summaries()

    if summaries:
        return jsonify(
            {'results': summaries}
        ), 200
    else:
        return jsonify({'message': 'Opeation Failed'}), 404


@app.post('/rest-v1/csl-summaries')
def csl_summaries():
    summaries = get_all_csl_summaries()
    if summaries:
        return jsonify(
            {'results': summaries}
        )
    else:
        return jsonify({'message': 'Opeation Failed'}), 404
    
