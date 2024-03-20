import streamlit as st
from utils.video_clip import *
from utils.readsheet import *
from utils.categories import *
from utils.util import *
from utils.draw_form import *
import pandas as pd

def view_page(whois, spreadsheet_id, cell_contents, video_number, clips_num, clips,  selected_video_num, selected_clip_num, selected_clip_edit_state, disabled):
    
    st.header("SMC Surgical Video Clip Annotation", divider='rainbow')
    st.write('Clip Number :', selected_clip_num)

    selected_clip_info = get_clip_info(cell_contents, selected_video_num, int(selected_clip_num.split('_')[-1]))

    l_col, r_col = st.columns(2)
    with l_col:
        draw_video_form(clips, clips_num, selected_clip_num, selected_clip_info)
        
    with r_col:
        if True in [bool(content) for content in selected_clip_info[1:9]]:
            edit = st.button("Edit", type='secondary')
            if edit:
                update_values(st.secrets['edit_spreadsheet_id'], whois+f'!C{selected_clip_edit_state.index[0]+2}', 'USER_ENTERED', ['False'])
                st.cache_data.clear()
                st.rerun()
            
        oper_name = st.text_input("operation_name", value=selected_clip_info[2], disabled=disabled)
        bkgd = st.text_area("background", value=selected_clip_info[3], disabled=disabled)
        
        step = draw_step(selected_clip_info, disabled)
            
        task = draw_task(step, selected_clip_info, disabled)
            
        next = st.text_area("next", value=selected_clip_info[6], disabled=disabled)
        
        act_oper = draw_oper_action(action_triplet_dict, selected_clip_info, disabled)
        
        act_assi = draw_assi_action(action_triplet_dict, selected_clip_info, disabled)
                
        submit_col, _, next_col = st.columns((2,6,1))
        with submit_col:
            submit_btn = st.button("Submit", type='primary')
        with next_col:
            next_btn = st.button("Next Clip", type="secondary", disabled=not disabled)
            
    if submit_btn:
        video_num = selected_video_num
        values = ['', oper_name, bkgd, step, task, next, act_oper, act_assi]

        update_idx = get_index_by_filter(cell_contents, video_num, selected_clip_info[-2], selected_clip_info[-1])

        if update_idx:
            range_name = f'{whois}!B{update_idx}:I{update_idx}'
            update_values(spreadsheet_id, range_name, "USER_ENTERED", values)
            
        update_values(st.secrets['edit_spreadsheet_id'], whois+f'!C{selected_clip_edit_state.index[0]+2}', 'USER_ENTERED', ['True'])

        st.cache_data.clear()
        st.rerun()
        
    if next_btn:
        st.session_state['next_clip_num'] += 1
        if st.session_state['next_clip_num'] + 1 > len(clips):
            st.session_state['next_video_num'] += 1
            st.session_state['next_clip_num'] = 0

        st.rerun()
