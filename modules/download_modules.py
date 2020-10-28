# -*- coding: utf-8 -*-
import os

with open("../install.txt", "r", encoding="utf-8") as f:
    content = [_.strip() for _ in f.readlines()]

for line in content:
    if line.startswith("Downloading"):
        module_url = line.split()[1]
        print(module_url)
        if module_url.startswith("http"):
            os.system("wget {}".format(module_url))
            print("Download {}".format(module_url.split("/")[-1]))
