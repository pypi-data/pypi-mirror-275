# SingleStore-demo - S2Generate
## Generation of a simple datasource for SingleStore

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://www.python.org/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/SDB-Support/Deployment/tree/main/singlestore_demo)

This python script creates a database and fills it up with data to perform several types of testing on a SingleStore DB.

- Easy to use. Using pip to install
- Fast. Creates the database and data with several K of data in a couple minutes.

## Features

- Can change the number of records to be inserted.
- Can change the database schema. Limited.

## Tech

SingleStore-demo uses a number of open source projects to work properly:

- [Python] - HTML enhanced for web apps!
- [singlestoredb-python] - SingleStore DB Python connector.
- [numpy] - NumPy is the fundamental package for scientific computing with Python.
- [mimesis] - Mimesis is a high-performance fake data generator for Python

And of course SingleStore-demo itself is open source [s2generator]
 on GitHub.

## Installation

SingleStore-demo requires Python v3.10+ and Pip v22.0+ to run.

Check the current version of installed Python and Pip by running:

```
$ python3 -V
Python 3.10.6
$ pip -V
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```

To install the script you need to run Pip, all the dependencies will be installed using a single command.

```bash
$ pip install singlestore-demo
Defaulting to user installation because normal site-packages is not writeable
Collecting singlestore-demo
  Using cached singlestore_demo-1.0.5-py3-none-any.whl (8.0 kB)
Collecting numpy>=1.24.1
  Using cached numpy-1.24.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.3 MB)
Collecting mimesis>=4.1.3
  Using cached mimesis-7.0.0-py3-none-any.whl (4.4 MB)
Collecting singlestoredb>=0.5.3
  Using cached singlestoredb-0.5.3-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (213 kB)
Requirement already satisfied: PyJWT in /usr/lib/python3/dist-packages (from singlestoredb>=0.5.3->singlestore-demo) (2.3.0)
Requirement already satisfied: wheel in /usr/lib/python3/dist-packages (from singlestoredb>=0.5.3->singlestore-demo) (0.37.1)
Requirement already satisfied: sqlparams in ./.local/lib/python3.10/site-packages (from singlestoredb>=0.5.3->singlestore-demo) (5.0.0)
Requirement already satisfied: build in ./.local/lib/python3.10/site-packages (from singlestoredb>=0.5.3->singlestore-demo) (0.9.0)
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (from singlestoredb>=0.5.3->singlestore-demo) (2.25.1)
Requirement already satisfied: packaging>=19.0 in ./.local/lib/python3.10/site-packages (from build->singlestoredb>=0.5.3->singlestore-demo) (23.0)
Requirement already satisfied: tomli>=1.0.0 in ./.local/lib/python3.10/site-packages (from build->singlestoredb>=0.5.3->singlestore-demo) (2.0.1)
Requirement already satisfied: pep517>=0.9.1 in ./.local/lib/python3.10/site-packages (from build->singlestoredb>=0.5.3->singlestore-demo) (0.13.0)
Installing collected packages: numpy, mimesis, singlestoredb, singlestore-demo
Successfully installed mimesis-7.0.0 numpy-1.24.1 singlestore-demo-1.0.4 singlestoredb-0.5.3
```

## Run

To run `s2generate` command

## Arguments

| Argument | Default Value | Description|
|----------|---------------|------------|
|`--host`|localhost|The hostname of the SingleStoreDB node to connect to|
|`--port`|3306|The port of the SingleStoreDB node to connect to|
|`--username`|root|The username of the SingleStoreDB user with permissions to create a database.|
|`--password`||The password of the SingleStoreDB user specified.|
|`--rows-per-insert`|10000|The number of rows to send to SingleStore at once|
|`-total-orders`|10|The total number of orders * rows per insert|
|`--total-suppliers`|1|The total number of suppliers * rows per insert|
|`--total-parts`|20|The total number of parts * rows per insert|
|`--total-parts-suppliers`|80|The total number of parts on suppliers * rows per insert|
|`--total-customers`|15|The total number of customers * rows per insert|
|`--lineitem-max`|10|The Maximum number of line items per order|
|`--lineitem-min`|4|The Minimum number of line items per order|
|`--only-orders`||Only adds a new orders to the database. Doesn't drop the database|
|`--schema`||The database schema file.|

To add more orders only you can run

```
s2generate --only-orders
```

## Development

Want to contribute, great...

Currently we are accepting ideas for more tables or complex types to improve the provided database.

## License

MIT License

Copyright (c) 2023 singlestore_demo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [singlestoredb-python]: <https://github.com/singlestore-labs/singlestoredb-python>
   [numpy]: <https://github.com/numpy/numpy>
   [mimesis]: <https://github.com/lk-geimfari/mimesis>
   [s2generator]: https://github.com/SDB-Support/Deployment/tree/main/singlestore_demo

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
