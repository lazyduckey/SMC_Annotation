import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import streamlit as st
import pandas as pd

creds, _ = google.auth.load_credentials_from_dict(dict(st.secrets['sheet_credentials']))

@st.cache_data
def get_cell_content(spreadsheet_id, whois):
    try:
        service = build("sheets", "v4", credentials=creds)

        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=whois+st.secrets['sheet_range'])
            .execute()
        )
        
        rows = result.get("values", [])
        print(f"{len(rows)} rows retrieved")
        return rows
    except HttpError as error:
        print(f"An error occurred: {error}")

def get_clip_info(cell_contents, video_number, clip_number):
    contents_for_video_number = [values for values in cell_contents if values[0] == video_number]
    
    for idx, values in enumerate(contents_for_video_number, 1):
        if idx == clip_number:
            return values
        
    print("Not Included Values")

@st.cache_data
def get_edit_state(spreadsheet_id, whois):
    try:
        service = build("sheets", "v4", credentials=creds)
        
        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=whois+st.secrets['edit_state_sheet_range'])
            .execute()
        )
        
        rows = result.get("values", [])
        print(f"{len(rows)} rows retrieved")
        return rows
    except HttpError as error:
        print(f"An error occurred: {error}")
    
# @st.cache_data   
def transform_to_df(spreadsheet_id, whois):
    data = get_edit_state(spreadsheet_id, whois)

    
    columns = data[0]
    edit_state_df = pd.DataFrame(columns=columns, data=data[1:])
    return edit_state_df


def init_edit_sheet_update(spreadsheet_id, edit_spreadsheet_id, whois):
    annotation_data = get_cell_content(spreadsheet_id, whois)
    
    edit_state = get_edit_state(edit_spreadsheet_id, whois)
    
    need_edit = False
    
    for idx, (annot, edit) in enumerate(list(zip(annotation_data, edit_state))):
        if True in [bool(content) for content in annot[2:9]]:
            if edit[2] == 'TRUE':
                continue
            else:
                edit_state[idx][2] = 'TRUE'
                need_edit = True
        else:
            if edit[2] == 'TRUE':
                edit_state[idx][2] = 'FALSE'
                need_edit = True
                
    if need_edit:            
        edit_state = [[state[2]] for state in edit_state[1:]]
        update_edit_values(edit_spreadsheet_id, whois+'!C2:C1278', "USER_ENTERED", edit_state)    
    else:
        print('Syncronized!')
    

def get_index_by_filter(cell_contents, video_number, start_time, end_time):

    for idx, values in enumerate(cell_contents, 1):
        if values[0] == video_number and values[9] == start_time and values[10] == end_time:
            return idx
    
    print("Not Included Values")
    
    
def update_edit_values(spreadsheet_id, range_name, value_input_option:str, _values:list):
    """
    Creates the batch_update the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
        service = build("sheets", "v4", credentials=creds)
        values = _values
        
        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{result.get('updatedCells')} cells updated.")
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    

def update_values(spreadsheet_id, range_name, value_input_option:str, _values:list):
    """
    Creates the batch_update the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
        service = build("sheets", "v4", credentials=creds)
        values = [
                _values
        ]
        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{result.get('updatedCells')} cells updated.")
        print(_values)
        # return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    



