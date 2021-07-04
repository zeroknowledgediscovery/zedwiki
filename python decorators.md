https://towardsdatascience.com/10-fabulous-python-decorators-ab674a732871
## @lru_cache

```
@lru_cache
def factorial(n):
    return n * factorial(n-1) if n else 1
    
```

---

## @dataclass

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


---

## @staticmethod

In some cases, there might be circumstances where one might want to be able to access things that are defined privately as in a more global sense. Sometimes we have functions that are contained within classes that we want to have methodized, and this is exactly what the staticmethod decorator is used for.

Using this decorator, we can make C++ static methods for working with our classes. Normally, methods that are written in the scope of a class will be private to that class, and not accessible unless called as a child. There are circumstances, however, where you might want to take a more functional approach with the way your methods interact with data. Using this decorator, we can create both options without the need for creating more than one function.
class Example:

```   @staticmethod
    def our_func(stuff):
        print(stuff)
```

We also do not need to explicitly provide our class as an argument. The staticmethod decorator takes care of this for us.

