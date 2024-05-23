from copy import deepcopy


STRICT = 'STRICT'
RELAXED = 'RELAXED'
SPLITTED = 'SPLITTED'
COMPOUND = 'COMPOUND'
# max gpt tokens
MAX_TOKENS = 750
# relation SEP
SEP_RELATION = ' -> '

NOT_DEFINED = 'NOT DEFINED'
PET_GOLD_ACTIVITY_LABEL = 'goldactivitylabels.json'
PET_GOLD_FILENAME = 'GoldData_PET_TEST.json'
PROCESS_DESCRIPTION = 'process description'
ACTIVITY_VALIDITY = '../activity_validity.json'
######
#  numbered activity. activity with the same name are numbered to differentiate them
#####

# for T1
GOLD_ACTIVITY_LIST = 'gold activity list'
GOLD_ACTIVITY_LIST_NUMBERED = 'gold activity list numbered'

ACTIVITY_LIST = 'activity list'

#  other tags for activity
ACTIVITY_INDEX = 'GOLD ACTIVITY INDEX'

GOLD_RAW_ACTIVITY_LABEL = 'gold RAW activity label'

GOLD_ACTIVITY_LABEL = 'gold activity label'
GOLD_ACTIVITY_LABEL_NUMBERED = 'gold activity label numbered'

# for T2
GOLD_ACTOR_LIST = 'gold actor list'
GOLD_ACTOR_LIST_MANUAL_FIX = 'gold actor list manual fix'

ACTOR_LIST = 'actor list'

# for T3
GOLD_PERFORMS_LIST = 'gold performs list'
GOLD_PERFORMS_LIST_MANUALLY_FIXED = 'gold performs list manually fixed'

PERFORMS_LIST = 'performs list'

# for T4
GOLD_DFG_LIST = 'gold dfg list'
GOLD_DFG_LIST_NUMBERED = 'gold dfg list numbered'

DFG_LIST = 'dfg list'

# for all
RAW_ANSWERS = 'raw answers'
RAW_ANSWER = 'raw answer'
EXTRACTED = 'extracted'

_SINGLE_ANSWER = {
        RAW_ANSWER: '',
        EXTRACTED:  list(),
}

#  train_doc_folds
MIN_ELEMENTS = 'min-elements'
TRAIN_FOLD_MIN_ELEMENTS_DOCS = [
    'doc-8.1',
    'doc-10.13'
    ]
MAX_ELEMENTS = 'max-elements'
TRAIN_FOLD_MAX_ELEMENTS_DOCS = [
    'doc-2.1',
    'doc-4.1'
    ]
MAX_ELEMENTS_COVERAGE = 'max-coverage'
TRAIN_FOLD_MAX_COVERAGE_DOCS = [
    'doc-5.4',
    'doc-1.4'
    ]

TRAIN_DOCS_PET_EXPERIMENTS = [
    'doc-8.1',
    'doc-10.13',
    'doc-2.1',
    'doc-4.1',
    'doc-5.4',
    'doc-1.4'
    ]


# Color Semantics

CORRECT_ACTIVITY = 'FF3CFF00'  # green background color used in excel

NON_RELAXABLE = 'NON_RELAXABLE'
#
NOT_AN_ACTIVITY = 'Not an Activity'
ADDED_CONDITION = 'Added a condition'
WRONG_ACTIVITY_DATA = 'Wrong Activity Data'
MISSING_ACTIVITY_DATA = 'Missing Activity Data'
WRONG_RECIPIENT = 'Wrong Recipient'
WRONG_PERFORMER = 'Wrong Performer'
WRONG_COMPOUND = 'Wrong Compound'
#
NON_RELAXABLE_ERRORS = [NOT_AN_ACTIVITY,
                        ADDED_CONDITION,
                        WRONG_ACTIVITY_DATA,
                        MISSING_ACTIVITY_DATA,
                        WRONG_RECIPIENT,
                        WRONG_PERFORMER,
                        WRONG_COMPOUND]

RELAXABLE = 'RELAXABLE'
#
ADDED_RECIPIENT = 'Added Recipient'
ADDED_PERFORMER = 'Added Performer'
ADDED_FS = 'Added Further Specification'
MISSING_PART_OF_AD = 'Missing part of the Activity Data'
ADDED_NO_AD_PART = 'Added a not annotated part'
REWORDING = 'Rewording'
#
RELAXABLE_ERRORS = [ADDED_RECIPIENT,
                    ADDED_PERFORMER,
                    ADDED_FS,
                    MISSING_PART_OF_AD,
                    ADDED_NO_AD_PART,
                    REWORDING]

TYPE = 'type'
LABEL = 'label'

#  error types T3
ERROR_TYPE_NOT_AN_ACTOR_PERFORMER = 'not an actor performer'
ERROR_TYPE_ANAPHORA = 'anaph'
ERROR_TYPE_ADD_INFO = '+INFO'
ERROR_TYPE_SUB_INFO = '-INFO'
ERROR_TYPE_REWORDING = 'rewording'

ERROR_TYPE_ACTOR_ROLE_SPECIFICATION = 'actor role specification' # IF A GENERICAL ACTOR IS REFERRED TO WITH A SPECIFIC ROLE, E.G., A SYSTEM REPRESENTED AS A GENERICAL ACTOR IS REFERRED TO AS A SPECIFIC ACTOR, E.G., A SYSTEM ADMINISTRATOR INSTEAD OF THE SYSTEM TEAM
ERROR_TYPE_ACTOR_ROLE_UNDERSPECIFIED = 'actor role underspecified' # IF A SPECIFIC ACTOR IS REFERRED TO WITH A GENERICAL ROLE, E.G., A SYSTEM ADMINISTRATOR IS REFERRED TO AS A SYSTEM INSTEAD OF A SYSTEM ADMINISTRATOR
T3_ERROR_TYPES = [ERROR_TYPE_ANAPHORA,
                  ERROR_TYPE_ADD_INFO,
                  ERROR_TYPE_SUB_INFO,
                  ERROR_TYPE_REWORDING]

T2_ERROR_TYPES = [ERROR_TYPE_NOT_AN_ACTOR_PERFORMER,
                  ERROR_TYPE_ANAPHORA,
                  ERROR_TYPE_ADD_INFO,
                  ERROR_TYPE_SUB_INFO,
                  ERROR_TYPE_REWORDING,
                  ERROR_TYPE_ACTOR_ROLE_SPECIFICATION,
ERROR_TYPE_ACTOR_ROLE_UNDERSPECIFIED
                  ]

# ERROR_TYPES = list().extend(NON_RELAXABLE_ERRORS).extend(RELAXABLE_ERRORS)
#####
## EDOC
#####
            # EDOC_TEST = 'EDOC TEST'
            # TRAIN_FOLD_EDOC_TEST = [
            #         'doc-2.2',
            #         'doc-10.9'
            # ]
            # TEST_FOLD_EDOC_TEST = [
            #         'doc-1.2',
            #         'doc-1.3',
            #         'doc-3.3',
            #         'doc-5.2',
            #         'doc-10.1',
            #         'doc-10.6',
            #         'doc-10.13'
            # ]

# tasks
T1 = 'T1- extract activities'
T2 = 'T2- extract actors'
T3 = 'T3- performs relations'
T4 = 'T4- dfg relations'

##################################
EX_EXPERIMENTAL_SETTING = 'ex(tracted)'
GS_EXPERIMENTAL_SETTING = 'G(old) S(tandard)'

EXPERIMENTAL_SETTINGS = [
        EX_EXPERIMENTAL_SETTING,
        GS_EXPERIMENTAL_SETTING
]
GOLDSTANDARD='GOLDSTANDARD'
#  Experiments PromptNames
T1_RAW = 'T1-Raw'
T1_RAW_CONTEXT = 'T1-RawContext'
T1_SHOTS = 'T1-Shots'
T1_SHOTS_CONTEXT = 'T1-ShotsContext'

#  NEW EXPERIMENTS
T2_RAW = 'RAW'
T2_RAW_CONTEXT = 'RAWCONTEXT'
T2_SHOTS = 'SHOTS'
T2_SHOTS_CONTEXT = 'SHOTSCONTEXT'

T3_RAW = 'T3-Raw'
T3_RAW_CONTEXT = 'T3-RawContext'
T3_SHOTS = 'T3-Shots'
T3_SHOTS_CONTEXT = 'T3-ShotsContext'

T4_RAW = 'T4-Raw'
T4_RAW_CONTEXT = 'T4-RawContext'
T4_SHOTS = 'T4-Shots'
T4_SHOTS_CONTEXT = 'T4-ShotsContext'

# experiments
#  Raw Setting
T1_EXPERIMENTS_RAW = [
        T1_RAW,
        T1_RAW_CONTEXT
]

T2_EXPERIMENTS_RAW = [
        T2_RAW,
        T2_RAW_CONTEXT
]

T3_EXPERIMENTS_RAW = [
        T3_RAW,
        T3_RAW_CONTEXT
]

T4_EXPERIMENTS_RAW = [
        T4_RAW,
        T4_RAW_CONTEXT
]

# complete set of experiments
T1_EXPERIMENTS_SHOTS = [
        T1_SHOTS,
        T1_SHOTS_CONTEXT
]

T2_EXPERIMENTS_SHOTS = [
        T2_SHOTS,
        T2_SHOTS_CONTEXT
]

T3_EXPERIMENTS_SHOTS = [
        T3_SHOTS,
        T3_SHOTS_CONTEXT
]

T4_EXPERIMENTS_SHOTS = [
        T4_SHOTS,
        T4_SHOTS_CONTEXT
]

# complete set of experiments
T1_EXPERIMENTS = [
        T1_RAW,
        T1_RAW_CONTEXT,
        T1_SHOTS,
        T1_SHOTS_CONTEXT
]

T2_EXPERIMENTS = [
        T2_RAW,
        T2_RAW_CONTEXT,
        T2_SHOTS,
        T2_SHOTS_CONTEXT
]

T3_EXPERIMENTS = [
        T3_RAW,
        T3_RAW_CONTEXT,
        T3_SHOTS,
        T3_SHOTS_CONTEXT
]

T4_EXPERIMENTS = [
        T4_RAW,
        T4_RAW_CONTEXT,
        T4_SHOTS,
        T4_SHOTS_CONTEXT
]

# filenames
# T1_RESULTS_FILENAME = 'T1-Results-raw.json.json'

T1_RESULTS_RAW = 'T1-Results-Raw.json'
T1_RESULTS_RAW_cleanned = 'T1-Results-Raw-cleanned.json'
T1_EXCEL_RESULTS_RAW_cleanned = 'T1-Raw.xlsx'

T1_RESULTS_MIN = 'T1-Results-Min.json'
T1_RESULTS_MIN_cleanned = 'T1-Results-Min-cleanned.json'
T1_EXCEL_RESULTS_MIN_cleanned = 'T1-Shots-Min.xlsx'

T1_RESULTS_MAX = 'T1-Results-Max.json'
T1_RESULTS_MAX_cleanned_FILENAME = 'T1-Results-Max-cleanned.json'
T1_EXCEL_RESULTS_MAX_cleanned = 'T1-Shots-Max.xlsx'

T1_RESULTS_COV = 'T1-Results-COV.json'
T1_RESULTS_COV_cleanned = 'T1-Results-COV-cleanned.json'
T1_EXCEL_RESULTS_COV_cleanned = 'T1-Shots-Cov.xlsx'


# T2_RESULTS_FILENAME = 'T2-Results.json'

# T3_RESULTS_FILENAME = 'T3/T3-Results.json'
T2_RESULTS_FILENAME_RAW = 'T2-Results-Raw.json'
T2_RESULTS_FILENAME_RAW_cleanned = 'T2-Results-raw-cleanned.json'
T2_EXCEL_RESULTS_RAW = 'T2-Raw.xlsx'

T2_RESULTS_TRAIN_MIN_ELE_FILENAME = 'T2-Results-MIN-ELEMENTS.json'
T2_RESULTS_TRAIN_MIN_ELE_cleanned = 'T2-Results-MIN-ELEMENTS-cleanned.json'
T2_EXCEL_RESULTS_MIN = 'T2-Shot-MIN.xlsx'

T2_RESULTS_TRAIN_MAX_ELE_FILENAME = 'T2-Results-MAX-ELEMENTS.json'
T2_RESULTS_TRAIN_MAX_ELE_cleanned = 'T2-Results-MAX-ELEMENTS-cleanned.json'
T2_EXCEL_RESULTS_MAX = 'T2-Shot-MAX.xlsx'

T2_RESULTS_TRAIN_COV_ELE_FILENAME = 'T2-Results-MAX-COV-ELEMENTS.json'
T2_RESULTS_TRAIN_COV_ELE_cleanned = 'T2-Results-MAX-COV-ELEMENTS-cleanned.json'
T2_EXCEL_RESULTS_COV = 'T2-Shot-COV.xlsx'


# T3_RESULTS_FILENAME = 'T3/T3-Results.json'
T3_RESULTS_FILENAME_RAW = 'T3-Results-raw.json'
T3_RESULTS_FILENAME_RAW_cleanned = 'T3-Results-raw-cleanned.json'
T3_EXCEL_RESULTS_FILENAME_RAW_cleanned = 'T3-Raw.xlsx'
T3_EXCEL_RESULTS_FILENAME_RAW_cleanned_GS = 'T3-Raw-GS.xlsx'

T3_RESULTS_TRAIN_MIN_ELE_FILENAME = 'T3-Results-MIN-ELEMENTS.json'
T3_RESULTS_TRAIN_MIN_ELE_cleanned_FILENAME = 'T3-Results-MIN-ELEMENTS-cleanned.json'
T3_EXCEL_RESULTS_TRAIN_MIN_ELE_cleanned_FILENAME = 'T3-Shot-MIN-ELEMENTS.xlsx'
T3_EXCEL_RESULTS_TRAIN_MIN_ELE_cleanned_GS = 'T3-Shot-MIN-ELEMENTS-GS.xlsx'

T3_RESULTS_TRAIN_MAX_ELE_FILENAME = 'T3-Results-MAX-ELEMENTS.json'
T3_RESULTS_TRAIN_MAX_ELE_cleanned_FILENAME = 'T3-Results-MAX-ELEMENTS-cleanned.json'
T3_EXCEL_RESULTS_TRAIN_MAX_ELE_cleanned_FILENAME = 'T3-Shot-MAX-ELEMENTS.xlsx'
T3_EXCEL_RESULTS_TRAIN_MAX_ELE_cleanned_GS = 'T3-Shot-MAX-ELEMENTS-GS.xlsx'

T3_RESULTS_TRAIN_COV_ELE_FILENAME = 'T3-Results-MAX-COV-ELEMENTS.json'
T3_RESULTS_TRAIN_COV_ELE_cleanned_FILENAME = 'T3-Results-MAX-COV-ELEMENTS-cleanned.json'
T3_EXCEL_RESULTS_TRAIN_COV_ELE_cleanned_FILENAME = 'T3-Shot-MAX-COV-ELEMENTS.xlsx'
T3_EXCEL_RESULTS_TRAIN_COV_ELE_cleanned_GS = 'T3-Shot-MAX-COV-ELEMENTS-GS.xlsx'

T4_RESULTS_FILENAME_RAW = 'T4-Results-raw.json'
T4_RESULTS_FILENAME_RAW_cleanned = 'T4-Results-raw-cleanned.json'
T4_EXCEL_RESULTS_RAW_EX = 'T4-Raw-EX.xlsx'
T4_EXCEL_RESULTS_RAW_GS = 'T4-Raw-GS.xlsx'


T4_RESULTS_TRAIN_MIN_ELE_FILENAME = 'T4-Results-MIN-ELEMENTS.json'
T4_RESULTS_TRAIN_MIN_ELE_cleanned_FILENAME = 'T4-Results-MIN-ELEMENTS-cleanned.json'
T4_EXCEL_RESULTS_MIN_EX = 'T4-Shot-MIN-ELEMENTS-EX.xlsx'
T4_EXCEL_RESULTS_MIN_GS = 'T4-Shot-MIN-ELEMENTS-GS.xlsx'

T4_RESULTS_TRAIN_MAX_ELE_FILENAME = 'T4-Results-MAX-ELEMENTS.json'
T4_RESULTS_TRAIN_MAX_ELE_cleanned_FILENAME = 'T4-Results-MAX-ELEMENTS-cleanned.json'
T4_EXCEL_RESULTS_TRAIN_MAX_ELE_cleanned_FILENAME = 'T4-Shot-MAX-ELEMENTS.xlsx'
T4_EXCEL_RESULTS_MAX_EX = 'T4-Shot-MAX-ELEMENTS-EX.xlsx'
T4_EXCEL_RESULTS_MAX_GS = 'T4-Shot-MAX-ELEMENTS-GS.xlsx'

T4_RESULTS_TRAIN_COV_ELE_FILENAME = 'T4-Results-MAX-COV-ELEMENTS.json'
T4_RESULTS_TRAIN_COV_ELE_cleanned_FILENAME = 'T4-Results-MAX-COV-ELEMENTS-cleanned.json'
T4_EXCEL_RESULTS_TRAIN_COV_ELE_cleanned_FILENAME = 'T4-Shot-MAX-COV-ELEMENTS.xlsx'
T4_EXCEL_RESULTS_COV_EX = 'T4-Shot-COV-ELEMENTS-EX.xlsx'
T4_EXCEL_RESULTS_COV_GS = 'T4-Shot-COV-ELEMENTS-GS.xlsx'





# RESULTS_FILENAME = 'NewMet-2.json'

TASKS = [
        T1,
        T2,
        T3,
        T4
]

T1_EMPTY_RESULT_ITEM = {experiment: deepcopy(_SINGLE_ANSWER) for experiment in T1_EXPERIMENTS}
T2_EMPTY_RESULT_ITEM = {experiment: deepcopy(_SINGLE_ANSWER) for experiment in T2_EXPERIMENTS}
T3_EMPTY_RESULT_ITEM = {
        experimental_setting: {
                experiment: deepcopy(_SINGLE_ANSWER)
                for experiment in T3_EXPERIMENTS}
        for experimental_setting in EXPERIMENTAL_SETTINGS
}
T4_EMPTY_RESULT_ITEM = {experimental_setting: {
                experiment: deepcopy(_SINGLE_ANSWER)
                for experiment in T4_EXPERIMENTS}
        for experimental_setting in EXPERIMENTAL_SETTINGS}

__EMPTY_RESULT_ITEM = {
        PROCESS_DESCRIPTION: '',
        # for T1
        GOLD_ACTIVITY_LIST:  list(),
        # ACTIVITY_LIST:       list(),
        # for T2
        GOLD_ACTOR_LIST:     list(),
        # ACTOR_LIST:          list(),
        # for T3
        GOLD_PERFORMS_LIST:  list(),
        # PERFORMS_LIST:       list(),
        # for T4
        GOLD_DFG_LIST:       list(),
        # DFG_LIST:            list(),
        # answers from GPT-3
        RAW_ANSWERS:         {
                T1: deepcopy(T1_EMPTY_RESULT_ITEM),
                T2: deepcopy(T2_EMPTY_RESULT_ITEM),
                T3: deepcopy(T3_EMPTY_RESULT_ITEM),
                T4: deepcopy(T4_EMPTY_RESULT_ITEM)
        }
}


def getEmptyResultsItem():
    return deepcopy(__EMPTY_RESULT_ITEM)



TP = 'TP'
FP = 'FP'
FN = 'FN'
PRECISION = 'Precision'
RECALL = 'Recall'
F1 = 'F1 score'

