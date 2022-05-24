# SolidProxy

> Note: to benefit from this code you will need to acquire your own instance of SolidWorks. It was (very lightly) tested on SolidWorks Student Edition 2021-2022. Of course, SolidWorks (and thus this software) is Windows only.

# Motivation

SolidWorks has a really good API ([link](https://help.solidworks.com/2020/english/api/sldworksapiprogguide/Welcome.htm)). Unfortunately it is intended primarily for `.NET` and associated programs. As these are comparatively less popular than something like `python` there is considerably less (free) libraries for them. 

The goal here is a proof of concept connecting to SolidWorks via `python3.x`. This is possible for two reasons:

1. The SolidWorks API works by exposing its internals to the Windows COM (Component Object Model)
2. The python library `pywin32` supports connecting to arbitrary COM objects through Windows API calls.

These two together give the ability to work with the SolidWorks API in python.

It works. And it doesn't seem like that bad of an idea. 

This repo contains the code from a month of on and off tinkering. More aptly, it contains a minimal sample set of code, which has been cleaned up to a decently high standard. There is alot you can do, and some very interesting topics. None of this code is included, but it should be trivial to implement:

* Generating BOMs for an assembly
* Automatically loading a file an running an interference detection
* Loading the model and rendering automatically
* Running multiple different simulations with varying parameters

All of these are possible in some capacity within SolidWorks already (either as a macro, command, and/or the task scheduler). However, the exciting part is that this can be done in python, which allows you access to practically anything you could want to integrate:

* A CI/CD pipeline for solid models: whenever an engineer makes a change, a suite of automated tests run on the part and can return a go/no-go decision. 
* Doing collision detection for a large assembly quickly through some Map-Reduce style paradigm across multiple machines
* Generating configurations and renders dynamically and showing them on a website in near-real time.

Likewise, this gives you (indirect) access to the underlying SolidWorks geometry/rendering/display engine. Perhaps that is an interesting use case for someone. Perhaps an overly complex (and expensive) graphing calculator.

# Structure 

Since python is dynamically typed and Windows COM is not builtin to python, there are alot of files which provide the proper type conversions to/from the COM value. The naming, function signatures, data members, etc. is generally taken straight from the SolidWorks API documentation. Where the signatures differ generally has to do with the SolidWorks API using pass-by-reference values being used to return information from SolidWorks to the caller. These are changed for tuples. See `ISldWorks::OpenDoc6()`. The other major change is that everything is a method inside these classes.

The files are laid out as follows:

* `SolidProxy/` - the standalone library. Would be published to `pip` if I wanted to support this long term (I don't).
  * `sldworks/` - the vast majority of SolidWork's features are accessed through this. These classed are supposed to be 1:1 translations from COM to python and thus do no processing.
    * `ISldWorks.py` - the base entry for the SolidWorks instance. Generally, this is the entry point.
  * `swconst/`- enums for constant values. These are int enums and support a `what()` function which returns the SolidWorks API documentation about the item (when not provided, just returns the name)
  * `bootstrap.py` - a file with functions for bootstrapping the program, namely `GetOrStartSWInst`. This will connect to a running instance or start one (without an interface).
* `TestFiles/` - a small handful of SolidWorks `.sldprt` files to demonstrate the functionality.
* `ex_test_*.py`- roughly test cases, but not integrated with any testing frame work. Demonstrate minimum functionality and thats about it.  

# Future Work

There is not much algorithmically to do here. Now it is a matter of translating the SolidWorks API (and ideally developing test cases/coverage.)

Some ideas:

* Most of this comes fom webpages on the internet (alternatively, it is included in SolidWorks). Can a script generate the classes automatically
* The enums can be checked against their value in C# (generate the names from html, generate C# to get the values based on name, create python code from that)

# Contributing

Until I come up with a use case, I'm not planning on developing new components. If someone wants to take this over, feel free to fork or open a pull request. 

> Note: Not affiliated, supported, or endorsed by SolidWorks, Dassault Systemes, or related entity
