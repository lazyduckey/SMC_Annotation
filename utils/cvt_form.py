import streamlit as st

def cvt_to_dict(streamlit_attrdict):
    if type(streamlit_attrdict) == st.runtime.secrets.AttrDict:
        streamlit_attrdict = dict(streamlit_attrdict)
        for key, value in streamlit_attrdict.items():
            streamlit_attrdict[key] = cvt_to_dict(streamlit_attrdict[key])
            if type(streamlit_attrdict) != st.runtime.secrets.AttrDict:
                key = value
                
    return streamlit_attrdict