# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:27:35 2024

@author: hityingph
"""

import dpdata
from ase.io import write
from tqdm import tqdm


dp_train = dpdata.MultiSystems().load_systems_from_file("train", fmt="deepmd/npy")

nep_train = []
for d in tqdm(dp_train):
    structure = d.to_ase_structure()
    nep_train.extend(structure[::100])
    
write("train.xyz", nep_train, format="extxyz")



dp_validate = dpdata.MultiSystems().load_systems_from_file("validate", fmt="deepmd/npy")

nep_validate = []
for d in tqdm(dp_validate):
    structure = d.to_ase_structure()
    nep_validate.extend(structure[::10])
    
write("validate.xyz", nep_validate, format="extxyz")



dp_test = dpdata.MultiSystems().load_systems_from_file("test", fmt="deepmd/npy")

nep_test = []
for d in tqdm(dp_test):
    structure = d.to_ase_structure()
    nep_test.extend(structure[::10])
    
write("test.xyz", nep_test, format="extxyz")