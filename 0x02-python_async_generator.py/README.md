# 0x02-python_async_comprehension

### [0-async_generator.py](./0-async_generator.py)
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait
1 second, then yield a random number between 0 and 10. Use the
random module.

### [1-async_comprehension.py](./1-async_comprehension.py)
Import async_generator from the previous task and then write a
coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random
numbers.
