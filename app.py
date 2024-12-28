print("Hello Git!")
s = ["hello","madam"]
for x in s:
    print(f'original : {x}\treversed : {x[::-1]}')
    if(x == x[::-1]):
        print(f'{x} is a palindrome')
    else:
        print(f'{x} is not a palindrome')