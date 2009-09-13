# to reproduce, please download my GCJ framework http://github.com/dusek/gcj
# and place this file as problems/2009/round1C/A.py and run
# bin/solve.sh 2009.round1C A <your input file> > <your output file>
# I had problems uploading ZIP archive of the linked repository as source code
# to GCJ
import gcj

class Solver(gcj.Solver):
    def _solve_one(self):
        symbol_to_digit={}
        number=self._getstringline()
        highest_digit=-1
        for symbol in number:
            if highest_digit==-1:
                new_highest_digit=1
            elif highest_digit==1:
                new_highest_digit=0
            elif highest_digit==0:
                new_highest_digit=2
            else:
                new_highest_digit=highest_digit+1
            current_digit=symbol_to_digit.setdefault(symbol,new_highest_digit)
            if current_digit==new_highest_digit:
                highest_digit=new_highest_digit
        if highest_digit==0:
            highest_digit=1
        base=highest_digit+1
        assert(base>=2)
        number_value=0
        for symbol in number:
            number_value*=base
            number_value+=symbol_to_digit[symbol]
        return number_value
