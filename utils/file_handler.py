import  ipdb
import datetime
def file_handler(array):
    treatedArray = []
    for index, item in enumerate(array):
        treatment = {
                "type":array[index][0],
                "date":f"{array[index][1:5]}-{array[index][5:7]}-{array[index][7:9]}",
                "value":array[index][9:19],
                "cpf":array[index][19:30],
                "card":array[index][30:42],
                "hour":datetime.time(int(array[index][42:44]), int(array[index][44:46]), int(array[index][46:48])),
                "owner":array[index][48:62],
                "shop":array[index][62:90],
            }
        treatedArray.append(treatment)
    return treatedArray