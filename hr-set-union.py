# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_members = int(input())
english = set(input().split())

french_numbers = int(input())
french = set(input().split())
print(len(english.union(french)))
