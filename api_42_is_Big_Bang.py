from os.path import dirname, join
import json
import requests as req

current_dir = dirname(__file__)
file_path = join(current_dir, "./dataset_24476_3.txt")
file_path2 = join(current_dir, "./answer.txt")
with open(file_path, "r") as i_f:
    with open(file_path2, "w") as o_f:
        for l in i_f:
            res = r'http://numbersapi.com/' + l[:-1] + r'/math?json=true'
            res = req.get(res)
            res = res.json()
            print(res)
            if res['found'] == False:
                o_f.write('Boring\n')
            else:
                o_f.write('Interesting\n')
