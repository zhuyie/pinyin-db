#!/usr/bin/env python3

db_file = 'Unihan/Unihan_Readings.txt'

def add_pinyin(pinyins, toadds):
	for toadd in toadds:
		if toadd not in pinyins:
			pinyins.append(toadd)

def build_line(hanzi, code, pinyins):
	line = '%c\t%s\t%s\n' % (hanzi, code, ",".join(pinyins))
	return line

def generate(source, filename):
	in_file = open(db_file, 'r')
	out_file = open(filename, 'w')

	entries = 0
	for line in in_file:
		# skip comments
		if line[0] == "#":
			continue

		# get rid of \n character at end of line
		line = line[:-1]
	
		# Eg. 'U+5364	kHanyuPinyin	10093.130:xī,lǔ 74609.020:lǔ,xī'
		try:
			code, field, value = line.split('\t')
		except ValueError as _:
			continue

		if field != source:
			continue

		code = code[2:]
		hanzi = chr(int(code, 16))

		pinyins = []
		if source != 'kMandarin':
			parts = value.split(' ')
			for part in parts:
				locations_and_readings = part.split(':')
				if len(locations_and_readings) != 2:
					continue
				add_pinyin(pinyins, locations_and_readings[1].split(','))
		else:
			add_pinyin(pinyins, value.split(' '))

		out_file.write(build_line(hanzi, code, pinyins))
		
		entries = entries + 1

	in_file.close()
	out_file.close()
	
	print('%s -> %d entries.' % (filename, entries))

def main():
	generate('kMandarin', 'Mandarin.txt')
	generate('kHanyuPinyin', 'HanyuPinyin.txt')
	generate('kTGHZ2013', 'TGHZ2013.txt')
	generate('kXHC1983', 'XHC1983.txt')

if __name__ == '__main__':
	main()
