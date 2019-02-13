#command to run the program
#python2 filename.py

from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights/frequency"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    #print heap
    heapify(heap)#maintains priprity qeue.heap[0] always the smallest element(according to frequency)
    #print heap
    while len(heap) > 1:
        lo = heappop(heap)# smallest of heap element is popped(min heap)
        #print lo
        hi = heappop(heap)#2nd smallest of heap element is popped(min heap)
        # print hi
        # print heap
        # print lo[1:]
        # print lo[0]
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]#assigning 0 to the left element
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]#assigning 1 to the left element
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])#building tree structure
        #print heap
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))#sorying the heap based on bits represented
print 'enter the text'
txt = raw_input()
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1#calculating the frequency of characters
#print symb2freq
huff = encode(symb2freq)
#print huff
print "Symbol\tWeight\tHuffman Code"
for p in huff:
    print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])