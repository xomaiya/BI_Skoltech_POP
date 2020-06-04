from modeller import *
from modeller.automodel import *

env = environ()

lm = loopmodel(
    env,
    sequence='CLTR2',
    alnfile='CLTR2_6rz8.ali',
    knowns='6rz8',
    # inimodel='automodel.final.pdb',
    assess_methods=(assess.DOPE, assess.GA341),
    loop_assess_methods=(assess.DOPE)
)

lm.starting_model = 1
lm.ending_model = 9
lm.make()
lm.write_final_model('loopmodel.final.pdb', None, None)
