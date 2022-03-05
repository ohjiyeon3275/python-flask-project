

---
###basic concept of `__name__`


in justPrintName.py
```
print(__name__)
```
console >> 
```
__main__
```


---
### import concept 0f `__name__`

in firstFile.py

```

if __name__ == '__main__':
    print "run directly"
else:
    print "run from import"
```

in secondFile.py

```
import firstFile

print "print module name: {}".format(__name__)
```


and console
```
run from import
print module name: __main__
```

