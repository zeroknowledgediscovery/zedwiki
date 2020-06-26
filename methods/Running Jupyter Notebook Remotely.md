+ In remote host, open the terminal, change directory to where you have your notebooks and type:
```
jupyter notebook --no-browser --port=8889
```

+ In your local computer:

```
ssh -N -f -L localhost:8888:localhost:8889 username@your_remote_host_name
```
+ Now open web browser 
```
localhost:8888
```

