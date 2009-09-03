import gcj
import sys

class Pattern:
    def __init__(self,pat):
        self.pattern=[]
        totallen=len(pat)
        end=0
        while end < totallen:
            begin=end
            extended_pattern=False
            if pat[begin] == '(':
                extended_pattern=True
            if extended_pattern:
                begin += 1
                end = pat.find(')',begin)
            else:
                end=begin+1
            self.pattern.append(pat[begin:end])
            if extended_pattern:
                end += 1

    def __str__(self):
        ret=""
        for letter in self.pattern:
            if len(letter)==1:
                ret+=letter
            else:
                ret+="(%s)" % letter
        return ret

class Node:
    def __init__(self,letter,parent,children_dict=None):
        if children_dict is None:
            children_dict = {}
        self.letter=letter
        self.parent=parent
        self.children=children_dict
        self.children.update(children_dict)

    @staticmethod
    def root(children_dict=None):
        return Node(None,None,children_dict)

    @staticmethod
    def advance(matches,letters):
        new_matches=[]
        for match in matches:
            for letter in letters:
                match_node=match.children.get(letter)
                if match_node is not None:
                    new_matches.append(match_node)
        return new_matches

    def insert(self,word):
        cur_node = self
        for letter in word:
            cur_node=cur_node.children.setdefault(letter,Node(letter,cur_node))

    def _print(self,indent=-1):
        if self.letter:
            print indent*" " + self.letter
        for letter,letter_node in self.children.iteritems():
            letter_node._print(indent+1)

    def assemble(self):
        if not self.children:
            words=[self.letter]
        else:
            words=[]
            for letter,child in self.children.iteritems():
                words.extend(child.assemble())
            for i,word in enumerate(words):
                words[i]=self.letter + word
        return words

class Solver(gcj.Solver):
    def solve(self):
        L,D,N = self._getintsline()
        self.words = Node.root()
        sys.stderr.write("Building dictionary of words\n")
        for i in xrange(D):
            self.words.insert(self._getstringline())
        case=0
        cases=N
        while cases:
            matches=[self.words]
            cases-=1
            case+=1
            sys.stderr.write("Solving case %d\n" % case)
            pattern=Pattern(self._getstringline())
            for i in xrange(L):
                matches=Node.advance(matches,pattern.pattern[i])
                if not matches:
                    break
            print "Case #%d: %s" % (case, len(matches))
