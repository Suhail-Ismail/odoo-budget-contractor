# -*- coding: utf-8 -*-

# INHERITANCE MODELS
# ----------------------------------------------------------
# from . import section_inherit

# BASIC MODELS
# ----------------------------------------------------------
from . import res_partner, contractor, contractor_contact, contract, \
    milestone, component, rfs, sicet, system_type

# MODELS INHERITANCE BELOW COMES LAST BECAUSE THEY ARE INHERITING MODELS FROM THE SAME MODULE
# INHERITANCE MODELS
from . import milestone_inherit_actual, rfs_inherit_actual

