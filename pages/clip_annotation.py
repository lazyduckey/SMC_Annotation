import streamlit as st
from annotated_text import annotated_text, annotation
from utils.video_clip import *
from utils.readsheet import *
from utils.categories import get_step_task_dict, get_action_triplet_dict
from utils.view_page import view_page
import pandas as pd

if 'next_video_num' not in st.session_state:
    st.session_state['next_video_num'] = 0

if 'next_clip_num' not in st.session_state:
    st.session_state['next_clip_num'] = 0

st.set_page_config(layout='wide')

if not st.session_state["authentication_status"]:
    st.write('# Login Failed !')
    st.stop()
    
step_task_dict = get_step_task_dict()
action_triplet_dict = get_action_triplet_dict()

whois = st.session_state['name']

spreadsheet_id = st.secrets['spreadsheet_id']

edit_spreadsheet_id = st.secrets['edit_spreadsheet_id']

cell_contents = get_cell_content(spreadsheet_id, whois)

video_number = get_video_numbers(st.secrets['clip_file_path'])

prior_col1, prior_col2 = st.columns((5,5))
with prior_col1:
    selected_video_num = st.selectbox('Select Video Number', [v_num for v_num in video_number], index=st.session_state['next_video_num'])

clips_num = get_clip_numbers(st.secrets['clip_file_path'], selected_video_num)

clips = get_clips(st.secrets['clip_file_path'], selected_video_num)

with prior_col2:
    selected_clip_num = st.selectbox('Select Video Clip Number', [c_num for c_num in clips_num], index=st.session_state['next_clip_num'] if st.session_state['next_video_num'] == selected_video_num else 0)
    st.session_state['next_clip_num'] = clips_num.index(selected_clip_num)

edit_state_df = transform_to_df(edit_spreadsheet_id, whois)

selected_clip_edit_state = edit_state_df[(edit_state_df['VideoNumber']==selected_video_num) & (edit_state_df['ClipNumber']==selected_clip_num.split('_')[-1])]
if selected_clip_edit_state.reset_index(drop=True)['editState'][0].upper() == 'TRUE':
    disabled = True
else:
    disabled = False

view_page(whois, spreadsheet_id, cell_contents, video_number, clips_num, clips, selected_video_num, selected_clip_num, selected_clip_edit_state, disabled)
