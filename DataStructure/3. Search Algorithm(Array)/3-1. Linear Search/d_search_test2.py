from search import seq_search

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ["DTS", "AAC", "FLAC"]

print(f"{t} : {seq_search(t, 5.6)}")
print(f"{s} : {seq_search(s,'n')}")
print(f"{a} : {seq_search(a, 'DTS')}")