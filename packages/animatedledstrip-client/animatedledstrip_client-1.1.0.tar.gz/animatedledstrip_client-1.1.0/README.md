[![Build Status](https://travis-ci.com/AnimatedLEDStrip/client-python.svg?branch=master)](https://travis-ci.com/AnimatedLEDStrip/client-python)
[![PyPI](https://img.shields.io/pypi/v/animatedledstrip-client.svg)](https://pypi.python.org/pypi/animatedledstrip-client)
[![codecov](https://codecov.io/gh/AnimatedLEDStrip/client-python/branch/master/graph/badge.svg)](https://codecov.io/gh/AnimatedLEDStrip/client-python)

# AnimatedLEDStrip Client Library for Python

This library allows a Python 3 client to communicate with an AnimatedLEDStrip server.

## Adding the Library to a Project

The library is available via pip:

```bash
pip3 install animatedledstrip-client
```

## Creating an `AnimationSender`

An `ALSHttpClient` is created with `ALSHttpClient(ip_address)`.

```python
from animatedledstrip import ALSHttpClient

sender = ALSHttpClient('10.0.0.254')
```

## Communicating with the Server

This library follows the conventions laid out for [AnimatedLEDStrip client libraries](https://animatedledstrip.github.io/clients/libraries), with the following modifications:

- Function names and class variables are in snake case to follow Python style conventions
- `get_supported_animations_dict` is provided as an alias for `get_supported_animations_map`
- `get_sections_dict` is provided as an alias for `get_sections_map`
