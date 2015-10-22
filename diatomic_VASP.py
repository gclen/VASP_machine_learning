#!/usr/bin/python

import os
import subprocess

def write_VASP_files(atom1, atom2):
    
    #Make the directory if it does not exist
    if not os.path.exists(atom1+atom2):
        os.makedirs(atom1+atom2)
    #Go into the directory 
    os.chdir(atom1+atom2)
    #Copy the necessary potcar files
    subprocess.call(['cp ../POTENTIALS/potpaw_PBE/%s/POTCAR ./%s_POTCAR' % (atom1, atom1)]
                     , shell=True)
    subprocess.call(['cp ../POTENTIALS/potpaw_PBE/%s/POTCAR ./%s_POTCAR' % (atom2, atom2)]
                     , shell=True)                       
    #Cat them together
    if atom1 == atom2:
        subprocess.call(['mv %s_POTCAR POTCAR' % (atom1)], shell=True)
    else:
        subprocess.call(['cat %s_POTCAR %s_POTCAR > POTCAR' % (atom1, atom2)], shell=True)
        #Remove individual POTCARS
        subprocess.call(['rm %s_POTCAR %s_POTCAR' % (atom1, atom2)], shell=True)

    #Copy INCAR and KPOINTS file 
    subprocess.call('cp ../INCAR_TEMPLATE ./INCAR; cp ../KPOINTS_TEMPLATE ./KPOINTS', shell=True)

    #Write the POSCAR file
    write_POSCAR(atom1, atom2)

    os.chdir('../')

def write_POSCAR(atom1, atom2):

    #Open up the POSCAR file for writing
    POSCAR_file=open('POSCAR','w')
    #Write the atom names
    POSCAR_file.write(atom1+atom2+'\n')
    #Write the scaling number 
    POSCAR_file.write('    1.00000000000000 \n')
    #Write the supercell vectors
    POSCAR_file.write('    10.0   0.00000    0.00000 \n')
    POSCAR_file.write('    0.00000   10.0    0.00000 \n')
    POSCAR_file.write('    0.00000   0.00000    10.0 \n')
    #Write the number of each atom type
    if atom1 == atom2:
        POSCAR_file.write('2 \n')
    else: 
        POSCAR_file.write('1 1 \n')
    #Write the type of the coordinates (Cartesian or direct)
    POSCAR_file.write('Cartesian \n')
    #Write the coordinates
    POSCAR_file.write(' 0.0 0.0 0.0 \n')
    POSCAR_file.write(' 0.0 0.0 2.0 \n')

    POSCAR_file.close()

def main():
    
    #List of all the atoms
    atom_list = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'] 

    for idx, atom1 in enumerate(atom_list[:2]):
        for atom2 in atom_list[idx:2]:
            write_VASP_files(atom1, atom2)
        
if __name__=="__main__":
    main()


