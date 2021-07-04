https://towardsdatascience.com/10-fabulous-python-decorators-ab674a732871

```
@lru_cache
def factorial(n):
    return n * factorial(n-1) if n else 1
    
```


@dataclass
One of the best decorators I utilize all the time in order to save time when writing classes is the dataclass decorator. This decorator can be used to quickly write common standard methods that are typically found in the classes that we write.

```
@dataclass
class Food:
    name: str
    unit_price: float
    stock: int = 0
        
    def stock_value(self) -> float:
        return(self.stock * self.unit_price)
        
```

Now we can create a new class by calling this constructor, like so:

`carrot = Food("Carrot", .45, 25)
`

https://github.com/emmettgb/Emmetts-DS-NoteBooks/blob/master/Python3/Python%20DataClasses.ipynb

A very valid advantage to using this decorator is also that it avoids a lot of clutter in classes. The example of assigning each individual value inside of a Python class to a member variable is actually incredibly common. There is not really a great reason to write an entire function with a ridiculous amount of `self.x = x` when this is entirely avoidable by simply using a decorator. This can also serve to make a class a lot more readable.
