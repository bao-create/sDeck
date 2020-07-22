from item_class import eleObject, node, ELE_SHELL, ELE_SOLID
from deck_class import deck

def k_read(file,words):
    model = deck(True)
    current_element_object = eleObject()
    with open(file) as f:
        line = f.readline()
        bulk_def = False #dyna does not declare the item type on each line, they declare the type then pass arbitrary sized bulk data
        sup = False
        while line:
            if line.find("$") == -1: # is the line a comment
                continue
            else:
                cnt = 0
                if line.find("*") == -1: #we are in bulk def if the line isnt a comment and doesnt have a *
                    bulk_def = True
                else: #if we arent in bulk def see if it is a supported keyword
                    bulk_def = False
                    for i in range(len(words)): #if its not a comment check the line for one of the supported keywords
                        if line.find(words[i]) == -1:
                            cnt += 1
                            continue #continue if it cant find it
                        else: #if it finds a keyword assign the item_type to that key
                            item_type = i
                            bulk_def = False #make this false so it wont try to make an item object from it
                            break #one word per line
                        
                    if cnt == len(words): #if we have tried all supported words and failed
                        sup = False
                    else:
                        sup = True

                if bulk_def  and sup: # if its a supported bulk def entry create the items as needed
                    if item_type == 0:
                        currentNode = node(line)
                        model.appendNode(currentNode)
                    elif item_type == 1:
                        currentEle = ELE_SOLID(line)
                        current_element_object.addELE_SOLID(currentEle)
                    elif item_type == 2:
                        currentEle = ELE_SHELL(line)
                        current_element_object.addELE_SHELL(currentEle)
                    else:
                        pass
                else:
                    pass



                
            line = f.readline()
    model.setEleList(current_element_object)
    return model