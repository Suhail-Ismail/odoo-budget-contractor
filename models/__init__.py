# -*- coding: utf-8 -*-

# INHERITANCE MODELS
# ----------------------------------------------------------

# BASIC MODELS
# ----------------------------------------------------------
from . import res_partner, contractor, contractor_contact, contract, \
    milestone, component, rfs, sicet, system_type, rfq, volume_discount

# MODELS INHERITANCE BELOW COMES LAST BECAUSE THEY ARE INHERITING MODELS FROM THE SAME MODULE
# INHERITANCE MODELS
from . import milestone_inherit_actual, rfs_inherit_actual

