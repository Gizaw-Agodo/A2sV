# Enter your code here. Read input from STDIN. Print output to STDOUT
english_numbers = int(input())
english = set(input().split())
french_numbers = int(input())
french = set(input().split())
difference = english.difference(french)
print(len(difference))
