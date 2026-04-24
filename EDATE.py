#!/usr/bin/env python3

import sys, os, subprocess
import json, argparse

o_IQHIGH = ["Yao", "yao"]
o_IQLOW = ["Keita", "makias"]

def main(before, after, exclude):
	EXCLUDE = ["EDATE.py"]
	EXCLUDE += exclude
	
	files = os.listdir()
	
	for file in files:
		if file in EXCLUDE: break
	with open(file) as f:
		contents = f.read()
	for i in range(len(before)):
		for j in range(len(before[i])):
			contents = contents.replace(before[i][j], after[i] if type(after[i])==str else after[i][j])
	with open(file, "w") as f:
		f.write(contents)

p = argparse.ArgumentParser("Change the names")

p.add_argument("-a", "--aiq-high", help="The person with high IQ", default=o_IQHIGH)
p.add_argument("-b", "--bum", help="The person with low IQ", default=o_IQLOW)
p.add_argument("-oa", "--oa", help="original a", default=o_IQHIGH)
p.add_argument("-ob", "--ob", help="original b", default=o_IQLOW)
p.add_argument("-x", "--exclude", help="exclude files (csv)", default=[__FILE__], type=lambda x: x.split(","))

args = p.parse_args()

main([args.oa, args.ob], [args.aiq_high, args.bum], args.exclude)

