# node-neon-usdt

A USDT probe in neon and node

# node-usdt

A project for adding minimum impact User Static Defined Tracing (USDT) to node.js applications on linux.

Currently it's just a proof of concept but I will be tinkering about with it as I get time.

### prereqs

* Install Rust Nightly `$ curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain nightly`

* [Install the bcc-tools](https://github.com/iovisor/bcc/blob/master/INSTALL.md)

* Install [neon](https://github.com/neon-bindings/neon) `$ npm install neon-cli -g`

### run

```
$ npm install
$ npm test
```

In a new console run

```
$ ps aux | grep node
anton    16405  0.4  0.1 543708 29772 pts/1    Sl+  14:55   0:00 node test/test-probe.js
...

$ sudo ./scripts/hello.py 16405
TIME(s)            COMM             PID    MESSAGE
9129.761490000     node        16405   Hello, World!
9132.762761000     node        16405   Hello, World!
9135.765193000     node        16405   Hello, World!
```

To use bpf trace run 
```
$ sudo bpftrace -p 16405 -e 'usdt:::helloprobe { printf("%s\n", comm) ; }'
$ CTL-C 
node
node
node
```