# import pandas as pd
#
# file =  pd.read_csv("squirel.csv")
# colour_of_squirell = (file["Primary Fur Color"].to_list())
#
# clr_sumary = {
#     "colour" : [],
#     "count" : []
#
# }
# for colour in colour_of_squirell:
#     if colour == "nan":
#         pass
#     elif colour not in clr_sumary["colour"]:
#         clr_sumary["colour"].append(colour)
#     elif colour in clr_sumary:
#         for colours in colour:
#
#     else:
#         pass
#
# print(clr_sumary)

import pandas as pd
from numpy.ma.core import count

file = pd.read_csv("squirel.csv")

red_squi = len(file[file["Primary Fur Color"] == "Cinnamon"])
gry_squi = len(file[file["Primary Fur Color"] == "Gray"])
blk_squi = len(file[file["Primary Fur Color"] == "Black"])
print(red_squi)
print(gry_squi)
print(blk_squi)

data_dict ={
    "clr_squirel" : ["red", "gry_squi", "blk_squi"],
    "count_squirel ": [red_squi, gry_squi, blk_squi],

}

pd.DataFrame(data_dict).to_csv("squireler.csv")
