import streamlit as st

@st.cache_data(persist=True)
def get_step_task_dict():
    return step_task_dict

@st.cache_data(persist=True)
def get_action_triplet_dict():
    return action_triplet_dict

step_task_dict = {
    "trocar placement": ["trocar placement"], 
    "left liver mobilization": ["dissection of the round ligament", 
                                "dissection of the falciform ligament", 
                                "dissection of the left coronary ligament", 
                                "dissection of the left triangular ligament",
                                "dissection of the hepatogastric ligament",
                                "hemostasis(bleeding control)",
                                "adhesiolysis",
                                "input text"],
    "parenchymal transection": ["demarcation of left lateral section",
                                "pringle's maneuvor",
                                "parenchymal transection",
                                "inflow control_division of G2 and G3",
                                "outflow control_division of left hepatic vein",
                                "hemostasis(bleeding control)",
                                "adhesiolysis",
                                "input text"],
    "hemostasis after transection": ["hemostasis of the transected liver surface", 
                                     "hemostasis of the perihepatic tissue",
                                     "hemostasis(bleeding control)",
                                     "adhesiolysis",
                                     "input text"],
    "extraction and drainage": ["package of the specimen",
                                "drainage tube placement",
                                "hemostasis(bleeding control)",
                                "adhesiolysis",
                                "hemostatic agents placement",
                                "anti-adhesive agents placement",
                                "input text"],
    "cholecystectomy": ["Calot triangle dissection",
                        "clipping and cutting",
                        "gall bladder dissection",
                        "hemostasis(bleeding control)",
                        "adhesiolysis",
                        "input text"],
    '**': ["hemostasis(bleeding control)",
           "adhesiolysis",
           "anti-adhesive agents placement",
           "hemostatic agents placement",
           "hemostasis(bleeding control)",
           "adhesiolysis",
           "input text"],
    "input text": ["input text"],
    None: [None]}

action_triplet_dict = {
    'tools': ['null',
             'grasper', 
             'hook', 
             'sonicision', 
             'bipolar', 
             'scissor', 
             'clipper', 
             'suction', 
             'specimen_bag', 
             'stapler', 
             'gauze', 
             'needle_holder', 
             'hemostatic agents', 
             'anti-adhesive agents', 
             'hemolock clip', 
             'bulldog clamp', 
             'bulldog',
             'right angle',
             'input text'],
    'targets': ['null',
               'round ligament',
               'falciform ligament', 
               'left coronary ligament',
               'left triangular ligament', 
               'hepatogastric ligament',
               'liver',
               'liver parenchyma',
               'left hepatic vein',
               'vein',
               'G2 and G3',
               'glisson',
               'specimen',
               'drain tube',
               'gauze',
               'blood',
               'bile',
               'adhesion',
               'cystic artery',
               'cystic duct',
               'cystic pedicle',
               'cystic plate',
               'fat',
               'gall bladder',
               'hepatoduodenal ligament',
               'omentum',
               'liver surface',
               'around of op site',
               'fluid',
               'intrahepatic vein',
               'input text'],
    'verbs': ['null',
             'dissect',
             'coagulate',
             'divide',
             'clip',
             'clamp',
             'cut',
             'suture',
             'pack',
             'place',
             'aspirate',
             'grasp',
             'suction',
             'irrigation',
             'retract',
             'tear',
             'removal',
             'input text']}