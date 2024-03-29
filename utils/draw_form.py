import streamlit as st
from utils.util import *
from annotated_text import annotated_text, annotation

def draw_video_form(clips, clips_num, selected_clip_num, selected_clip_info):
    st.video(f'{st.secrets["basic_address"]}/{clips[clips_num.index(selected_clip_num)]}')
    st.write("timestamp")
    timestamp_container = st.container(border=True)
    with timestamp_container:
        space_l, col1, col2, space_r = st.columns((1, 2, 1, 0.5))
        with col1:
            annotated_text("start", annotation(selected_clip_info[-2], color="#52ffc2"))
        with col2:
            annotated_text("end", annotation(selected_clip_info[-1], color="#52ffc2"))

def draw_step(selected_clip_info, disabled):
    step = st.selectbox("step", (step_task_dict.keys()), index=find_task_index(selected_clip_info, list(step_task_dict.keys()), 4), placeholder='Select Step', disabled=disabled)
    if step == "input text":
        detailed_step = st.text_area("step", value=selected_clip_info[4], disabled=disabled)
        step = detailed_step
        
    return step

def draw_task(step, selected_clip_info, disabled):
    task = st.selectbox("task", step_task_dict[step] if step in step_task_dict.keys() else step_task_dict["input text"], index=find_step_index(selected_clip_info, step if step else None, 5), placeholder='Select Task', disabled=disabled)
    if task == "input text":
        detailed_task = st.text_area("task", value=selected_clip_info[5], disabled=disabled)
        task = detailed_task
        
    return task

def draw_oper_action(action_triplet_dict, selected_clip_info, disabled):
    st.write("Action Operator")
    container_oper = st.container(border=True)
    with container_oper:
        act_oper_coll_1, act_oper_coll_2, act_oper_coll_3 = st.columns(3)
        act_oper_colr_1, act_oper_colr_2, act_oper_colr_3 = st.columns(3)
        with act_oper_coll_1:
            act_oper_left_tool = st.selectbox("action_operator left tool", 
                                                action_triplet_dict['tools'], 
                                                index=get_index_action(0, get_value_action(selected_clip_info, 'oper', 'left', 'tools')),
                                                placeholder='Select Tool', 
                                                disabled=disabled)
            if act_oper_left_tool == "input text":
                detailed_act_oper_left_tool = st.text_area("act_oper_left_tool", value=get_value_action(selected_clip_info, 'oper', 'left', 'tools'), disabled=disabled)
                act_oper_left_tool = detailed_act_oper_left_tool
            
        with act_oper_coll_2:
            act_oper_left_verb = st.selectbox("action_operator left verb", 
                                                action_triplet_dict['verbs'], 
                                                index=get_index_action(1, get_value_action(selected_clip_info, 'oper', 'left', 'verbs')),
                                                placeholder='Select Verb', 
                                                disabled=disabled)
            if act_oper_left_verb == "input text":
                detailed_act_oper_left_verb = st.text_area("act_oper_left_verb", value=get_value_action(selected_clip_info, 'oper', 'left', 'verbs'), disabled=disabled)
                act_oper_left_verb = detailed_act_oper_left_verb
            
    
        with act_oper_coll_3:
            act_oper_left_target = st.selectbox("action_operator left target", 
                                                action_triplet_dict['targets'], 
                                                index=get_index_action(2, get_value_action(selected_clip_info, 'oper', 'left', 'targets')),
                                                placeholder='Select Target', 
                                                disabled=disabled)
            if act_oper_left_target == "input text":
                detailed_act_oper_left_target = st.text_area("act_oper_left_target", value=get_value_action(selected_clip_info, 'oper', 'left', 'targets'), disabled=disabled)
                act_oper_left_targetl = detailed_act_oper_left_target
            

        with act_oper_colr_1:
            act_oper_right_tool = st.selectbox("action_operator right tool", 
                                                action_triplet_dict['tools'], 
                                                index=get_index_action(0, get_value_action(selected_clip_info, 'oper', 'right', 'tools')), 
                                                placeholder='Select Tool', 
                                                disabled=disabled)
            if act_oper_right_tool == "input text":
                detailed_act_oper_right_tool = st.text_area("act_oper_right_tool", value=get_value_action(selected_clip_info, 'oper', 'right', 'tools'), disabled=disabled)
                act_oper_right_tool = detailed_act_oper_right_tool
            
            
        with act_oper_colr_2:
            act_oper_right_verb = st.selectbox("action_operator right verb", 
                                                action_triplet_dict['verbs'], 
                                                index=get_index_action(1, get_value_action(selected_clip_info, 'oper', 'right', 'verbs')), 
                                                placeholder='Select Verb', 
                                                disabled=disabled)   
            if act_oper_right_verb == "input text":
                detailed_act_oper_right_verb = st.text_area("act_oper_right_verb", value=get_value_action(selected_clip_info, 'oper', 'right', 'verbs'), disabled=disabled)
                act_oper_right_verb = detailed_act_oper_right_verb
            
            
        with act_oper_colr_3:
            act_oper_right_target = st.selectbox("action_operator right target", 
                                                    action_triplet_dict['targets'], 
                                                    index=get_index_action(2, get_value_action(selected_clip_info, 'oper', 'right', 'targets')), 
                                                    placeholder='Select Target', 
                                                    disabled=disabled)
            if act_oper_right_target == "input text":
                detailed_act_oper_right_target = st.text_area("act_oper_right_target", value=get_value_action(selected_clip_info, 'oper', 'right', 'targets'), disabled=disabled)
                act_oper_right_target = detailed_act_oper_right_target
            

            
    return f'''{act_oper_left_tool},{act_oper_left_verb},{act_oper_left_target}
{act_oper_right_tool},{act_oper_right_verb},{act_oper_right_target}'''

def draw_assi_action(action_triplet_dict, selected_clip_info, disabled):
    st.write("Action Assistant")
    container_assi = st.container(border=True)
    with container_assi:
        act_assi_coll_1, act_assi_coll_2, act_assi_coll_3 = st.columns(3)
        act_assi_colr_1, act_assi_colr_2, act_assi_colr_3 = st.columns(3)
        with act_assi_coll_1:
            act_assi_left_tool = st.selectbox("action_assistant left tool", 
                                                action_triplet_dict['tools'], 
                                                index=get_index_action(0, get_value_action(selected_clip_info, 'assi', 'left', 'tools')), 
                                                placeholder='Select Tool', 
                                                disabled=disabled)
            if act_assi_left_tool == "input text":
                detailed_act_assi_left_tool = st.text_area("act_assi_left_tool", value=get_value_action(selected_clip_info, 'assi', 'left', 'tools'), disabled=disabled)
                act_assi_left_tool = detailed_act_assi_left_tool
            
            
        with act_assi_coll_2:
            act_assi_left_verb = st.selectbox("action_assistant left verb", 
                                                action_triplet_dict['verbs'], 
                                                index=get_index_action(1, get_value_action(selected_clip_info, 'assi', 'left', 'verbs')), 
                                                placeholder='Select Verb', 
                                                disabled=disabled)    
            if act_assi_left_verb == "input text":
                detailed_act_assi_left_verb = st.text_area("act_assi_left_verb", value=get_value_action(selected_clip_info, 'assi', 'left', 'verbs'), disabled=disabled)
                act_assi_left_verb = detailed_act_assi_left_verb
            
            
        with act_assi_coll_3:
            act_assi_left_target = st.selectbox("action_assistant left target", 
                                                action_triplet_dict['targets'], 
                                                index=get_index_action(2, get_value_action(selected_clip_info, 'assi', 'left', 'targets')), 
                                                placeholder='Select Target', 
                                                disabled=disabled)
            if act_assi_left_target == "input text":
                detailed_act_assi_left_target = st.text_area("act_assi_left_target", value=get_value_action(selected_clip_info, 'assi', 'left', 'targets'), disabled=disabled)
                act_assi_left_target = detailed_act_assi_left_target
            
            
        with act_assi_colr_1:
            act_assi_right_tool = st.selectbox("action_assistant right tool", 
                                                action_triplet_dict['tools'], 
                                                index=get_index_action(0, get_value_action(selected_clip_info, 'assi', 'right', 'tools')), 
                                                placeholder='Select Tool', 
                                                disabled=disabled)
            if act_assi_right_tool == "input text":
                detailed_act_assi_right_tool = st.text_area("act_assi_right_tool", value=get_value_action(selected_clip_info, 'assi', 'right', 'tools'), disabled=disabled)
                act_assi_right_tool = detailed_act_assi_right_tool
            
        with act_assi_colr_2:
            act_assi_right_verb = st.selectbox("action_assistant right verb", 
                                                action_triplet_dict['verbs'], 
                                                index=get_index_action(1, get_value_action(selected_clip_info, 'assi', 'right', 'verbs')), 
                                                placeholder='Select Verb', 
                                                disabled=disabled)    
            if act_assi_right_verb == "input text":
                detailed_act_assi_right_verb = st.text_area("act_assi_right_verb", value=get_value_action(selected_clip_info, 'assi', 'right', 'verbs'), disabled=disabled)
                act_assi_right_verb = detailed_act_assi_right_verb
            
        with act_assi_colr_3:
            act_assi_right_target = st.selectbox("action_assistant right target", 
                                                    action_triplet_dict['targets'], 
                                                    index=get_index_action(2, get_value_action(selected_clip_info, 'assi', 'right', 'targets')), 
                                                    placeholder='Select Target', 
                                                    disabled=disabled)
            if act_assi_right_target == "input text":
                detailed_act_assi_right_target = st.text_area("act_assi_right_target", value=get_value_action(selected_clip_info, 'assi', 'right', 'targets'), disabled=disabled)
                act_assi_right_target = detailed_act_assi_right_target
            
    return f'''{act_assi_left_tool},{act_assi_left_verb},{act_assi_left_target}
{act_assi_right_tool},{act_assi_right_verb},{act_assi_right_target}'''