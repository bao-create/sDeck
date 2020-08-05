def writedeck(model,filename):
    if model.typef: #if model started as lsdyna file write as bdf
        with open(filename,'w') as f:
            f.write("CEND")
            f.write("$BDF DECK PREPARED BY SDECK")
            f.write("BEGIN BULK")
            for key,value in model.node:
                line = "GRID"+ "    "+ key+"    " + value.xyz[0]+"    " + value.xyz[1]+"    " + value.xyz[2]
                f.write(line)
            for key,value in model.eles[0].ELE_SOLID:
                if len(value.nodes) == 4:
                    line = "CTETRA" + "    "+ key +"    "+ value.nodes[0] +"    " + value.nodes[1]+"    " + value.nodes[2] +"    "+ value.nodes[3]
                elif len(value.nodes) == 8:
                    line = "CHEXA" + "    "+ key +"    "+ value.nodes[0] +"    " + value.nodes[1]+"    " + value.nodes[2] +"    "+ value.nodes[3] +"    "+ value.nodes[4] +"    "+ value.nodes[5]+"    "+ value.nodes[6]+"    "+ value.nodes[7]
                f.write(line)
            for key,value in model.eles[0].ELE_SHELL:
                if len(value.nodes) == 4:
                    line = "CQUAD4" + "    "+ key +"    "+ value.nodes[0] +"    " + value.nodes[1]+"    " + value.nodes[2] +"    "+ value.nodes[3]
                elif len(value.nodes) == 8:
                    line = "CQUAD8" + "    "+ key +"    "+ value.nodes[0] +"    " + value.nodes[1]+"    " + value.nodes[2] +"    "+ value.nodes[3] +"    "+ value.nodes[4] +"    "+ value.nodes[5]+"    "+ value.nodes[6]+"    "+ value.nodes[7]

            f.write("ENDDATA")
    else:
        pass
        #write dyna
    return