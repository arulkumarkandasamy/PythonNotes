```
Files

f = open('C:\\workspace\\Masters.txt')

f.readline()

Python File Modes

Mode

Description

'r'

Open a file for reading. (default)

'w'

Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.

'x'

Open a file for exclusive creation. If the file already exists, the operation fails.

'a'

Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.

't'

Open in text mode. (default)

'b'

Open in binary mode.

'+'

Open a file for updating (reading and writing)

f = open("test.txt",mode = 'r',encoding = 'utf-8')



How to close a file Using Python?

f = open("test.txt",encoding = 'utf-8')

# perform file operations

f.close()



A safer way is to use a try...finally block.

try:

   f = open("test.txt",encoding = 'utf-8')

   # perform file operations

finally:

   f.close()



The best way to do this is using the with statement. This ensures that the file is closed when the block inside with is exited.

We don't need to explicitly call the close() method. It is done internally.

with open("test.txt",encoding = 'utf-8') as f:

   # perform file operations



How to write to File Using Python?

with open("test.txt",'w',encoding = 'utf-8') as f:

   f.write("my first file\n")

   f.write("This file\n\n")

   f.write("contains three lines\n")



How to read files in Python?

f = open("test.txt",'r',encoding = 'utf-8')

f.read(4)    # read the first 4 data

f.read(4)    # read the next 4 data

f.read()     # read in the rest till end of file

f.read()  # further reading returns empty sting

read() method returns newline as '\n'. Once the end of file is reached, we get empty string on further reading.



We can change our current file cursor (position) using the seek() method. Similarly, the tell() method returns our current position (in number of bytes).

f.tell()    # get the current file position

f.seek(0)   # bring file cursor to initial position

print(f.read())  # read the entire file



We can read a file line-by-line using a for loop. This is both efficient and fast.

for line in f:

     print(line, end = '')



Alternately, we can use readline() method to read individual lines of a file.

f.readline()



readlines() method returns a list of remaining lines of the entire file.



Python File Methods

Method

Description

close()

Close an open file. It has no effect if the file is already closed.

detach()

Separate the underlying binary buffer from the TextIOBase and return it.

fileno()

Return an integer number (file descriptor) of the file.

flush()

Flush the write buffer of the file stream.

isatty()

Return True if the file stream is interactive.

read(n)

Read atmost n characters form the file. Reads till end of file if it is negative or None.

readable()

Returns True if the file stream can be read from.

readline(n=-1)

Read and return one line from the file. Reads in at most n bytes if specified.

readlines(n=-1)

Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.

seek(offset,from=SEEK_SET)

Change the file position to offset bytes, in reference to from (start, current, end).

seekable()

Returns True if the file stream supports random access.

tell()

Returns the current file location.

truncate(size=None)

Resize the file stream to size bytes. If size is not specified, resize to current location.

writable()

Returns True if the file stream can be written to.

write(s)

Write string s to the file and return the number of characters written.

writelines(lines)

Write a list of lines to the file.







urllib2

The urllib and urllib2 modules are merged together in python3 as urllib.



# Used to make requests

import urllib.request



x = urllib.request.urlopen('https://www.google.com/')

print(x.read())



# used to parse values into the url

import urllib.parse



url = 'https://www.google.com/search'

values = {'q' : 'python programming tutorials'}

data = urllib.parse.urlencode(values)

data = data.encode('utf-8') # data should be bytes

req = urllib.request.Request(url, data)

resp = urllib.request.urlopen(req)

respData = resp.read()



print(respData)



# Another Example

try:

    x = urllib.request.urlopen('https://www.google.com/search?q=test')

    #print(x.read())



    saveFile = open('noheaders.txt','w')

    saveFile.write(str(x.read()))

    saveFile.close()

except Exception as e:

    print(str(e))



# Another Example 2

try:

    url = 'https://www.google.com/search?q=python'



    # now, with the below headers, we defined ourselves as a simpleton who is

    # still using internet explorer.

    headers = {}

    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    req = urllib.request.Request(url, headers = headers)

    resp = urllib.request.urlopen(req)

    respData = resp.read()



    saveFile = open('withHeaders.txt','w')

    saveFile.write(str(respData))

    saveFile.close()

except Exception as e:

    print(str(e))



Start a static HTTP server in any directory





Python Regular Expressions

re.search

>>> import re

>>> m = re.search('(?<=abc)def', 'abcdef')

>>> m.group(0)

'def'

This example looks for a word following a hyphen:

>>> m = re.search(r'(?<=-)\w+', 'spam-egg')

>>> m.group(0)

'egg'



re.compile(pattern, flags=0)

The sequence

prog = re.compile(pattern)

result = prog.match(string)

is equivalent to

result = re.match(pattern, string)

but using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.



Following regular expression objects that match a decimal number are functionally equal:

a = re.compile(r"""\d +  # the integral part

                   \.    # the decimal point

                   \d *  # some fractional digits""", re.X)

b = re.compile(r"\d+\.\d*")



re.split(pattern, string, maxsplit=0, flags=0)¶

Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.

>>>

>>> re.split(r'\W+', 'Words, words, words.')

['Words', 'words', 'words', '']

>>> re.split(r'(\W+)', 'Words, words, words.')

['Words', ', ', 'words', ', ', 'words', '.', '']

>>> re.split(r'\W+', 'Words, words, words.', 1)

['Words', 'words, words.']

>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)

['0', '3', '9']

If there are capturing groups in the separator and it matches at the start of the string, the result will start with an empty string. The same holds for the end of the string:

>>>

>>> re.split(r'(\W+)', '...words, words...')

['', '...', 'words', ', ', 'words', '...', '']

That way, separator components are always found at the same relative indices within the result list.

Empty matches for the pattern split the string only when not adjacent to a previous empty match.

>>> re.split(r'\b', 'Words, words, words.')

['', 'Words', ', ', 'words', ', ', 'words', '.']

>>> re.split(r'\W*', '...words...')

['', '', 'w', 'o', 'r', 'd', 's', '', '']

>>> re.split(r'(\W*)', '...words...')

['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', '']



re.sub(pattern, repl, string, count=0, flags=0)¶

Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; if it is a string, any backslash escapes in it are processed. That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth. Unknown escapes such as \& are left alone. Backreferences, such as \6, are replaced with the substring matched by group 6 in the pattern. For example:

>>>

>>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',

...        r'static PyObject*\npy_\1(void)\n{',

...        'def myfunc():')

'static PyObject*\npy_myfunc(void)\n{'

If repl is a function, it is called for every non-overlapping occurrence of pattern. The function takes a single match object argument, and returns the replacement string. For example:

>>>

>>> def dashrepl(matchobj):

...     if matchobj.group(0) == '-': return ' '

...     else: return '-'

>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')

'pro--gram files'

>>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)

'Baked Beans & Spam'

The pattern may be a string or a pattern object.



re.escape(pattern)¶

Escape special characters in pattern. This is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it. For example:

>>>

>>> print(re.escape('python.exe'))

python\.exe



>>> legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"

>>> print('[%s]+' % re.escape(legal_chars))

[abcdefghijklmnopqrstuvwxyz0123456789!\#\$%\&'\*\+\-\.\^_`\|\~:]+



>>> operators = ['+', '-', '*', '/', '**']

>>> print('|'.join(map(re.escape, sorted(operators, reverse=True))))

/|\-|\+|\*\*|\*

This functions must not be used for the replacement string in sub() and subn(), only backslashes should be escaped. For example:

>>>

>>> digits_re = r'\d+'

>>> sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'

>>> print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))

/usr/sbin/sendmail - \d+ errors, \d+ warnings



Regular Expression Examples

Checking for a Pair

In this example, we’ll use the following helper function to display match objects a little more gracefully:

def displaymatch(match):

    if match is None:

        return None

    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

Suppose you are writing a poker program where a player’s hand is represented as a 5-character string with each character representing a card, “a” for ace, “k” for king, “q” for queen, “j” for jack, “t” for 10, and “2” through “9” representing the card with that value.

To see if a given string is a valid hand, one could do the following:

>>>

>>> valid = re.compile(r"^[a2-9tjqk]{5}$")

>>> displaymatch(valid.match("akt5q"))  # Valid.

"<Match: 'akt5q', groups=()>"

>>> displaymatch(valid.match("akt5e"))  # Invalid.

>>> displaymatch(valid.match("akt"))    # Invalid.

>>> displaymatch(valid.match("727ak"))  # Valid.

"<Match: '727ak', groups=()>"

That last hand, "727ak", contained a pair, or two of the same valued cards. To match this with a regular expression, one could use backreferences as such:

>>>

>>> pair = re.compile(r".*(.).*\1")

>>> displaymatch(pair.match("717ak"))     # Pair of 7s.

"<Match: '717', groups=('7',)>"

>>> displaymatch(pair.match("718ak"))     # No pairs.

>>> displaymatch(pair.match("354aa"))     # Pair of aces.

"<Match: '354aa', groups=('a',)>"

To find out what card the pair consists of, one could use the group() method of the match object in the following manner:

>>> pair.match("717ak").group(1)

'7'



# Error because re.match() returns None, which doesn't have a group() method:

>>> pair.match("718ak").group(1)

Traceback (most recent call last):

  File "<pyshell#23>", line 1, in <module>

    re.match(r".*(.).*\1", "718ak").group(1)

AttributeError: 'NoneType' object has no attribute 'group'



>>> pair.match("354aa").group(1)

'a'

Simulating scanf()

Python does not currently have an equivalent to scanf(). Regular expressions are generally more powerful, though also more verbose, than scanf() format strings. The table below offers some more-or-less equivalent mappings between scanf() format tokens and regular expressions.

scanf() Token

Regular Expression

%c

.

%5c

.{5}

%d

[-+]?\d+

%e, %E, %f, %g

[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?

%i

[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)

%o

[-+]?[0-7]+

%s

\S+

%u

\d+

%x, %X

[-+]?(0[xX])?[\dA-Fa-f]+

To extract the filename and numbers from a string like

/usr/sbin/sendmail - 0 errors, 4 warnings

you would use a scanf() format like

%s - %d errors, %d warnings

The equivalent regular expression would be

(\S+) - (\d+) errors, (\d+) warnings

search() vs. match()

Python offers two different primitive operations based on regular expressions: re.match() checks for a match only at the beginning of the string, while re.search() checks for a match anywhere in the string (this is what Perl does by default).

For example:

>>>

>>> re.match("c", "abcdef")    # No match

>>> re.search("c", "abcdef")   # Match

<re.Match object; span=(2, 3), match='c'>

Regular expressions beginning with '^' can be used with search() to restrict the match at the beginning of the string:

>>>

>>> re.match("c", "abcdef")    # No match

>>> re.search("^c", "abcdef")  # No match

>>> re.search("^a", "abcdef")  # Match

<re.Match object; span=(0, 1), match='a'>

Note however that in MULTILINE mode match() only matches at the beginning of the string, whereas using search() with a regular expression beginning with '^' will match at the beginning of each line.

>>>

>>> re.match('X', 'A\nB\nX', re.MULTILINE)  # No match

>>> re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match

<re.Match object; span=(4, 5), match='X'>

Making a Phonebook

split() splits a string into a list delimited by the passed pattern. The method is invaluable for converting textual data into data structures that can be easily read and modified by Python as demonstrated in the following example that creates a phonebook.

First, here is the input. Normally it may come from a file, here we are using triple-quoted string syntax:

>>>

>>> text = """Ross McFluff: 834.345.1254 155 Elm Street

...

... Ronald Heathmore: 892.345.3428 436 Finley Avenue

... Frank Burger: 925.541.7625 662 South Dogwood Way

...

...

... Heather Albrecht: 548.326.4584 919 Park Place"""

The entries are separated by one or more newlines. Now we convert the string into a list with each nonempty line having its own entry:

>>> entries = re.split("\n+", text)

>>> entries

['Ross McFluff: 834.345.1254 155 Elm Street',

'Ronald Heathmore: 892.345.3428 436 Finley Avenue',

'Frank Burger: 925.541.7625 662 South Dogwood Way',

'Heather Albrecht: 548.326.4584 919 Park Place']

Finally, split each entry into a list with first name, last name, telephone number, and address. We use the maxsplit parameter of split() because the address has spaces, our splitting pattern, in it:

>>> [re.split(":? ", entry, 3) for entry in entries]

[['Ross', 'McFluff', '834.345.1254', '155 Elm Street'],

['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'],

['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'],

['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]

The :? pattern matches the colon after the last name, so that it does not occur in the result list. With a maxsplit of 4, we could separate the house number from the street name:

>>> [re.split(":? ", entry, 4) for entry in entries]

[['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'],

['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'],

['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'],

['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']]

Text Munging

sub() replaces every occurrence of a pattern with a string or the result of a function. This example demonstrates using sub() with a function to “munge” text, or randomize the order of all the characters in each word of a sentence except for the first and last characters:

>>>

>>> def repl(m):

...     inner_word = list(m.group(2))

...     random.shuffle(inner_word)

...     return m.group(1) + "".join(inner_word) + m.group(3)

>>> text = "Professor Abdolmalek, please report your absences promptly."

>>> re.sub(r"(\w)(\w+)(\w)", repl, text)

'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'

>>> re.sub(r"(\w)(\w+)(\w)", repl, text)

'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'

Finding all Adverbs

findall() matches all occurrences of a pattern, not just the first one as search() does. For example, if a writer wanted to find all of the adverbs in some text, they might use findall() in the following manner:

>>>

>>> text = "He was carefully disguised but captured quickly by police."

>>> re.findall(r"\w+ly", text)

['carefully', 'quickly']

Finding all Adverbs and their Positions

If one wants more information about all matches of a pattern than the matched text, finditer() is useful as it provides match objects instead of strings. Continuing with the previous example, if a writer wanted to find all of the adverbs and their positions in some text, they would use finditer() in the following manner:

>>>

>>> text = "He was carefully disguised but captured quickly by police."

>>> for m in re.finditer(r"\w+ly", text):

...     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

07-16: carefully

40-47: quickly

Raw String Notation

Raw string notation (r"text") keeps regular expressions sane. Without it, every backslash ('\') in a regular expression would have to be prefixed with another one to escape it. For example, the two following lines of code are functionally identical:

>>>

>>> re.match(r"\W(.)\1\W", " ff ")

<re.Match object; span=(0, 4), match=' ff '>

>>> re.match("\\W(.)\\1\\W", " ff ")

<re.Match object; span=(0, 4), match=' ff '>

When one wants to match a literal backslash, it must be escaped in the regular expression. With raw string notation, this means r"\\". Without raw string notation, one must use "\\\\", making the following lines of code functionally identical:

>>>

>>> re.match(r"\\", r"\\")

<re.Match object; span=(0, 1), match='\\'>

>>> re.match("\\\\", r"\\")

<re.Match object; span=(0, 1), match='\\'>

Writing a Tokenizer

A tokenizer or scanner analyzes a string to categorize groups of characters. This is a useful first step in writing a compiler or interpreter.

The text categories are specified with regular expressions. The technique is to combine those into a single master regular expression and to loop over successive matches:

import collections

import re



Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])



def tokenize(code):

    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}

    token_specification = [

        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number

        ('ASSIGN',   r':='),           # Assignment operator

        ('END',      r';'),            # Statement terminator

        ('ID',       r'[A-Za-z]+'),    # Identifiers

        ('OP',       r'[+\-*/]'),      # Arithmetic operators

        ('NEWLINE',  r'\n'),           # Line endings

        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs

        ('MISMATCH', r'.'),            # Any other character

    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    line_num = 1

    line_start = 0

    for mo in re.finditer(tok_regex, code):

        kind = mo.lastgroup

        value = mo.group()

        column = mo.start() - line_start

        if kind == 'NUMBER':

            value = float(value) if '.' in value else int(value)

        elif kind == 'ID' and value in keywords:

            kind = value

        elif kind == 'NEWLINE':

            line_start = mo.end()

            line_num += 1

            continue

        elif kind == 'SKIP':

            continue

        elif kind == 'MISMATCH':

            raise RuntimeError(f'{value!r} unexpected on line {line_num}')

        yield Token(kind, value, line_num, column)



statements = '''

    IF quantity THEN

        total := total + price * quantity;

        tax := price * 0.05;

    ENDIF;

'''



for token in tokenize(statements):

    print(token)

The tokenizer produces the following output:

Token(type='IF', value='IF', line=2, column=4)

Token(type='ID', value='quantity', line=2, column=7)

Token(type='THEN', value='THEN', line=2, column=16)

Token(type='ID', value='total', line=3, column=8)

Token(type='ASSIGN', value=':=', line=3, column=14)

Token(type='ID', value='total', line=3, column=17)

Token(type='OP', value='+', line=3, column=23)

Token(type='ID', value='price', line=3, column=25)

Token(type='OP', value='*', line=3, column=31)

Token(type='ID', value='quantity', line=3, column=33)

Token(type='END', value=';', line=3, column=41)

Token(type='ID', value='tax', line=4, column=8)

Token(type='ASSIGN', value=':=', line=4, column=12)

Token(type='ID', value='price', line=4, column=15)

Token(type='OP', value='*', line=4, column=21)

Token(type='NUMBER', value=0.05, line=4, column=23)

Token(type='END', value=';', line=4, column=27)

Token(type='ENDIF', value='ENDIF', line=5, column=4)

Token(type='END', value=';', line=5, column=9)



Frequently Used Regular Expressions

    ^ matches the beginning of a string.

    $ matches the end of a string.

    \b matches a word boundary.

    \d matches any numeric digit.

    \D matches any non-numeric character.

    (x|y|z) matches exactly one of x, y or z.

    (x) in general is a remembered group. We can get the value of what matched by using the groups() method of the object returned by re.search.

    x? matches an optional x character (in other words, it matches an x zero or one times).

    x* matches x zero or more times.

    x+ matches x one or more times.

    x{m,n} matches an x character at least m times, but not more than n times.

    ?: matches an expression but do not capture it. Non capturing group.

    ?= matches a suffix but exclude it from capture. Positive look ahead.

    a(?=b) will match the "a" in "ab", but not the "a" in "ac"

    In other words, a(?=b) matches the "a" which is followed by the string 'b', without consuming what follows the a.

    ?! matches if suffix is absent. Negative look ahead.

    a(?!b) will match the "a" in "ac", but not the "a" in "ab"

    ?<= positive look behind

    ?<! negative look behind







Boto3



boto3 client vs resource

https://stackoverflow.com/questions/39272744/when-to-use-a-boto3-client-and-when-to-use-a-boto3-resource



boto3.resources is a high level services class wrap around boto3.client.

It is means to attach connected resources under where you can later use other resources without specify the original resource-id.

import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket('mybucket')



# now bucket is "attached" the S3 bucket name "mybucket"

print(bucket)

# s3.Bucket(name='mybucket')



print(dir(bucket))

#show you all class method action you may perform



OTH, boto3.client are low level, you don't have a "entry class object", thus you must explicitly specify the exact resources it connect to for every action you perform.

It depends on individual needs. However, boto3.resources doesn't wrap all the boto3.client functionality, so sometime you need to call boto3.client , or use boto3.resource.meta.client () to get the job done.



client

c = boto3.client('ec2', region_name='eu-west-1')

instanceid = urllib2.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read()

instance_data = c.describe_instances(InstanceIds=[instanceid])

tags = instance_data['Reservations'][0]['Instances'][0]['Tags']

for tag in tags:

   if tag['Key'] == "Name":

    name=tag['Value']





resources

#!/usr/bin/env python

import sys

import boto3

ec2 = boto3.resource('ec2')

for instance_id in sys.argv[1:]:

    instance = ec2.Instance(instance_id)

    response = instance.terminate()

    print response



Configure system to use boto3

Using the pip command, install the AWS CLI and Boto3:

pip install awscli boto3 -U --ignore-installed six

The -U option will upgrade any packages if they are already installed. On some systems,

there may be issues with a package named "six"; using the "--ignore-installed six" option can work

around those issues.



Run the command "aws --version" and something similar to the following should be reported:

aws-cli/1.11.34 Python/2.7.10 Darwin/15.6.0 botocore/1.4.91

Finally, run the following to check boto3: python -c “import boto3”. If nothing is reported, all is

well. If there are any error messages, review the setup for anything you might have missed.



Users, Permissions, and Credentials

Before we can get up and running on the command line, we need to go to AWS via the web console

to create a user, give the user permissions to interact with specific services, and get credentials to

identify that user.



Back in the terminal, enter aws configure. You’ll be prompted for the AWS access key ID, AWS

secret access key, default region name, and default output format. Using the credentials from the

user creation step, enter the access key ID and secret access key.



quick test

aws ec2 describe-instances







Classes and Instances (__init__, __call__, etc.)

The __init__() method

In Python, objects are created in two steps:

    Constructs an object

    __new()__

    Initializes the object

    __init()__

However, it's very rare to actually need to implement __new()__ because Python constructs our objects for us. So, in most of the cases, we usually only implement the special method, __init()__.

Instance vairables

class Student:

        def __init__(self, id):

                self.id = id

	def setData(self, value):

	self.data = value

	def display(self):

	print(self.data)

self.id is an instance variable.

Properties

Operator overloading: 2.6 __cmp__() (Removed in 3.0)

Operator overloading: __str__

__str__ vs __repr__

When we use print, Python will look for an __str__ method in our class. If it finds one, it will call it. If it does not, it will look for a __repr__ method and call it. If it cannot find one, it will create an internal representation of our object.

sys.argv

sys.argv is the list of arguments passed to the Python program.

The first argument, sys.argv[0], is actually the name of the program. It exists so that we can change our program's behavior depending on how it was invoked.

__call__

Python runs a __call__ method when an instance is called as a function form.



if __name__ == '__main__':

example 1

class Rectangle(object):

	def __init__(self, w, h):

	self.width = w

	self.height = h

	def area(self):

	return self.width * self.height



if __name__ == '__main__':

        r1 = Rectangle(10,20)

        print(r1.width, r1.height)

example 2

def main():

    try:

        doMainthing()

        return 0

    except:

        return 1



if __name__ == "__main__":

    sys.exit(main())



class method vs static method



    simple method : defined outside of a class. This function can access class attributes by feeding instance arg.

    def outside_foo():



    instance method :

    def foo(self,)



    class method : if we need to use class attributes

    @classmethod

    def cfoo(cls,)



    static method : do not have any info about the class

    @staticmethod

    def sfoo()



argparse

The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.



Exception

    Error Handling:

    Python raises exceptions at runtime. We can catch (or ignore) and respond to the errors in our code. If we opt to ignore the raised exception, Python's default exception-handling kicks in and stops our code with an error message. So, if we don't like the default way of handling exception, we may want to catch it using "try".

    Closing time operation:

    We can use "try/finally" to guarantee the execution of a certain operation regardless of the presence or absence of exceptions in our code.

Example 1

    try:

...    raise IndexError

... except IndexError:

...    print('got exception raised by our code')

Example 2

while True:

   try:

      age = int(input("Type in your guess : Age of the Universe : " ))

      print(age)

      break

   except ValueError:

      print("Please make sure you type in an integer")

   except:

      break

   finally:

      print("age loop" )





*args and **kwargs - Collecting and Unpacking Arguments

Putting *args and/or **kwargs as the last items in our function definition's argument list allows that function to accept an arbitrary number of anonymous and/or keyword arguments.







Hash Tables and Hashlib

When we talk about hash tables, we're actually talking about dictionary.

Python provides hashlib for secure hashes and message digests:

md5(), sha*():





Collections

Most common elements in an iterable (collections.Counter)

Double-ended queue (collections.deque)

Double-ended queue with maximum length (collections.deque)

Mapping objects to unique counting numbers (collections.defaultdict)

Largest and smallest elements (heapq.nlargest and heapq.nsmallest)







Lambda

lambdas are sometimes known as anonymous functions. In practice, they are used as a way to inline a function definition, or to defer execution of a code.

    lambda is an expression, not a statement.

    	Because of this, a lambda can appear in places a def is not allowed. For example, places like inside a list literal, or a function call's arguments. As an expression, lambda returns a value that

        can optionally be assigned a name. In contrast, the def statement always assigns the new function to the name in the header, instead of returning is as a result.

    lambda's body is a single expression, not a block of statements.

    	The lambda's body is similar to what we'd put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an

        expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles larger tasks.

exaample

	f = lambda x, y, z: x + y + z

The lambdas can be used as a function shorthand that allows us to embed a function within the code.

lambdas are also commonly used to code jump tables which are lists or dictionaries of actions to be performed on demand.

Nested lambda

	action = (lambda x: (lambda newx: x + newx))

	>>> (  (lambda x: (lambda newx: x + newx)) (99)) (100)

	ans : 199

lambda and sorted()

	sorted(iterable[, key][, reverse])

	sorted(birth, key=lambda age: age[2]) (birth is array of lists)

Flattening lists:

list(itertools.chain.from_iterable(a))

flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]







yield keyword

The yield enables a function to comeback where it left off when it is called again.

The yield keyword helps a function to remember its state.

what is it returning from yield -> generator object





Generator Functions and Expressions

Python provides tools that produce results only when needed:

    Generator functions

    They are coded as normal def but use yield to return results one at a time, suspending and resuming.

    Generator expressions

    These are similar to the list comprehensions. But they return an object that produces results on demand instead of building a result list.

List comprehension makes a list

    [ x ** 3 for x in range(5)]

Generator expression makes an iterable

    (x ** 3 for x in range(5))

Generator expressions

g = (x ** 2 for x in xrange(10))

next(g)



Iterators

iterable produces iterator via __iter__()

	iterator = iterable.__iter__()

iterator produces a stream of values via next()

	value = iterator.next()

	value = iterator.next()

File Iterators

	f = open('C:\\workspace\\Masters.txt')

	f.readline()



Cartesian products (itertools.product)



Combinations and combinations with replacement (itertools.combinations and itertools.combinations_with_replacement)



Permutations (itertools.permutations)



Chaining iterables (itertools.chain)



Grouping rows by a given key (itertools.groupby)







subprocess

http://www.pythonforbeginners.com/os/subprocess-for-system-administrators

subprocess should be used

for accessing system commands.

The subprocess module allows us to spawn processes, connect to their

input/output/error pipes, and obtain their return codes.

Subprocess intends to replace several other, older modules and functions,

like: os.system, os.spawn*, os.popen*, popen2.* commands.



# output of df

df = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)

# pipe df output to grep <devicename>

output = subprocess.check_output(('grep','^/dev/'), stdin=df.stdout).strip().replace('  ', ' ')

# Get free space percentage field and remove the % symbol

used_percentage = output.split()[4][:-1]



Recall notes from bogotobogo



Subprocess Module



The subprocess module allows us to:

    spawn new processes

    connect to their input/output/error pipes

    obtain their return codes

and is intended to replace the following functions:

    os.system()

    os.spawn*()

    os.popen*()

    popen2.*()

    commands.*()



os.system()

The simplest way of running UNIX command is to use os.system(). returns 0

os.popen()

Open a pipe to or from command. The return value is an open file object connected to the pipe, which can be read or written depending on whether mode is 'r' (default) or 'w'. returns stream



subprocess.call()

This is basically just like the Popen class and takes all of the same arguments, but it simply wait until the command completes and gives us the return code.

subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

Run the command described by args. Wait for command to complete, then return the returncode attribute.



subprocess.check_call()

subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

The check_call() function works like call() except that the exit code is checked, and if it indicates an error happened then a CalledProcessError exception is raised.



subprocess.check_output()

subprocess.check_output(args, *, stdin=None, stderr=None,

                                 shell=False, universal_newlines=False)

The standard input and output channels for the process started by call() are bound to the parent's input and output. That means the calling program cannot capture the output of the command. To capture the output, we can use check_output() for later processing.



subprocess.Popen()

subprocess.Popen() executes a child program in a new process. On Unix, the class uses os.execvp()-like behavior to execute the child program. On Windows, the class uses the Windows CreateProcess() function.

class subprocess.Popen(args, bufsize=0, executable=None,

                       stdin=None, stdout=None, stderr=None,

                       preexec_fn=None, close_fds=False,

                       shell=False, cwd=None, env=None, universal_newlines=False,

                       startupinfo=None, creationflags=0)



os.popen vs. subprocess.Popen()

This is intended as a replacement for os.popen, but it is more complicated. For example, we use

subprocess.Popen("echo Hello World", stdout=subprocess.PIPE, shell=True).stdout.read()

instead of

os.popen("echo Hello World").read()

But it is comprehensive and it has all of the options in one unified class instead of different os.popen functions.







Zip Unzip



A mapping object maps immutable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary.#



a = [1, 2, 3, 4, 5, 6]

# Using iterators

group_adjacent = lambda a, k: zip(*([iter(a)] * k))

group_adjacent(a, 3)



# Using slices

from itertools import islice

group_adjacent = lambda a, k: zip(*(islice(a, i, None, k) for i in range(k)))



If the syntax *expression appears in the function call, expression must evaluate to a sequence.

If the syntax **expression appears in the function call, expression must evaluate to a mapping, the contents of which are treated as additional keyword arguments.



itertools.islice(iterable, start, stop[, step])





Sliding windows ( n -grams) using zip and iterators

def n_grams(a, n):

    z = (islice(a, i, None) for i in range(n))

    return zip(*z)



Inverting a dictionary using zip

zip(m.values(), m.keys())

mi = dict(zip(m.values(), m.keys()))



Python's zip, map, and lambda

a = [1, 2, 3, 4, 5]

b = [2, 2, 9, 0, 9]

map(lambda pair: max(pair), zip(a, b))



Dictionary construction with zip

We can use zip to generate dictionaries when the keys and values must be computed at runtime.

keys = ['a', 'b', 'c']

values = [1, 2, 3]

list(zip(keys,values))





Decorator wraps a function without modifying the function itself.

    Adds functionality of the function.

    Modifies the behavior of the function.

Decorator example:



def dollar(fn):

    def new(*args):

        return '$' + str(fn(*args))

    return new



@dollar

def price(amount, tax_rate):

    return amount + amount*tax_rate



print price(100,0.1)

output : $110









Map Filter Reduce



Expression oriented functions of Python provides are:

    map(aFunction, aSequence)

    filter(aFunction, aSequence)

    reduce(aFunction, aSequence)

    lambda

    list comprehension

The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object and returns a list containing all the function call results.

list(map((lambda x: x **2), items))

usually faster than a manually coded for loop

The map call is similar to the list comprehension expression. But map applies a function call to each item instead of an arbitrary expression.

As the name suggests filter extracts each element in the sequence for which the function returns True. The reduce function is a little less obvious in its intent. This function reduces a list to a single value by combining elements via a supplied function.

list( filter((lambda x: x < 0), range(-5,5)))

from functools import reduce

reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

ans : 24







getattr with arbitrary depth. (Python recipe)



def multi_getattr(obj, attr, default = None):

    """

    Get a named attribute from an object; multi_getattr(x, 'a.b.c.d') is

    equivalent to x.a.b.c.d. When a default argument is given, it is

    returned when any attribute in the chain doesn't exist; without

    it, an exception is raised when a missing attribute is encountered.



    """

    attributes = attr.split(".")

    for i in attributes:

        try:

            obj = getattr(obj, i)

        except AttributeError:

            if default:

                return default

            else:

                raise

    return obj



# Example usage

obj  = [1,2,3]

attr = "append.__doc__.capitalize.__doc__"



multi_getattr(obj, attr) #Will return the docstring for the

                         #capitalize method of the builtin string

                         #object





https://askubuntu.com/questions/416930/unable-to-fetch-some-archives-when-trying-to-install-phpmyadmin



sed -i -e 's/zesty/trusty/g' sources.list







six

Six is a Python 2 and 3 compatibility library. It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions.







Built-in Functions

dict([arg])

	Create a new data dictionary, optionally with items taken from arg.

exec(object[, globals[, locals]])

	This function supports dynamic execution of Python code.

filter(function, iterable)

	Construct an iterator from those elements of iterable for which function returns true.

frozenset([iterable])

	Return a frozenset object, optionally with elements taken from iterable.

getattr(object, name[, default])

	Return the value of the named attribute of an object. In other words, it is used to fetch an attribute from an object, using a string object instead of an identifier to identify the attribute.

globals()

	Return a dictionary representing the current global symbol table.

	This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

hash(object)

	Return the hash value of the object (if it has one).

	Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup.

isinstance(object, classinfo)

	Return true if the object argument is an instance of the classinfo argument, or of a (direct or indirect) subclass thereof.

issubclass(class, classinfo)

	Return true if class is a subclass (direct or indirect) of classinfo.

iter(object[, sentinel])

	Return an iterator object.

list([iterable])

	Return a list whose items are the same and in the same order as iterable's items.

map(function, iterable, ...)

	Return an iterator that applies function to every item of iterable, yielding the results.

memoryview(obj)

	Return a memory view object created from the given argument.

next(iterator[, default])

	Retrieve the next item from the iterator by calling its __next__() method.

	If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)

	Open file and return a corresponding stream.

	If the file cannot be opened, an IOError is raised.

property(fget=None, fset=None, fdel=None, doc=None)

	Return a property attribute.

range([start], stop[, step])

	This is a versatile function to create iterables yielding arithmetic progressions.

	It is most often used in for loops.

	The arguments must be integers.

repr(object)

	Return a string containing a printable representation of an object.

reversed(seq)

	Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments

        starting at 0).

round(x[, n])

	Return the floating point value x rounded to n digits after the decimal point.

set([iterable])

	Return a new set, optionally with elements taken from iterab

setattr(object, name, value)

	This is the counterpart of getattr(object, name).

slice([start], stop[, step])

	Return a slice object representing the set of indices specified by range(start, stop, step).

	The start and step arguments default to None.

sorted(iterable[, key][, reverse])

	Return a new sorted list from the items in iterable.

staticmethod(function)

	Return a static method for function.

	A static method does not receive an implicit first argument.

	To declare a static method, use this idiom:

	    class C:

    	        @staticmethod

    	        def f(arg1, arg2, ...): ...

	The @staticmethod form is a function decorator.

str([object[, encoding[, errors]]])

	Return a string version of an object

sum(iterable[, start])

	Sums start and the items of an iterable from left to right and returns the total. start defaults to 0.

super([type[, object-or-type]])

	Return a proxy object that delegates method calls to a parent or sibling class of type.

	This is useful for accessing inherited methods that have been overridden in a class.

tuple([iterable])

	Return a tuple whose items are the same and in the same order as iterable's items.

type(object)

	Return the type of an object.

	The return value is a type object and generally the same object as returned by object.__class__.

type(name, bases, dict)

	Return a new type object.

	This is essentially a dynamic form of the class statement.

zip(*iterables)

	Make an iterator that aggregates elements from each of the iterables.

	Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

	The iterator stops when the shortest input iterable is exhausted.

	With a single iterable argument, it returns an iterator of 1-tuples.

	With no arguments, it returns an empty iterator.



```