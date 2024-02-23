import streamlit as st
from annotated_text import annotated_text, annotation
from utils.video_clip import *
from utils.readsheet import *

st.set_page_config(layout='wide')

if not st.session_state["authentication_status"]:
    st.write('# Login Failed !')
    st.stop()

spreadsheet_id = st.secrets['spreadsheet_id']

cell_contents = get_cell_content(spreadsheet_id)

video_number = get_video_numbers(st.secrets['clip_file_path'])

prior_col1, prior_col2 = st.columns((5,5))
with prior_col1:
    selected_video_num = st.selectbox('Select Video Number', [v_num for v_num in video_number])

clips_num = get_clip_numbers(st.secrets['clip_file_path'], selected_video_num)

clips = get_clips(st.secrets['clip_file_path'], selected_video_num)

with prior_col2:
    selected_clip_num = st.selectbox('Select Video Clip Number', [i for i in clips_num])


st.header("SMC Surgical Video Clip Annotation", divider='rainbow')
st.write('Clip Number :', selected_clip_num)

selected_clip_info = get_clip_info(cell_contents, selected_video_num, int(selected_clip_num.split('_')[-1]))

l_col, r_col = st.columns(2)
with l_col:
    st.video(f'{st.secrets["basic_address"]}/{clips[clips_num.index(selected_clip_num)]}')
    space_l, col1, col2, space_r = st.columns((5, 2, 2, 5))

with r_col:
    with st.form(f"Video Clip Information_{selected_video_num}", clear_on_submit=True):   
        if True in [bool(content) for content in selected_clip_info[1:8]]:
            is_contents = True
            edit = st.form_submit_button("Edit")

            if edit:
                is_contents = False
                
        else:
            is_contents = False
            
        annot = st.radio("Annotator", ("SJ", "EY", "NK", "JY"), index=check_index(selected_clip_info), horizontal=True, disabled=is_contents)
        oper_name = st.text_input("operation_name", value=selected_clip_info[2], disabled=is_contents)
        bkgd = st.text_area("background", value=selected_clip_info[3], disabled=is_contents)
        step = st.text_input("step", value=selected_clip_info[4], disabled=is_contents)
        task = st.text_input("task", value=selected_clip_info[5], disabled=is_contents)
        next = st.text_input("next", value=selected_clip_info[6], disabled=is_contents)
        act_oper = st.text_area("action_operator", value=selected_clip_info[7], disabled=is_contents)
        act_assi = st.text_area("action_assistant", value=selected_clip_info[8], disabled=is_contents)
        st.write("timestamp")
        space1, start_col, end_col, space2 = st.columns((0.5, 2, 2, 0.5))
        with start_col:
            annotated_text("start", annotation(selected_clip_info[-2], color="#52ffc2"))
        with end_col:
            annotated_text("end", annotation(selected_clip_info[-1], color="#52ffc2"))

        submit = st.form_submit_button("Submit", type='primary')

if submit:
    video_num = selected_video_num
    values = [annot, oper_name, bkgd, step, task, next, act_oper, act_assi]

    update_idx = get_index_by_filter(cell_contents, video_num, selected_clip_info[-2], selected_clip_info[-1])

    if update_idx:
        range_name = f'Sheet1!B{update_idx}:I{update_idx}'
        update_values(spreadsheet_id, range_name, "USER_ENTERED", values)
        
        
    st.rerun()