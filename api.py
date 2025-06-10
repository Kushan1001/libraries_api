from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Functions

def get_all_asi_summaries():
    df = pd.read_csv('asi-summaries.csv')

    asi_list = []
    nid_seen = []

    for id in df['nid']:
        row = row = df[df['nid'] == id]

        if id not in nid_seen:
            if len(row) > 1:
                asi_obj = {}
                for _, entry in row.iterrows():
                    if entry['nid'] not in nid_seen:
                        asi_obj['nid'] = str(entry['nid'])
                        asi_obj['title'] = entry['title']
                        asi_obj['pdf_path'] = entry['pdf_path']
                        asi_obj['summary'] = entry['summary']

                        asi_list.append(asi_obj)
                        nid_seen.append(entry['nid'])
                    else:
                        same_nid_dict = [obj for obj in asi_list if obj['nid'] == str(entry['nid'])][0]
                        same_nid_dict['title'] += f",  {entry['title']}"
                        same_nid_dict['pdf_path'] += f",  {entry['pdf_path']}"
                        same_nid_dict['summary'] += f"\n\n {entry['summary']}"         
            else:
                asi_obj = {}
                asi_obj['nid'] = str(row['nid'].iloc[0])
                asi_obj['title'] = row['title'].iloc[0]
                asi_obj['pdf_path'] = row['pdf_path'].iloc[0]
                asi_obj['summary'] = row['summary'].iloc[0]
                asi_list.append(asi_obj)
                nid_seen.append(row['nid'].iloc[0])

    return asi_list


def get_all_dli_summaries():
    df = pd.read_csv('dli-summaries.csv')
    
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
    df = pd.read_excel('csl-summaries.xlsx')

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

def get_all_ignca_summaries():
    df = pd.read_excel('ignca-summaries.xlsx')

    ignca_list = []
    nid_seen = []

    for id in df['nid']:
        row = row = df[df['nid'] == id]

        if id not in nid_seen:
            if len(row) > 1:
                ignca_obj = {}
                for _, entry in row.iterrows():
                    if entry['nid'] not in nid_seen:
                        ignca_obj['nid'] = str(entry['nid'])
                        ignca_obj['title'] = entry['title']
                        ignca_obj['pdf_path'] = entry['pdf_path']
                        ignca_obj['summary'] = entry['summary']

                        ignca_list.append(ignca_obj)
                        nid_seen.append(entry['nid'])
                    # else:
                    #     same_nid_dict = [obj for obj in ignca_list if obj['nid'] == str(entry['nid'])][0]
                    #     same_nid_dict['title'] += f",  {entry['title']}"
                    #     same_nid_dict['pdf_path'] += f",  {entry['pdf_path']}"
                    #     same_nid_dict['summary'] += f"\n\n {entry['summary']}"         
            else:
                ignca_obj = {}
                ignca_obj['nid'] = str(row['nid'].iloc[0])
                ignca_obj['title'] = row['title'].iloc[0]
                ignca_obj['pdf_path'] = row['pdf_path'].iloc[0]
                ignca_obj['summary'] = row['summary'].iloc[0]
                ignca_list.append(ignca_obj)
                nid_seen.append(row['nid'].iloc[0])

    return ignca_list


def get_all_nli_summaries():
    df = pd.read_excel('completed_nli-summaries.xlsx')

    nli_list = []
    nid_seen = []

    for id in df['nid']:
        row = row = df[df['nid'] == id]

        if id not in nid_seen:
            if len(row) > 1:
                nli_obj = {}
                for _, entry in row.iterrows():
                    if entry['nid'] not in nid_seen:
                        nli_obj['nid'] = str(entry['nid'])
                        nli_obj['title'] = entry['title']
                        nli_obj['pdf_path'] = entry['pdf_path']
                        nli_obj['summary'] = entry['summary']

                        nli_list.append(nli_obj)
                        nid_seen.append(entry['nid'])
                    # else:
                    #     same_nid_dict = [obj for obj in ignca_list if obj['nid'] == str(entry['nid'])][0]
                    #     same_nid_dict['title'] += f",  {entry['title']}"
                    #     same_nid_dict['pdf_path'] += f",  {entry['pdf_path']}"
                    #     same_nid_dict['summary'] += f"\n\n {entry['summary']}"         
            else:
                nli_obj = {}
                nli_obj['nid'] = str(row['nid'].iloc[0])
                nli_obj['title'] = row['title'].iloc[0]
                nli_obj['pdf_path'] = row['pdf_path'].iloc[0]
                nli_obj['summary'] = row['summary'].iloc[0]
                nli_list.append(nli_obj)
                nid_seen.append(row['nid'].iloc[0])

    return nli_list


excel_df = pd.read_excel('all-20k-summaries.xlsx')
output_list = []

for idx, row in excel_df.iterrows():
    summary_obj = {}
    summary_obj['nid'] = row['nid']
    summary_obj['title'] = row['title']
    summary_obj['summary'] = row['summaries']

    output_list.append(summary_obj)


#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

# APIs
# Done
@app.post('/rest-v1/asi-summaries')
def asi_summaries():
    summaries = get_all_asi_summaries()

    if summaries:
        return jsonify(
            {'results': summaries}
        ), 200
    else:
        return jsonify({'message': 'Opeation Failed'}), 404


# Done
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


@app.post('/rest-v1/ignca-summaries')
def ignca_summaries():
    summaries = get_all_ignca_summaries()
    if summaries:
        return jsonify(
            {'results': summaries}
        )
    else:
        return jsonify({'message': 'Opeation Failed'}), 404
    
@app.post('/rest-v1/nli-summaries')
def nli_summaries():
    summaries = get_all_nli_summaries()
    if summaries:
        return jsonify(
            {'results': summaries}
        )
    else:
        return jsonify({'message': 'Opeation Failed'}), 404

excel_df = pd.read_excel('all-20k-summaries.xlsx')


@app.get('/rest-v1/all-summaries')
def all_summaries():
    return jsonify({'results': output_list}), 200
    

