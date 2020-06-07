

## grid with constrained directions

## use something like

r,c = 0,0


## each step in bfs/dfs explore happens this way.
for row,col in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
    ## for the neighboring nodes
    pass

## for visited mark, same grid can be used.
## Example: No. of Islands
