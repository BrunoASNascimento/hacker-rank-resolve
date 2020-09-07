SELECT N,
if(P is null, 'Root',
  if(N in (SELECT P FROM BST),'Inner','Leaf')
  )

from BST order by N
