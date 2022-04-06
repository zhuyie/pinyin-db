#!/usr/bin/env python3

from collections import Counter
import grapheme

total_pinyins = 0
total_chars = 0
char_usedtimes = Counter()

def analyze(filename):
	global total_pinyins
	global total_chars
	global char_usedtimes

	in_file = open(filename, 'r')
	for line in in_file:
		line = line[:-1]

		try:
			char, code, pinyins = line.split('\t')
			pinyin_list = pinyins.split(',')
		except ValueError as _:
			continue

		for pinyin in pinyin_list:
			total_pinyins += 1
			for char in grapheme.graphemes(pinyin):
				char_usedtimes[char] += 1
				total_chars += 1
			
	in_file.close()

def output():
	print('total_pinyins = %d' % (total_pinyins))
	print('total_chars   = %d' % (total_chars))
	print('unique_chars  = %d' % (len(char_usedtimes)))
	print('')
	for char in sorted(char_usedtimes.keys()):
		print('%-5d\t%s\t%s' %(char_usedtimes[char], char, ascii(char)))

def main():
	analyze('data/Mandarin.txt')
	analyze('data/HanyuPinyin.txt')
	analyze('data/TGHZ2013.txt')
	analyze('data/XHC1983.txt')
	output()

if __name__ == '__main__':
	main()
