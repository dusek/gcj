import gcj

class Node:
    def __init__(self, probability, feature, left, right):
        assert(isinstance(probability, float))
        assert((feature is None) == (left is None) == (right is None))
        self.probability = probability
        self.feature = feature
        self.left = left
        self.right = right

    @staticmethod
    def Leaf(probability):
        return Node(probability, None, None, None)

    @staticmethod
    def Inner(probability, feature, left, right):
        return Node(probability, feature, left, right)

    @staticmethod
    def parse(str,i=0):
        def get_token(str,i):
            def skipws(str,i):
                c=str[i]
                while c in (' ', '\n', '\t', '\r'):
                    i+=1
                    c=str[i]
                return i
            def findtokenend(str,i):
                c=str[i]
                if c==')':
                    return i+1
                while c not in (' ', '\n', ')'):
                    i+=1
                    c=str[i]
                return i
            i=skipws(str,i)
            start=i
            if str[i]=='(':
                return (i+1,'(')
            end=findtokenend(str,i)
            return (end,str[start:end])
        i,open_paren=get_token(str,i)
        #print repr(open_paren)
        assert(open_paren == '(')
        i,prob_str=get_token(str,i)
        prob=float(prob_str)
        #print "probability: %s" % repr(prob)
        i,feature=get_token(str,i)
        left=None
        right=None
        if feature==')':
            #print repr(')')
            feature=None
        else:
            #print "feature: %s" % repr(feature)
            i,left=Node.parse(str,i)
            i,right=Node.parse(str,i)
            i,close_paren=get_token(str,i)
            #print repr(close_paren)
            assert(close_paren==')')
        return (i,Node(prob, feature, left, right))

    def get_probability(self, features, probability=1):
        probability *= self.probability
        if self.feature is not None:
            if self.feature in features:
                node = self.left
            else:
                node = self.right
            probability = node.get_probability(features, probability)
        return probability


class Solver(gcj.Solver):
    def _solve_one(self):
        tree_lines=self._getintline()
        tree_str=""
        for i in xrange(tree_lines):
            tree_str+=self._getstringline()
            tree_str+=" "
        i,tree=Node.parse(tree_str)
        animal_count = self._getintline()
        answer=""
        for animal_idx in xrange(animal_count):
            answer+='\n'
            features=self._getstringsline()[2:]
            answer+="%.30f" % tree.get_probability(features)
        return answer
