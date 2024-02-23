import streamlit as st
from video_clip import *
from st_pages import show_pages_from_config, add_page_title, hide_pages, show_pages, Page
import streamlit_authenticator as stauth
from cvt_form import cvt_to_dict 

def main():
    st.set_page_config(layout='wide')

    add_page_title()
    show_pages_from_config()
    hide_pages(["Annotation"])
    
    accounts = cvt_to_dict(st.secrets['account'])
    
    authenticator = stauth.Authenticate(
        accounts['credentials'],
        accounts['cookie']['name'],
        accounts['cookie']['key'],
        accounts['cookie']['expiry_days'],
        accounts['preauthorized']
    )

    authenticator.login()

    

    if st.session_state["authentication_status"]:
        st.write(f'### Login Success! \n Welcome *{st.session_state["name"]}*')
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Annotation Page", type='primary'):
                st.switch_page(st.secrets['go_pages'])

        with col2:
            authenticator.logout()
        
        
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

if __name__ == "__main__":
    main()