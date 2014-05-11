import gcj

class Solver(gcj.Solver):
    def _solve_one(self):
        N = self._getintline()
        sets = self._getstringsline()
        assert len(sets) == N
        letordering = []
        for i in range(26):
            letordering.append([None, None])
        PREV, NEXT = range(2)

        # 1. order letters
        for set in sets:
            prevlet = None
            let = None
            for letter in set:
                prevlet = let
                let = ord(letter) - ord('a')
                if prevlet is not None and prevlet != let:
                    # the pair (let -> prevlet) specifies ordering of letters, check and fail/add
                    prevorder = letordering[prevlet]
                    nextorder = letordering[let]
                    if prevorder[NEXT] is not None and prevorder[NEXT] != let:
                        return 0
                    if nextorder[PREV] is not None and nextorder[PREV] != prevlet:
                        return 0
                    prevorder[NEXT] = let
                    nextorder[PREV] = prevlet
        components = []
        for let in range(26):
            if letordering[let][PREV] is None:
                components.append(let)
        letters = []
        for component in components:
            letter = component
            while letter is not None:
                letters.append(letter)
                letter = letordering[letter][NEXT]
        letterorder = range(26)
        for i, letter in enumerate(letters):
            letterorder[letter] = i
        # letters contains letters in their order, letterorder contains order index of each letter
        # 2. order sets
#        print "Order of letters: %s" % (letterorder,)
 #       print "sets: %s" % (sets,)
        sets = map(lambda set: (ord(set[0]) - ord('a'), ord(set[-1]) - ord('a'),), sets)
  #      print "sets: %s" % (sets,)
        BEGIN, END = range(2)
        sets = sorted(sets, key=lambda set: set[BEGIN]==set[END] and (letterorder[set[BEGIN]] - 0.1) or letterorder[set[BEGIN]])
        prevset = None
        setcomponents = []
        setcomponent = []
        setcount = 26*[0]
        for set in sets:
            #print "Examining set %s" % (set,)
            if set[BEGIN] == set[END]:
                setcount[set[BEGIN]] += 1
            if prevset is not None:
                if letterorder[prevset[END]] > letterorder[set[BEGIN]]:
                    return 0
                elif letterorder[prevset[END]] < letterorder[set[BEGIN]]:
                    setcomponent = []
                    setcomponents.append(setcomponent)
            else:
                # very first set
                setcomponent = []
                setcomponents.append(setcomponent)
            if set[BEGIN] != set[END] or setcount[set[BEGIN]] == 1:
                setcomponent.append(set)
            prevset = set
        # setcomponents contains components of set graph, each component is ordered list of sets
        results = 1
        def modmultiply(initial, factor, mod):
            for f in range(factor):
                initial *= (f+1)
                initial %= mod
            return initial
        for setcomponent in setcomponents:
            for set in setcomponent:
                if set[BEGIN] == set[END]:
                    assert setcount[set[BEGIN]] > 0
                    factor = setcount[set[BEGIN]]
                    results = modmultiply(results, factor, 1000000007)
        results = modmultiply(results, len(setcomponents), 1000000007)
        #print "setcount = %s" % (setcount,)
        #print "setcomponents = %s" % (setcomponents,)
        return results