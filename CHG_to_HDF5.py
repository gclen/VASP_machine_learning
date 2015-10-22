#!/usr/bin/python

import numpy as np
import os
import h5py

def read_CHG_file():

    header_info = parse_CHG_header()
    #Need to skip 10 lines + number of atoms
    skip_num = header_info[0] + 10
    #Get number of points in each direction
    num_x = header_info[1][0]
    num_y = header_info[1][1]
    num_z = header_info[1][2]

    #Read in the data from the CHG file
    chg_data_raw = np.loadtxt(fname='CHG', skiprows=skip_num)
    chg_data = np.reshape(chg_data_raw,(num_x, num_y, num_z))

    return chg_data      

def parse_CHG_header():

    chg_file = open('CHG', 'r')

    #Skip first 6 lines
    for i in range(6):
        chg_file.readline()
    #Sum up the total number of atoms in the system
    atom_tot = sum([int(i) for i in chg_file.readline().split()])
    #Skip
    for i in range(atom_tot+2):
        chg_file.readline()
    #Get the number of points in each direction
    num_points = [int(i) for i in chg_file.readline().split()]
    
    return (atom_tot, num_points)

    chg_file.close()

def write_hdf5(chg_data):

    #Get the name of the file from the current directory
    dir_name = os.path.split(os.getcwd())[-1]

    #Open the hdf5 file
    chg_hdf5 = h5py.File(dir_name+'_CHG.hdf5', 'w')

    #Write the data out in an hdf5 file
    chg_hdf5.create_dataset('charge_density', data=chg_data)

    #Close the file
    chg_hdf5.close()

def main():

    chg_data = read_CHG_file() 
    write_hdf5(chg_data)

if __name__=="__main__":
    main()


