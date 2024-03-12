from utils.categories import *


def get_index_action(selected_clip_info, role, hand, action):
    if role == 'oper':
        role_idx = 7
    elif role == 'assi':
        role_idx = 8
    
    if hand == 'left':
        hand_idx = 0
    elif hand == 'right':
        hand_idx = 1
        
    if action == 'tools':
        act_idx = 0
    elif action == 'verbs':
        act_idx = 1   
    elif action == 'targets':
        act_idx = 2
        
    return action_triplet_dict[action].index(selected_clip_info[role_idx].split('\n')[hand_idx].split(',')[act_idx]) if selected_clip_info[role_idx] else 0


def find_index(selected_clip_info, task_or_step_lst, idx):
    if selected_clip_info[idx]:
        if selected_clip_info[idx] in task_or_step_lst:
            return task_or_step_lst.index(selected_clip_info[idx])
        else:
            return selected_clip_info[-1]
    else:    
        return None
    
    
    