import gcj

class Solver(gcj.Solver):
    def _solve_one(self):
        N = self._getintline()
        words = [self._getstringline() for i in range(N)]
        def pattern(word):
            curletter = None
            currun = 0
            ret = []
            for letter in word:
                if curletter != letter:
                    if curletter is not None:
                        ret.append(currun)
                    currun = 1
                    curletter = letter
                else:
                    currun += 1
            ret.append(currun)
            return ret
        patterns = map(pattern, words)
        #print patterns
        lengths = map(len, patterns)
        if min(lengths) != max(lengths):
            return "Fegla Won"
        length = lengths[0]
        steps = 0
        for i in range(length):
            positions = [pattern[i] for pattern in patterns]
            avg = int(round(float(sum(positions))/len(positions)))
            #print "Position %d: avg=%d" % (i, avg,)
            for position in positions:
                steps += abs(position - avg)
        return steps