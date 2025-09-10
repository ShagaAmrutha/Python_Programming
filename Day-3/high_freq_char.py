s=input("enter string")
freq={}
for ch in s:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch]=1
high_char=None
high_freq=0
for ch in freq:
    if freq[ch]>high_freq:
        high_freq=freq[ch]
        high_char=ch
print("Highest frequency character:", high_char)
print("Frequency:", high_freq)