from modeller import *

env = environ()

aln = alignment(env)
mdl = model(env, file='6rz8_cutted.pdb')
aln.append_model(mdl, align_codes='6rz8', atom_files='6rz8_cutted.pdb')
aln.append(file='CLTR2_cutted.ali', align_codes='CLTR2')
aln.align2d()
aln.write(file='CLTR2_6rz8.ali', alignment_format='PIR')
aln.write(file='CLTR2_6rz8.pap', alignment_format='PAP')
