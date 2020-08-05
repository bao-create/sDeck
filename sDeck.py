import sys
from k_reader import k_read
from bdf_reader import bdf_read
from writedeck import writedeck


bdf_words = ["GRID","CQUAD4","CQUAD8","CTETRA","CHEXA"]
k_words = ["*NODE","*ELEMENT_SOLID","*ELEMENT_SHELL"]







file_name = sys.argv[0]

if file_name.find(".bdf") > -1:
    model = bdf_read(file_name,bdf_words)
    file_name = file_name +".k"
else:
    model = k_read(file_name,k_words)
    fiel_name = file_name +".bdf"

writedeck(model,file_name)