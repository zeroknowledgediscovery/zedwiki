# Fetch the remote 

```
git --fetch all
git reset --hard origin/main #origin/master
```

# rollback commit

Check if something is committed with:

```
git cherry -v
```

If you know you want to use git reset, it still depends what you mean by "uncommit". If all you want to do is undo the act of committing, leaving everything else intact, use:
```
git reset --soft HEAD^
```
If you want to undo the act of committing and everything you'd staged, but leave the work tree (your files intact):
```
git reset HEAD^
```
And if you actually want to completely undo it, throwing away all uncommitted changes, resetting everything to the previous commit (as the original question asked):
```
git reset --hard HEAD^
```