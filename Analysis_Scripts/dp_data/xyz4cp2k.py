#!/usr/bin/env python
# coding: utf-8

import os
import shutil
import random


def get_xyz(lines, poscar,idx):
    write_poscar = open(poscar, 'w')
    write_poscar.write(lines[0])
    write_poscar.write("frame index %d\n" %idx)
    for i in range(2,len(lines)):   
        write_poscar.write(lines[i])      
    
    write_poscar.close()


def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 

if __name__ == '__main__':

    xyz_path = "./012"
    xyz = "/data/HOME_BACKUP/pengchao/glycine/deepks/M062X_Dataset/Glycine54H2O_efield/lammpstrj/012_r011"
    xyzfile = os.path.join(xyz,"glycine_1b_real.xyz")
    searchfile = open(xyzfile, "r")
    lines = searchfile.readlines()
    searchfile.close() 
    
    atoms = int(lines[0].split()[0])
    s_index = 0
    s_list = []
    for line in lines:
        s_index += 1
        if 'Title' in line:
            s_list.append(s_index)
    
    j = 1
    #for i in range(801,len(s_list),5):
    for i in range(0,len(s_list),1):
        name = str(10000+j)
        j += 1
        mkpath = os.path.join(xyz_path, name)
        mkdir(mkpath)
        poscar = os.path.join(mkpath, 'POSCAR1.xyz') 
        get_xyz(lines[s_list[i]-2:s_list[i]+atoms], poscar, i)     
