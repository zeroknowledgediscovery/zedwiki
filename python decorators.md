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

