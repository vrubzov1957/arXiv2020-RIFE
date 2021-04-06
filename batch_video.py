import argparse

parser = argparse.ArgumentParser(description='Interpolation for a pair of images')
parser.add_argument('--list', dest='list', type=str, default=None)

file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    execfile('inference_video.py --fp16 --exp=2 --video='+line) 
 
