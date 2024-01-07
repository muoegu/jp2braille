<!-- Please install VScode extension called "Markdown Mind Map Preview" (https://marketplace.visualstudio.com/items?itemName=josephcz.vscode-markdown-mindmap-preview) -->


# Japanese Braille Translator with LLM

## Concept

### Braille translation
- Natural language -> braille

### Japanese mixed with Kanji and Hiragana
- Convert all in Hiragana(reading)
	- Convert to Braille(1 on 1)

## Motivation

### problem
- Kanji often has multiple reading
	- On-reading
		- From Chinese
	- Kun-reading
		- Japan
- braille
	- Needs to kanji->yomi conversion
	- Volunteer
		- Sapie Library
		- Time-consuming
	- translation
	- App 
		- expensive
		- Not accurate

### How to improve
- Fast, accurate, cheep
- Another application
	- Language Learners
	- Voice over

## Difficulties?

### On-kun

## Research

### Kanji->Yomi
- machine learning
	- That's surely more accurate
	- Requires extensive training data

### Value
- LLM’s possibility 
	- 

### braille

## Braille translation

### Mecab
- Morphological analysis tool
	- like spaCy 
- Can get Yomi info
	- Phonological reading
	- は（ha, wa）へ（he, e）

### [点字自動翻訳 on the web](http://muzik.gr.jp/tenji/conv_tenji.asp)


### chatGPT
- GPT3.5
- GPT4

### liblouis
- Rule base

### Paid apps or services

## My project

### Mecab result as base

### dictionary

### Let LLM decide

## Pipeline

### Preprocessing
- Get input
	- Input by one sentence
		- Too much prompt
	- Future: use of multiple sentences
- Morphological analysis
	- Mecab
		- get basic Yomi
			- how accurate?
		- get 
			- phonetic
				- Phonological change
			- POS
				-  later?
	- tokenization
		- Split into chunks
			- Easy to analyze
- Check if its contains Kanji
	- input
		- Morphological analysed data
	- No need to search all reading
		- All hiragana
			- pass
			- は、へ
				- Mecab can handle
			- Supposed to use kanji but Hira???
		- Contains kanji
- Filter ambiguous kanji
	- input
		- Contain kanji chunk
	- single entry reading 
		- use that reading
	- multiple reading  even though has single entry
		- How to distinguish????
			- kinou or sakujitu(yesterday)
			- kyou(today) or konichi(recently)
				- entry

### Prompt engineering??
- Get dictionary entries 
	- input
		- Only ambiguous chunks
	- Josh API
		- Scrape JP dictionary 
			- In English
				- Language consistency 
				- Just yomi written in hiragana
				- Ref?
		- No official
			- Ex; 萌典
	- data
		- entries
		- pos?
		- readings
		- Example sentences?
- Prompt Design
	- input
		- Original text
		- ambiguous chunks
		- Dictionary info
	- open AI API
		- prompting
			- design
				- data
					- Input text
					- Ambiguous kanji
				- How to read considering the context of text iself
					- Hoe to let them consider context
						- Give context?
			- Just let them convert
				- Not accurate
			- Just let them convert ambiguous  one 
			- Can’t give many prompt
				- Need to 
					- Contains lots of info
					- But simple, smaller tokens
	- Output purser
		- Let them only output list
			- Use this list afterword
		- Didn’t work well
		- Out put
			- Readings of Ambiguous chunks(list)

### Implementation
- Update kana data for input data
	- input
		- Readings of Ambiguous chunks(list)
	- Get LLM result
		- Decide reading
	- Add word order number 
	- Update dictionaly
- Create braille dictionary
	- originally CSV
		- Add 1 to 1? data
	- data
		- hiragana
		- katakana
		- Alphabet
		- Braille
		- unicode
		- Represent number
- Convert to Braille 
	- Mapping dictionaly
- Display conversion result

## Result

### Evaluation
- Create dataset 
	- Yomi answer
	- Translator result
	- [difflib](https://docs.python.org/3/library/difflib.html)
	- Ambiguous reading pair
		- Too short?
		- Long ver
			- Not good….
- score
	- Per level
	- Just check the key
	- Find whether it contains key or not
- pipeline
	- Preprocessing
		- Add Kana_answer
	- streamlit
		- Input CSV
		- CSV to Pandas Dataframe
			- test_texts
				- Change name
				- Text data
			- target_words
				- Change name

### Comparison
- Mecab
	- Quite good score
	- same answer in the pair
	- 
- GPT3.5
	- incorrect
		- hallucination
		- Kana + Hira mix
		- Just output a word
- GPT4
	- Better than GPT3.5
	- hallucination
- Yomi -GPT
	- better?

## Limitation

### The more inputs there are
- the more expensive
- the more time

### Spacing
- Accuracy↓

### Another models

# Final presentation

## project overview

## motivation

### What kind of problem?

## explain basic rules

### 

## reserch  method

## pipline

## result

### 

## demo

### Just convert to hiragana part

### Streamlit deploy

## Demo app

### streamlit

### pagenation
- main
	- translation
- converter plus
	- Especially for conversion
- test
	- Perform test
		- mecab
		- chatGPT
		- 
	- comparison
