string = "BCAAADADCCCADD"

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.right = right
        self.left = left
        
    def children(self):
        return (self.left, self.right)
    
    def nodes(self):
        return (self.left, self.right)
    
    def __str__(self):
        return '%s_%s' % (self.left, self.right)
    
def huffman_code_tree(node, left=True, binString=''):
    if isinstance(node, str):
        return {node: binString}
    
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
        
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = [(key, c) for key, c in freq]

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmancode = huffman_code_tree(nodes[0][0])

print('char | Huffman code')
print("-----------------------")
for (char, frequency) in freq:
    print(' %-4s | %12s' % (char, huffmancode[char]))
