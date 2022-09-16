#!/bin/bash
docker build . -t circuitpython
docker run -it --rm -v $(PWD)/build:/root/build circuitpython
