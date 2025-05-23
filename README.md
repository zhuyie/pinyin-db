# pinyin-db
A simple script that generates a character to pinyin mapping from the [Unihan database](https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip).

## Sources
- Mandarin
  - The most customary pīnyīn reading for this character. When there are two values, then the first is preferred for zh-Hans (CN) and the second is preferred for zh-Hant (TW). When there is only one value, it is appropriate for both.
- HanyuPinyin
  - 《漢語大字典》 Hànyǔ Dà Zìdiǎn (HDZ). This data was originally input by 井作恆 Jǐng Zuòhéng, proofed by 聃媽歌 Dān Māgē (Magda Danish, using software donated by 文林 Wénlín Institute, Inc. and tables prepared by 曲理查 Qū Lǐchá), and proofed again and prepared for the Unicode Consortium by 曲理查 Qū Lǐchá (2008-01-14).
- TGHZ2013
  - 《通用规范汉字字典》(Tōngyòng Guīfàn Hànzì Zìdiǎn = TGHZ; ‘General Purpose Normalized Hanzi Dictionary’). 商务印书馆辞书研究中心编 (Dictionary Research Center of the Commercial Press, eds.). 北京: 商务印书馆, 2013 [2013年7月第1版; 2013年9月北京第3次印刷; 印张 22⅞; ISBN 978-7-100-05961-9]. http://www.cp.com.cn/book/366cddb0-1.html
- XHC1983
  - 《现代汉语词典》 [Xiàndài Hànyǔ Cídiǎn = XHC; ‘Modern Chinese Dictionary’]. 中国社会科学院语言研究所词典编辑室编 [Chinese Academy of Social Sciences, Linguisitics Research Institute, Dictionary Editorial Office, eds.]. 北京: 商务印书馆, 1983 [1978 年 12 月第 1 版; 1983 年 1 月第 2 版; 1984 年 1 月北京第 49 次印刷印张 54; 统一书号: 17017.91].

## File Format
The text files using UTF-8 and Unix line endings.

Each of the lines is one entry, with three, tab-separated fields: the character, the Unicode scalar value, and a comma-separated list of one or more pīnyīn readings. Eg. :
```
三	4E09	sān
上	4E0A	shàng,shǎng
下	4E0B	xià
```
