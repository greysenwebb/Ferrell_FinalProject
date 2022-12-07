'''
Name: Aaron Paulson, Spiros Yotas, Addyson Stansel, Greysen Webb
email: Paulsoar@mail.uc.edu, Yotassg@mail.uc.edu, Stansean@mail.uc.edu, Webbgp@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: We will collaborate with our team to develop an eclipse application and upload a picture through eclipse
Citations:
Anything else that's relevant: 
'''
import json
from PIL import Image
def decrypt_file():
    with open('encryptedgrouphints.json')as x:
        data=json.load(x)
    reference=(data['Ferrell'])


   
    with open ('english.txt')as y:
        lines=y.readlines()

    for i in range(len(reference)):
        value=int(reference[i])
        print(lines[value], end='')
        
def team_image ( filename ):
    myimage = Image.open(filename)
    myimage.load()
    return myimage
