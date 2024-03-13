from utils.categories import *

def get_index_action(act_idx, act):
    if act_idx == 0:
        if act in action_triplet_dict['tools']:
            return action_triplet_dict['tools'].index(act)
        else:
            return action_triplet_dict['tools'].index(action_triplet_dict['tools'][-1])
    elif act_idx == 1:
        if act in action_triplet_dict['verbs']:
            return action_triplet_dict['verbs'].index(act)
        else:
            return action_triplet_dict['verbs'].index(action_triplet_dict['verbs'][-1])
    elif act_idx == 2:
        if act in action_triplet_dict['targets']:
            return action_triplet_dict['targets'].index(act)
        else:
            return action_triplet_dict['targets'].index(action_triplet_dict['targets'][-1])

def get_value_action(selected_clip_info, role, hand, action):
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
        
    return selected_clip_info[role_idx].split('\n')[hand_idx].split(',')[act_idx] if selected_clip_info[role_idx] else None

def find_index(selected_clip_info, task_or_step_lst, idx):
    if selected_clip_info[idx]:
        if selected_clip_info[idx] in task_or_step_lst:
            return task_or_step_lst.index(selected_clip_info[idx])
        else:
            return selected_clip_info[-1]
    else:    
        return None
    
    
    