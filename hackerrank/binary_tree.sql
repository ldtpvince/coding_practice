-- Question: https://www.hackerrank.com/challenges/binary-search-tree-1
-- Solution:

-- To categorize the node:
--     - Root node is the one with no parents => BST.P is null
--     - Inner node is the one which has a parent and has some nodes point at them => right join the table with itself to check these condition
--     - Leaf node is basically not root node and not inner node

select distinct b2.N, if(b2.P is null, "Root", 
          if(b1.N is not null, "Inner", "Leaf"))
from bst b1
right join bst b2
on b1.P = b2.N
order by b2.N asc