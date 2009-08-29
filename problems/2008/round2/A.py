import gcj

invert=[1,0]
OR=0
AND=1

traced_pos=3

class Solver(gcj.Solver):
    def _solve_one(self):
        M,V = self._getintsline()
        self.tree=[None] # we are numbering from 1
        i=0
        for i in range(M):
            self.tree.append(map(int, self._getstringline().rstrip().split(' ')))
        min_changes=self._changes(1, V)
        if min_changes==-1:
            return "IMPOSSIBLE"
        else:
            return str(min_changes)

    def _changes_internal(self, pos, gate, desired_value):
        changes_left=self._changes(2*pos, desired_value)
        changes_right=self._changes(2*pos+1, desired_value)
        #if pos==traced_pos:
        #    print "Changes with gate %d: l,r = %d, %d" % (gate, changes_left, changes_right)
        if gate+desired_value!=1:
            # 0, AND    or    1, OR
            # both values must be same
            cur_changes=min(changes_left, changes_right)
            if cur_changes!=-1:
                cur_changes=changes_left+changes_right
        else:
            # either one can be successful
            if changes_left==-1 or changes_right==-1:
                cur_changes=max(changes_left,changes_right)
            else:
                cur_changes=min(changes_left,changes_right)
        return cur_changes

    def _changes(self, pos, desired_value):
        cur_node=self.tree[pos]
        t=len(cur_node)
        if t==1:
            # this is terminal node, containing fixed value that can't be changed
            if cur_node[0]==desired_value:
                return 0
            else:
                return -1
        else:
            # internal node
            gate, changeable=cur_node
            cur_changes=self._changes_internal(pos, gate, desired_value)
            if not changeable:
                return cur_changes
            inverted_gate=invert[gate]
            inverted_changes=self._changes_internal(pos, inverted_gate, desired_value)
            if inverted_changes!=-1:
                inverted_changes+=1
            if cur_changes==-1:
                return inverted_changes
            elif inverted_changes==-1:
                return cur_changes
            else:
                return min(cur_changes, inverted_changes)
