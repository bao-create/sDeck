from item_class import chexa, cquad4, ctetra4, eleObject, node
from deck_class import deck


def bdf_read(file,words):
    model = deck(False)
    current_element_object = eleObject()
    with open(file) as f:
        line = f.readline()
        while line: #for each line
            if line.find("$") == -1: # is the line a comment
                continue
            else:
                if line.find("+") != -1:
                    cont_flag =True
                for i in range(len(words)): #if its not a comment check each line for one of the words
                    if line.find(words[i]) == -1:
                        continue #continue if it cant find it
                    else:
                        item_type = i #assign this the index of the word
                        if cont_flag:
                            first_line = line # get both lines
                            line = f.readline() # im assuming for now this grabs the next line
                            first_line = first_line.replace("+","")
                            line = line.replace("+"," ")
                            line_to_pass = line + first_line
                        break #end the loop cause there is only one word per line
                
            if item_type == 0:
                currentNode = node(line_to_pass)
                model.appendNode(currentNode)
            elif item_type == 1:
                currentEle = cquad4(line_to_pass)
                current_element_object.addcquad4Ele(currentEle)
            elif item_type == 2:
                currentEle = cquad8(line_to_pass)
                current_element_object.addcquad8Ele(currentEle)
            elif item_type == 3:
                currentEle = ctetra4(line_to_pass)
                current_element_object.addctetra4Ele(currentEle)

            elif item_type == 4:
                currentEle = chexa(line_to_pass)
                current_element_object.addchexaEle(currentEle)
            
                
            else:
                pass
            line = f.readline() #assign the iterator a new line for next round of loop
    model.setEleList(current_element_object)
