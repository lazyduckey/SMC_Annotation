import streamlit as st
from annotated_text import annotated_text, annotation
from utils.video_clip import *
from utils.readsheet import *
from utils.categories import *
from utils.util import *
import pandas as pd

def view_page(whois, spreadsheet_id, cell_contents, video_number, clips_num, clips,  selected_video_num, selected_clip_num, selected_clip_edit_state, disabled):
    
    st.header("SMC Surgical Video Clip Annotation", divider='rainbow')
    st.write('Clip Number :', selected_clip_num)

    selected_clip_info = get_clip_info(cell_contents, selected_video_num, int(selected_clip_num.split('_')[-1]))

    l_col, r_col = st.columns(2)
    with l_col:
        st.video(f'{st.secrets["basic_address"]}/{clips[clips_num.index(selected_clip_num)]}')
        st.write("timestamp")
        timestamp_container = st.container(border=True)
        with timestamp_container:
            space_l, col1, col2, space_r = st.columns((1, 2, 1, 0.5))
            with col1:
                annotated_text("start", annotation(selected_clip_info[-2], color="#52ffc2"))
            with col2:
                annotated_text("end", annotation(selected_clip_info[-1], color="#52ffc2"))
    with r_col:
        if True in [bool(content) for content in selected_clip_info[1:9]]:
            edit = st.button("Edit", type='secondary')
            if edit:
                update_values(st.secrets['edit_spreadsheet_id'], whois+f'!C{selected_clip_edit_state.index[0]+2}', 'USER_ENTERED', ['False'])
                st.cache_data.clear()
                st.rerun()
                
            
        oper_name = st.text_input("operation_name", value=selected_clip_info[2], disabled=disabled)
        bkgd = st.text_area("background", value=selected_clip_info[3], disabled=disabled)
        
        step = st.selectbox("step", (step_task_dict.keys()), index=None, placeholder='Select Step', disabled=disabled)
        if step == "input text":
            detailed_step = st.text_area("step", value=selected_clip_info[4], disabled=disabled)
            step = detailed_step
            
        task = st.selectbox("task", step_task_dict[step] if step in step_task_dict.keys() else ["input text"], index=None, placeholder='Select Task', disabled=disabled)
        if task == "input text":
            detailed_task = st.text_area("task", value=selected_clip_info[5], disabled=disabled)
            task = detailed_task
            
        next = st.text_input("next", value=selected_clip_info[6], disabled=disabled)
        
        st.write("Action Operator")
        container_oper = st.container(border=True)
        with container_oper:
            act_oper_coll_1, act_oper_coll_2, act_oper_coll_3 = st.columns(3)
            act_oper_colr_1, act_oper_colr_2, act_oper_colr_3 = st.columns(3)
            with act_oper_coll_1:
                act_oper_left_tool = st.selectbox("action_operator left tool", 
                                                  action_triplet_dict['tools'], 
                                                  index=get_index_action(selected_clip_info, 'oper', 'left', 'tools'), 
                                                  placeholder='Select Tool', 
                                                  disabled=disabled)
            with act_oper_coll_2:
                act_oper_left_target = st.selectbox("action_operator left target", 
                                                    action_triplet_dict['targets'], 
                                                    index=get_index_action(selected_clip_info, 'oper', 'left', 'targets'), 
                                                    placeholder='Select Target', 
                                                    disabled=disabled)
            with act_oper_coll_3:
                act_oper_left_verb = st.selectbox("action_operator left verb", 
                                                  action_triplet_dict['verbs'], 
                                                  index=get_index_action(selected_clip_info, 'oper', 'left', 'verbs'), 
                                                  placeholder='Select Verb', 
                                                  disabled=disabled)
            with act_oper_colr_1:
                act_oper_right_tool = st.selectbox("action_operator right tool", 
                                                   action_triplet_dict['tools'], 
                                                   index=get_index_action(selected_clip_info, 'oper', 'right', 'tools'), 
                                                   placeholder='Select Tool', 
                                                   disabled=disabled)
            with act_oper_colr_2:
                act_oper_right_target = st.selectbox("action_operator right target", 
                                                     action_triplet_dict['targets'], 
                                                     index=get_index_action(selected_clip_info, 'oper', 'right', 'targets'), 
                                                     placeholder='Select Target', 
                                                     disabled=disabled)
            with act_oper_colr_3:
                act_oper_right_verb = st.selectbox("action_operator right verb", 
                                                   action_triplet_dict['verbs'], 
                                                   index=get_index_action(selected_clip_info, 'oper', 'right', 'verbs'), 
                                                   placeholder='Select Verb', 
                                                   disabled=disabled)
                
        act_oper = f'''{act_oper_left_tool},{act_oper_left_target},{act_oper_left_verb}
{act_oper_right_tool},{act_oper_right_target},{act_oper_right_verb}'''

        container_assi = st.container(border=True)
        with container_assi:
            act_assi_coll_1, act_assi_coll_2, act_assi_coll_3 = st.columns(3)
            act_assi_colr_1, act_assi_colr_2, act_assi_colr_3 = st.columns(3)
            with act_assi_coll_1:
                act_assi_left_tool = st.selectbox("action_assistant left tool", 
                                                  action_triplet_dict['tools'], 
                                                  index=get_index_action(selected_clip_info, 'assi', 'left', 'tools'), 
                                                  placeholder='Select Tool', 
                                                  disabled=disabled)
            with act_assi_coll_2:
                act_assi_left_target = st.selectbox("action_assistant left target", 
                                                    action_triplet_dict['targets'], 
                                                    index=get_index_action(selected_clip_info, 'assi', 'left', 'targets'), 
                                                    placeholder='Select Target', 
                                                    disabled=disabled)
            with act_assi_coll_3:
                act_assi_left_verb = st.selectbox("action_assistant left verb", 
                                                  action_triplet_dict['verbs'], 
                                                  index=get_index_action(selected_clip_info, 'assi', 'left', 'verbs'), 
                                                  placeholder='Select Verb', 
                                                  disabled=disabled)
            with act_assi_colr_1:
                act_assi_right_tool = st.selectbox("action_assistant right tool", 
                                                   action_triplet_dict['tools'], 
                                                   index=get_index_action(selected_clip_info, 'assi', 'right', 'tools'), 
                                                   placeholder='Select Tool', 
                                                   disabled=disabled)
            with act_assi_colr_2:
                act_assi_right_target = st.selectbox("action_assistant right target", 
                                                     action_triplet_dict['targets'], 
                                                     index=get_index_action(selected_clip_info, 'assi', 'right', 'targets'), 
                                                     placeholder='Select Target', 
                                                     disabled=disabled)
            with act_assi_colr_3:
                act_assi_right_verb = st.selectbox("action_assistant right verb", 
                                                   action_triplet_dict['verbs'], 
                                                   index=get_index_action(selected_clip_info, 'assi', 'right', 'verbs'), 
                                                   placeholder='Select Verb', 
                                                   disabled=disabled)
        act_assi = f'''{act_assi_left_tool},{act_assi_left_target},{act_assi_left_verb}
{act_assi_right_tool},{act_assi_right_target},{act_assi_right_verb}'''
                
        submit_col, _, next_col = st.columns((2,6,1))
        with submit_col:
            submit_btn = st.button("Submit", type='primary')
        with next_col:
            next_btn = st.button("Next", type="secondary", disabled=not disabled)
            

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
