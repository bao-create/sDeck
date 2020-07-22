import sys
from k_reader import k_read
from bdf_reader import bdf_read


bdf_words = ["GRID","CQUAD4","CQUAD8","CTETRA","CHEXA"]
k_words = ["*NODE","*ELEMENT"]







file_name = sys.argv

if file_name.find(".bdf") > -1:
    bdf_read(file_name,bdf_words)
else:
    k_read(file_name,k_words)

