# Learning RPC (Remote Procedure Calls) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://github.com/hchiam/learning-rpc/blob/main/LICENSE)

Just one of the things I'm learning. https://github.com/hchiam/learning

ELI5: RPC = ask another computer to do something https://www.reddit.com/r/explainlikeimfive/comments/1rt51c/eli5wth_is_remote_procedure_call_rpc/

RPC vs API vs REST vs GraphQL: https://apisyouwonthate.com/blog/understanding-rpc-rest-and-graphql (REST involves a little more than you might think)

Wiktionary definition: https://en.wiktionary.org/wiki/remote_procedure_call

Wikipedia page for further reading and more links: https://en.wikipedia.org/wiki/Remote_procedure_call

## To actually building something quickly that uses RPC

RPyC ("Remote Python Call"): https://github.com/tomerfiliba-org/rpyc and https://rpyc.readthedocs.io

https://rpyc.readthedocs.io/en/latest/tutorial.html#tutorial

```sh
pip install rpyc
```

### Older way to use RPyC

(RPC server is completely controlled by the client.)

#### Server

`python bin/rpyc_classic.py` didn't seem to work for me, but this did:

```sh
rpyc_classic.py
```

#### Client

```sh
# run python in CLI:
python3

# RPC setup for the client to run code on the server:
import rpyc
connection = rpyc.classic.connect('localhost')
remote_sys = connection.modules.sys
minidom = connection.modules['xml.dom.minidom']

# prints out remote server's command line:
remote_sys.argv

# change current directory of the server process:
connection.modules.os.chdir('..')

# print out something on the server's output:
print('Hello World!', file=connection.modules.sys.stdout)

# read a file on the server:
file = connection.builtins.open('./example-file.txt')
file.read()

# write and read python variables on the server:
connection.execute('a = 1')
connection.eval('a')
connection.eval('a + 2')
# connection.namespace

# write functions and send them to the server:
def square(x):
    print('This will print on the server: ' + str(x) + ' ^ 2 = ' + str(x**2))
    return x**2 # this will return a result to the client
remote_proc_call_square = connection.teleport(square)
remote_proc_call_square(3)
connection.eval('square(4)')
connection.namespace['square'] is remote_proc_call_square # True

connection.execute('import sys')
anonymous_function = lambda: print(sys.version_info)
print_version_on_server = connection.teleport(anonymous_function)
print_version_on_server()

connection.execute('import sys')
def get_version_from_server():
    return sys.version_info
get_version_from_server = connection.teleport(get_version_from_server)
get_version_from_server()
```

### Newer way to use RPyC

(RPC server treated as service provider)

#### Server (newer way)

```sh
python server.py
```

#### Client (newer way)

```sh
python client.py
```

### Much more in the tutorial!

https://rpyc.readthedocs.io/en/latest/tutorial.html

Netrefs (network references)? Exceptions? Callbacks between client/server? Async operation and events?
