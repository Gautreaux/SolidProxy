# SolidProxy

> I wanted the name `PYSW` but that already exists on `pip`. Very open to new name suggestions.

> Note: to benefit from this code you will need to acquire your own instance of SolidWorks. It was (very lightly) tested on SolidWorks Student Edition 2021-2022. Of course, SolidWorks (and thus this software) is Windows only.

# Motivation

SolidWorks has a really good API ([link](https://help.solidworks.com/2020/english/api/sldworksapiprogguide/Welcome.htm)). Unfortunately it is intended primarily for `.NET` and associated programs. As these are comparatively less popular than something like `Python3` there is considerably less (free) libraries for them. 

> NOTE: code was developed and tested on `Python3.9` on `CPython` on `Windows 10`. There is no known reason it won't work on other versions, but it is untested. Also, its Windows only because SolidWorks is Windows only.

The goal here is a proof of concept connecting to SolidWorks via `Python3.x`. This is possible for two reasons:

1. The SolidWorks API works by exposing its internals to the Windows COM (Component Object Model)
2. The Python3.x library `pywin32` supports connecting to arbitrary COM objects through Windows API calls.

These two together give the ability to work with the SolidWorks API in Python3.

It works. And it doesn't seem like that bad of an idea. 

This repo contains the code from a month-plus of on and off tinkering. More aptly, it contains a minimal sample set of code, which has been cleaned up to a decently polished state. There is alot you can do, and some very interesting topics. None of this code is included, but it should be trivial to implement:

* Generating BOMs for an assembly
* Automatically loading a file an running an interference detection
* Loading the model and rendering automatically
* Running multiple different simulations with varying parameters

All of these are possible in some capacity within SolidWorks already (either as a macro, command, and/or the task scheduler). However, the exciting part is that this can be done in Python3, which allows you access to practically anything you could want to integrate:

* A CI/CD pipeline for solid models: whenever an engineer makes a change, a suite of automated tests run on the part and can return a go/no-go decision. 
* Doing collision detection for a large assembly quickly through some Map-Reduce style paradigm across multiple machines (`treat subassemblies as components` but also run collision detection on the subassembly in another instance)
* Generating configurations and renders dynamically and showing them on a website in near-real time.

Likewise, this gives you (indirect) access to the underlying SolidWorks computational geometry/rendering/display engine. Perhaps that is an interesting use case for someone. Perhaps an overly complex (and expensive) graphing calculator.

# Resources

The following resources may be of interest:

* When SolidWorks is installed, the api details are located at `C:/Program Files/SOLIDWORKS Corp/SOLIDWORKS/api`
  * The `.chm` files are compressed html help files (its a Windows thing)
  * `redist/` contains the `.dll` files for linking your program into SolidWorks. They are not used in the Python3 implementation, but may provide a cross reference if using C# or C++
* The help files are also online at [link](https://help.solidworks.com/2021/english/api/SWHelp_List.html)
* O'Reilly article on PythonCOM [link](https://www.oreilly.com/library/view/python-programming-on/1565926218/ch12s03s06.html)

# File Structure 

Since Python3 is dynamically typed and Windows COM is not builtin to Python3, there is some boiler plate needed to make all parties happy. Generally, the SolidProxy files are simply a translation and type hints for converting between Python3 and COM calls. The naming, function signatures, data members, comments, etc. is generally taken straight from the SolidWorks API documentation. Where the signatures differ generally has to do with the SolidWorks API using pass-by-reference values being used to return information from SolidWorks to the caller. These are changed to return tuples. For an example, see `ISldWorks::OpenDoc6()`. The other major change is that everything is a method inside these classes.

The files are laid out as follows:

* `SolidProxy/` - the standalone library. Would be published to `pip` if I wanted to support this long term (I don't).
  * `sldworks/` - the vast majority of SolidWork's features are accessed through this. These classed are supposed to be 1:1 translations from COM to Python3 and thus do no processing.
    * `ISldWorks.py` - the base entry for the SolidWorks instance. Generally, this is the entry point to get references to anything in SolidWorks. To get an object, see `bootstrap.py`
  * `swconst/`- enums for constant values. These are int enums and support a `what()` function which returns the SolidWorks API documentation about the item (when not provided, just returns the name)
  * `bootstrap.py` - a file with functions for bootstrapping the program, namely `GetOrStartSWInst`. This will connect to a running instance or start one (without an interface).
* `TestFiles/` - a small handful of SolidWorks `.sldprt` files to demonstrate the functionality.
* `ex_test_*.py`- roughly test cases, but not integrated with any testing frame work. Demonstrate minimum functionality and thats about it.  
* `ex_backend/` - contains an example Django React REST webapp for displaying SolidWorks data in the web-browser. More detail is in `ex_backend/README.md`

The methods in all interfaces do not provide default values. This is in keeping with the organization of the SoldWorks API. Generally, the SolidWorks APIs will need to be wrapped to a particular use case. For example, you can fetch an `IPartDoc` (as a pointer to a COM Object). Then this object should be managed in a way such that the references is held in Python; there is no need to re-fetch it every time (this depends on the object's lifecycle. For example parts are good until the document is closed whereas a selection group may be valid only until the selection ends). Likewise, the `IPartDoc` should probably be wrapped with functions that handle most of the boiler plate of the actual SolidWorks call. For example, `ISldWorks::OpenDoc6` takes 4 parameters but only one, the file name, is probably necessary in most use cases. See `ex_utils.py` and `ex_backend/` for examples.

# Future Work

There is not much algorithmically to do here. Now it is a matter of translating the SolidWorks API (and ideally developing test cases/coverage.)

Some ideas:

* Most of the work is translating C# to COM. The format comes fom webpages on the internet (alternatively, it is included in SolidWorks). Can a script generate the classes automatically? 
  * Can you used the `.dll` and/or Visual Studio (Code?) Intellisense to generate function names and signatures?
* Alternatively, can you parse out structure and comments to make the docs easier to navigate through. Examples:
  * You almost always want the interface members page and it is always 2+ clicks deep
  * Google doesn't really index these pages (they probably arent that popular) and it is often confusing to find what you need. And if you do it may be for a past version.
* The enums can be checked against their value in C#. Sample workflow:
  * Parse the enums from html docs
  * Generate C# to get the values based on name
  * Compile and test C# to validate values vs parsed values
    * Bonus if you can easily check for enum values not listed in html
  * Create Python3 code from that
* Proper testing / test cases
* Register an Addin with a callback in Python
* Use CPython (C++) or IronPython (C#) to interface with the officially supported DLLs. 

# Contributing

Until I come up with a use case, I'm not planning on developing new components. If someone wants to take this over, feel free to fork or open a pull request. 

> Note: Not affiliated, supported, or endorsed by SolidWorks, Dassault Systemes, or related entity
