# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:52:48 2019

@author: eduar
"""

import shutil
import os

#source = "C:/Users/eduar/Documents/bongioloes.github.io/_site/"
#dest = "C:/Users/eduar/Documents/bongioloes.github.io/"

#files = os.listdir(source)
#files.remove("files")
#files.remove("images")
#files.remove("pos_html_arrangaments.py")

#for f in files:
#        shutil.move(source+f, dest)

#shutil.rmtree("C:/Users/eduar/Documents/bongioloes.github.io/_site/")

### Index page
index = open("index.html", encoding = "Latin-1",).read().replace('class="fa fa-researchgate','class="fab fa-researchgate')

with open('index.html',encoding = "Latin-1", mode = "w") as text_index:
    text_index.write(index)
    text_index.close()
    
### Academic page
academic = open("academic.html", encoding = "Latin-1",).read().replace('class="fa fa-researchgate','class="fab fa-researchgate')

with open('academic.html',encoding = "Latin-1", mode = "w") as text_academic:
    text_academic.write(academic)
    text_academic.close()

### Skill page
skill = open("skill.html", encoding = "Latin-1",).read().replace('class="fa fa-researchgate','class="fab fa-researchgate')

with open('skill.html',encoding = "Latin-1", mode = "w") as text_skill:
    text_skill.write(skill)
    text_skill.close()

### Projects page
projects = open("projects.html", encoding = "Latin-1",).read().replace('class="fa fa-researchgate','class="fab fa-researchgate')

with open('projects.html',encoding = "Latin-1", mode = "w") as text_projects:
    text_projects.write(projects)
    text_projects.close()

### Pictures page
pictures = open("pictures.html", encoding = "Latin-1",).read().replace('class="fa fa-researchgate','class="fab fa-researchgate')

with open('pictures.html',encoding = "Latin-1", mode = "w") as text_pictures:
    text_pictures.write(pictures)
    text_pictures.close()
