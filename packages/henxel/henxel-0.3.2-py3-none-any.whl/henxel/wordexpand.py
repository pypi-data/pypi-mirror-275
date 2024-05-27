'''Complete the current word before the cursor with words in the editor.

This file is taken from Python:idlelib -github-page:
https://github.com/python/cpython/tree/3.11/Lib/idlelib/

Each call to expand_word() replaces the word with a
different word with the same prefix. The search for matches begins
before the target and moves toward the top of the editor. It then starts
after the cursor and moves down. It then returns to the original word and
the cycle starts again.

Changing the current text line or leaving the cursor in a different
place before requesting the next selection causes ExpandWord to reset
its state.
'''


import re


class ExpandWord:
	wordchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.'
	# string.ascii_letters + string.digits + "_" + "."


	def __init__(self, textwid):
		"textwid is tkinter.Text -widget"
		
		self.textwid = textwid
		self.bell = self.textwid.bell
		self.state = None
		

	def expand_word(self):
		"Replace the current word with the next expansion."
		
		curinsert = self.textwid.index("insert")
		curline = self.textwid.get("insert linestart", "insert lineend")
		
		# if used first time:
		if not self.state:
			words = self.getwords()
			index = 0
			
			
		# if used second time:
		else:
			words, index, insert, line = self.state
			
			if insert != curinsert or line != curline:
				words = self.getwords()
				index = 0
				
				
		if not words:
			self.bell()
			return "break"
			
			
			
		word = self.getprevword()
		self.textwid.delete("insert - %d chars" % len(word), "insert")
		
		newword = words[index]
		index = (index + 1) % len(words)
		
		if index == 0:
			self.bell()            # Warn we cycled around
			
		self.textwid.insert("insert", newword)
		

		curinsert = self.textwid.index("insert")
		curline = self.textwid.get("insert linestart", "insert lineend")
		self.state = words, index, curinsert, curline
		
		return "break"

			
	def getwords(self):
		"Return a list of words that match the prefix before the cursor."
		
		word = self.getprevword()

		if not word:
			return []

		before = self.textwid.get("1.0", "insert wordstart")
		wbefore = re.findall(r"\b" + word + r"\w+\b", before)
		del before

		after = self.textwid.get("insert wordend", "end")
		wafter = re.findall(r"\b" + word + r"\w+\b", after)
		del after

		if not wbefore and not wafter:
			return []
		
		
		words = []
		dict = {}
		
		# search backwards through words before
		wbefore.reverse()

		for w in wbefore:
			if dict.get(w):
				continue
				
			words.append(w)
			dict[w] = w

		# search onwards through words after
		for w in wafter:
			if dict.get(w):
				continue
			
			words.append(w)
			dict[w] = w

		words.append(word)
		return words


	def getprevword(self):
		"Return the word prefix before the cursor."

		line = self.textwid.get("insert linestart", "insert")
		i = len(line)

		while i > 0 and line[i-1] in self.wordchars:
			i = i-1

		return line[i:]

