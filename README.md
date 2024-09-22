
# <p align="center">Simplelog</p>
  
This is a simple package that allows for logging-to-stdout functionality. Basically a tool for people that want to log with prints, but better.

## 🧐 Features    
- Configurable styles
- Simple setup
- Lightweight


## 🧑🏻‍💻 Usage
```py
from simplelog import Logger

my_logger = Logger()

my_logger.info("Let's check that math still works")
my_logger.info(f"2 + 2 = {2+2}")
if 2 + 2 != 4:
    my_logger.fatal("Math is corrupted! May god help us")
```