<!-- Please install VScode extension called "Markdown Mind Map Preview" (https://marketplace.visualstudio.com/items?itemName=josephcz.vscode-markdown-mindmap-preview) -->


# Japanese Braille Translation Machine and LLM

## Concept

### Automatic Braille Translation
- Natural Language -> Braille

### Kanji and Kana Mixed Script
- Convert everything to Hiragana (reading)
	- Then convert to Braille (1-to-1 mapping)

## Japanese Braille

### Rules
- 6-dot system
	- Can express 64 different characters
- 8-dot system
	- Kanji Braille
		- Not commonly used
		- No issues with reading interpretation

### Braille
- Kanji -> Reading conversion is necessary
	- Often overlooked by other services
- Translation
- App
	- Expensive
	- Not always accurate

### Automatic Braille Translation
- Manual work
	- Volunteers
		- Time-consuming
		- [Sapie Library](https://www.sapie.or.jp/cgi-bin/CN1WWW)
			- Braille data
- Current approaches
	- Braille translation
		- Paid apps and services
		- [Online Braille Translation](http://muzik.gr.jp/tenji/conv_tenji.asp)
			- Using Mecab
				- Mecab
					- Morphological analysis tool
						- Similar to spaCy
					- Can obtain reading information
						- Phonetic reading
						- ha (は, わ) he (へ, え)
		- chatGPT
			- GPT3.5
			- GPT4
		- liblouis
			- Rule-based
			- Only for Kanji Braille?
		- Examples ignoring reading issues
- Issues
	- Need to estimate the correct reading from multiple possible readings
		- Kanji often have multiple readings
			- [On average, 1.84 different readings exist per Kanji character](https://scholar.google.com/scholar_url?url=https://ipsj.ixsq.nii.ac.jp/ej/%3Faction%3Dpages_view_main%26active_action%3Drepository_view_main_item_detail%26item_id%3D10268%26item_no%3D1%26page_id%3D13%26block_id%3D8&hl=en&sa=T&oi=gsb&ct=res&cd=0&d=13269403299765182997&ei=gcmbZbfcC9qs6rQP04mLyAg&scisig=AFWwaeZuTfQbEnIf7guEqi-DPmlo)
			- Differences in On'yomi and Kun'yomi
				- On'yomi
					- From Chinese
					- 日 (ひ)
				- Kun'yomi
					- Native Japanese
					- 日 (にち)
			- Differences in voiced and unvoiced sounds
				- Sequential voicing
				- 会社
					- カイシャ
						- As a standalone word
					- ガイシャ
						- In compound words
							- 株式会社、有限会社
			- Homophones
				- Reading changes depending on context
				- 今日
					- キョウ
						- Today
					- コンニチ
						- Recently
			- Synonyms
				- 昨日
					- キノウ
					- サクジツ
			- Japanese notation
				- Same reading, different character systems
					- Katakana
						- アイ (ai)
					- Hiragana
						- あい (ai)
				- Kanji
					- 愛、藍、阿井 (ai)

## Motivation

## Related Research

### Kanji -> Reading
- Machine Learning
	- Definitely more accurate
	- Requires extensive training data
		- Studies have created corpora
			- Mecab
			- Aozora Bunko
			- Japanese Corpora
	- Japanese language model
		- Fine-tuning

### Contribution
- Potential of LLM

### Braille
- Overview
- Rule-Based Approach
- Machine Learning-Based Approach
- LLM-Based Approach

### ML->LLM Transition

## My Project

### Contribution?
- The potential combination of LLM and other resources (like dictionaries)
- Possibilities with Japanese Language Models
- Reducing Necessary Resources
- Fast, Accurate
- Beyond Braille
	- Language Learners
	- Voiceover

### Overview
- Using ChatGPT
- Prompt Creation
	- Based on Mecab results
	- Adding dictionary data
- Determining readings with LLM

### Fast, Accurate, Affordable

## Pipeline

### Preprocessing
- Receiving Input
	- One sentence at a time
		- Too many prompts otherwise
	- Future: Use of multiple sentences
- Morphological Analysis
	- Tokenization
		- Dividing into chunks
			- To facilitate analysis
		- Unique tokenization for Braille
	- Mecab
		- Morphological analyzer, tokenizer tool
			- Widely used in research
		- Acquiring basic readings
			- How accurate?
		- Sound
		- Pronunciation
			- Phonetic changes
		- POS
			- Later use?
	- [KyTea](https://www.phontron.com/kytea/)?
- Checking for Kanji Inclusion
	- Input
		- Morphologically analyzed data
	- Not all readings need to be searched
		- If all Hiragana
			- Pass through
			- ha, he
				- Processable by Mecab
			- What if it should be Kanji but is written in Hiragana?
		- If Kanji included
- Filtering Ambiguous Kanji
	- Input
		- Chunks containing Kanji
	- If single-entry reading
		- Use that reading
	- Single-entry but multiple readings
		- How to distinguish?
			- Yesterday (きのう) or Yesterday (さくじつ)
			- Today (きょう) or Today (こんにち)
				- Entry

### Prompt Engineering
- Retrieving Dictionary Entries
	- Input
		- Only ambiguous chunks
	- Josh API
		- Scraping Japanese dictionary in English
			- Language consistency
			- Only readings written in Hiragana
			- References?
		- Not official
			- Example: MoeDict
	- Data
		- Entries
		- pos?
		- Readings
		- Example sentences?
- Designing Prompts
	- Input
		- Original text
		- Ambiguous chunks
		- Dictionary information
	- Langchain for prompt templates
		- Prompting
			- Design
				- Data
					- Input text
					- Ambiguous Kanji
				- How to determine readings considering the text's context
					- How to incorporate context
						- Provide context?
			- Just converting
				- Inaccurate
			- Convert only ambiguous parts
			- Can't give too many prompts
				- Needed
					- Lots of information
					- But simple and small tokens
		- OpenAI API
	- Output Parser
		- Output only a list
			- To use this list later
		- Didn't work out?
		- Output
			- Readings of ambiguous chunks (List)

### Conversion to Braille
- Update Kana Data of Input
	- Input
		- Readings of ambiguous chunks (List)
	- Obtain results from LLM
		- Decide on the readings
	- Add word order numbering
	- Update dictionary
- Creation of a Braille Dictionary
	- Originally in CSV
		- Adding 1-to-1 data
	- Data
		- Hiragana
		- Katakana
		- Alphabet
		- Braille
		- Unicode
		- Representation of Numbers
- Conversion to Braille
	- Dictionary Mapping
- Display Conversion Results

## Experiment

### Evaluation
- Dataset
	- Japanese Written Language Corpus?
	- About 50 characters per data
	- Contain one ambiguous reading word
	- 36 items
		- 18 types × 2 pairs
- Creation of Dataset
	- Reading Answers
	- Translator's Results
	- [difflib](https://docs.python.org/3/library/difflib.html)
	- Pairs of Ambiguous Readings
		- Too short?
		- Longer version
			- Didn't work well…
- Method
	- Old Method
		- Mistakes in target word
			- -2 points
		- Other mistakes
			- -1 point
	- Check only the target word
		- Is this method sufficient?
		- Check if answer key is included
- Pipeline
	- Preprocessing
		- Adding Kana_answer
	- streamlit
		- Evaluation
			- CSV Input
			- Convert CSV to Pandas Dataframe
				- test_texts
					- Rename
					- Text data
				- target_words
					- Rename
			- Testing
				- Test Type
					- Mecab
						- Connecting 'reading' information
					- GPT 3.5
						- One shot prompting
						- Langchain's Prompt template
							- Only instruction to convert to Katakana
					- GPT 4
						- One shot prompting
						- Langchain's Prompt template
							- Only instruction to convert to Katakana
					- Mecab + GPT
						- Proposed method of this study
					- Japanese Pretrained Model?
					- Liblouis?
						- Not compatible with 6-dot Braille
				- Execute Test
				- Compare Target Words
					- Whether included or not
					- Editable Results
				- Obtain Accuracy

### Results and Discussion
- Mecab
	- Some answers consider context
	- Some fail to understand context and give the same reading
	- 66.667%
- GPT3.5
	- Inaccurate
		- Hallucination?
		- Mixed Kana + Hiragana
		- Simply outputs words
- GPT4
	- Better than GPT3.5
	- Hallucination?
- Mecab+GPT
	- Highest accuracy rate

## Conclusion and Future Work

### Conclusion

### Limitations
- More input
	- More expensive
	- More time-consuming
- Spacing
	- ↓ Accuracy
- Other Models
