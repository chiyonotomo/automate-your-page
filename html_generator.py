# PROS: much less repetition! which means less room for silly typographical errors :]
# CON: still relies a bit on specific 'coding' for the input, albeit much simpler than actual HTML


# all the text copy-pasted from browser view of my HTML page, plus added 'CODE' for styling
test_text = """WORD: DOM - Document Object Model
DEFINITION: A cross-platform and language-independent convention for representing and interacting with objects in HTML (and other markup languages).
The nodes of every document are organized in a tree structure, called the DOM tree.
In a browser, this structure shows up as a series of nested boxes.
WORD: HTML - HyperText Markup Language
DEFINITION: The standard markup language used to create web pages.
When writing HTML, we tell browsers the type of each element by using HTML tags.
Elements are either inline or block. Block elements form an "invisible box" around the content inside of them.
A good resource/tutorial is available at w3schools.
WORD: CSS - Cascading Style Sheets
DEFINITION: Style sheet language used for describing the look and formatting of a document written in a markup language.
This is done by giving similar HTML elements the same class name and then specifying the style that should apply to that class.
CSS helps us to avoid repetition and to maintain consistency.
This zen garden shows how cool and powerful these style sheets can be.
WORD: Python
DEFINITION: High-level computer programming language, run by an interpreter of the same name.
WORD: variable
DEFINITION: Assigned with the statement [CODE]<name> = <expression>[/CODE]
The name can be alphanumeric and underscores, but cannot lead with a number.
Once defined, a variable's value can be changed.
WORD: string
DEFINITION: Can use single ([CODE]'[/CODE]) or double ([CODE]"[/CODE]) quotes. Triple for multi-line.
Indexed starting at 0: eg, [CODE]<string>[<expression>][/CODE]
Negative expression goes backward, -1 being the last character of the string.
Select subsequence of a string: [CODE]<string>[<expression>:<expression>][/CODE]
[CODE]<string>.find(<substring>)[/CODE] provides the position where the substring is first found.
WORD: function
DEFINITION: A tool to create something that can be used repeatedly.
To define: def [CODE]<function>(<input>,<input>,...][/CODE]
Use a return statement for the output.
To use, call it by writing the name followed by values for the arguments in parenthesis.
WORD: making decisions
DEFINITION: number comparison operators: [CODE]<[/CODE], [CODE]>[/CODE], [CODE]<=[/CODE], [CODE]>=[/CODE] [Boolean output]
[CODE]if[/CODE], [CODE]elif[/CODE], [CODE]else[/CODE]
loops: [CODE]while[/CODE], [CODE]for[/CODE]
WORD: list
DEFINITION: Super versatile: a sequence of any combination of anything (strings, numbers, lists).
[CODE]<list> = [<expression>, <expression>,...][/CODE]
Elements in a list can be mutated/changed after the list is created.
Supports aliasing, for two different ways to refer to the same object.
Operations include [CODE]<list>.append(<element>)[/CODE], concatenation ([CODE]+[/CODE]), [CODE]len(<list>)[/CODE]
WORD: problem solving
DEFINITION: 1. What are the inputs?
2. What are the outputs?
3. Solve the problem as a human, try some examples.
4. Find simple mechanical solutions.
5. Develop incrementally and test as you go.
WORD: debugging
DEFINITION: Examine error messages.
Check intermediate results by printing.
Comment out ([CODE]#[/CODE]) and check old versions."""


# function to take two separate chunks of text and spits out HTML
# input is two strings of characters
# output is concatenated strings
# "word" and "definition" are the corresponding classes used in the CSS
# for use after create_text [this is the final step]
def htmlize(word,definition):
    html_for_start = """    <p class="word">
        <strong>"""
    html_for_mid = """</strong>
    </p>
        
    <p class="definition">
        """
    html_for_end = """
    </p>
    """
    print html_for_start + word + html_for_mid + definition + html_for_end

# simple test htmlize:
#print htmlize("Python","High-level computer programming language, run by an interpreter of the same name.")


# function to take one large chunk of text and break up into nested lists of [WORD, DEFINITION]
# first removes text's line break \n
# input is a string of characters
# output is a list of lists, inner list has two elements
# designated by [WORD] and [DEFINITION] in the original text
# assumes that if there is a WORD there must be a DEFINITION that follows
# first accounts for HTMl replacements...
# replaces line break \n with <br> in definition, removes \n from word
def create_text(text):
	text = text.replace("<","&lt;")
	text = text.replace("[CODE]",'<span class="code">')
	text = text.replace("[/CODE]","</span>")
	text_nested_lists = []
	while text.find("WORD:") > -1:
		word_start = text.find("WORD: ") + len("WORD: ")
		word_end = text.find("DEFINITION:")
		def_start = text.find("DEFINITION: ") + len("DEFINITION: ")
		if text.find("WORD:",word_start) == -1:
			text_nested_lists.append([text[word_start:word_end],text[def_start:]])
		else:
			def_end = text.find("WORD:",word_start)
			text_nested_lists.append([text[word_start:word_end],text[def_start:def_end]])
		text = text[def_end:]
	for i in text_nested_lists:
		i[0] = i[0].replace('\n','')
		i[1] = i[1].replace('\n','<br>')
	return text_nested_lists

# does not yet account for text starting with WORD (find = 0)
# what happens with line break in text? in a multi-line string """ ?

# simple tests create_text, to see the list:
#print create_text(test_text)
# for better readability:
#for i in create_text(test_text):
#	print i[0]
#	print i[1]


# function to put it all together now...
def html_magic(text):
	for i in create_text(text):
		htmlize(i[0],i[1])

html_magic(test_text)