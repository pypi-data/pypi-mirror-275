# `pyyield`: For when you don't know what `time.sleep()` does.

Keeping it at simple as possible, `pyyield` is a simple Python module build from C++ and executes 1 line of code:
``` cpp
::std::this_thread::yield()
```
The only reason for creating this was due to the inconsistencies when using `time.sleep()`,  which until recently was not very well documented to how it's supposed to work when using with 0 or a small float, where some implementations don't seem to do anything on 0 and other implementations round up very small floats.

That is not to say the C++ yield is always the same either, but for that, read more

## Usage:

Example usage, yield from a loop
``` python
from pyyield import pyyield

def workerLoop():
    while performSomeWork():
        pyyield()

```
## Build and install from source:

``` bash
pip install -r requirements.txt
python -m build -o ./dist
pip install ./dist/pyyield*.whl
```

## Tests
``` bash
pip install pytest        
pytest --verbose --log-cli-level=DEBUG
```
The tests are mainly there to make an extremely simple check of performance differences. Please change the tests and play around with it yourself to understand how it performs on the system you want to run it on!

For example, as of writing this, in GitHub Actions, `ubuntu-latest`, `pyyield` does not perform any better than sleep(0) on all python versions tested, printing the info:

>``
>Failed to at speed test: pyyield is not faster than sleep(0)!
>``