<div align="center">
  <img src="https://media.discordapp.net/attachments/972467177624072263/972555155822239824/logo4.png?width=250&height=250" />
  <br/>
  <b>A bunch of well crafted PyGame examples.</b>
  <br/>
  <br/>
	<a href="https://github.com/Matiiss/pygame_examples/actions/workflows/lint.yml"><img src="https://img.shields.io/github/workflow/status/Matiiss/pygame_examples/Run%20pylint%20and%20black"></a>  
  <a href="https://discord.gg/DCGyWedkde"><img src="https://img.shields.io/discord/972445332476665866"/></a>
	<a href="https://github.com/Matiiss/pygame_examples/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Matiiss/pygame_examples"></a>
	<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-brightgreen"></a>
  
</div>


# Pygame [Examples](https://github.com/Matiiss/pygame_examples/tree/main/pgex/examples)
Just a bunch of [pygame](https://github.com/pygame/pygame) examples, feel free to use them

Most examples should be WASM compatible meaning that they can be run in the browser (after being properly packaged)


# Installation 
## By cloning the repository 
  - We recommend reading our [getting a development environment setup](https://github.com/Matiiss/pygame_examples/blob/main/SETUP.md)
## Through pip
  - `pip install git+https://github.com/Matiiss/pygame_examples`
## Through [releases](https://github.com/Matiiss/pygame_examples/releases)
  - Coming soon.

# Usage
  - These are primarily meant to be used to read the source code, so going through our [examples](https://github.com/Matiiss/pygame_examples/tree/main/pgex/examples) should allow you to get an idea on how we recommend writing your code.
  - Our examples are also compatible with WASM builds, follow contentions, reviewed by experienced pygame users, and follow an [ECS](https://en.wikipedia.org/wiki/Entity_component_system) or [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) paradigm for the most part. Which means that following our example(no pun intended), is meant to allow you to write *better* Python code with the `pygame` framework!
  - If you want to try running our examples, and want to avoid the tedious process of setting up a development environment, we recommend using `pip install git+https://github.com/Matiiss/pygame_examples` if you have Python `3.7+` installed. This will also add `pgex` to the PATH.
  - You can use the `pgex` CLI interface to get started with launching examples on desktop or browser:
  - You can start by running `pgex --help` which should list the available commands. 
	  - `pgex run` can be used to run any of the available examples
	    `pgex run -n "example_name"` can be used to directly run the given example
	    `pgex run --web` can be used to run the example on the browser. All examples are WASM compatible.
	  - `pgex view` can be used to view the main file for the example on [github.dev](https://github.dev/Matiiss/pygame_examples)
	    `pgex view -n "example_name"` can be used to run a specific example.

# Contributing
  - We recommend reading our [contributing guidelines](https://github.com/Matiiss/pygame_examples/blob/main/CONTRIBUTING.md)
