import argparse

parser = argparse.ArgumentParser(description= 'Search for words including partial word')
parser.add_argument('snippet', help = 'partial (or complete) string to search for in words' )

args = parser.parse_args()
snippet = args.snippet.lower()

#words = open('/usr/share/dict/words').readlines()
#with open('usr/home/xmen_base') as file: 
    #words = f.readlines()
#real words = open('/usr/home/xmen_base').readlines()
#real print([word for word in words if snippet in word.lower()])
    

matches = []

for word in words:
    if snippet in word .lower():
            matches.append(word)
            
print(matches)

