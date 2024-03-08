from utils.categories import *


def get_index_action(selected_clip_info, role, hand, action):
    if hand == 'right':
        hand_idx = 0
    elif hand == 'left':
        hand_idx = 1
        
    if role == 'oper':
        role_idx = 7
    elif role == 'assi':
        role_idx = 8
        
    if action == 'tools':
        act_idx = 0
    elif action == 'targets':
        act_idx = 1
    elif action == 'verbs':
        act_idx = 2
    
        
    return action_triplet_dict[action].index(selected_clip_info[role_idx].split('\n')[hand_idx].split(',')[act_idx]) if selected_clip_info[role_idx] else 0
