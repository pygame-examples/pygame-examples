# Contributing to `pgex`
  - Firstly, thank you for wanting to improve `pgex`! The sentiment already means a lot to us.
  - There are many means through which one can make contributions, suggesting ideas, reporting bugs, fixing typos, improving our wording in files like these, chatting in our discord server, besides writing code.
  - Code based contributions are also of course greatly appreciated, but do keep in mind -- You are setting an example, literally, it has to be good >:). We have no intentions of scaring you! Setting examples are important, yes, but as long as they follow some basic steps and regulations, we are fine with it. Please continue reading to make sure you have all the steps done!

# Setting up a development environment
  - Setting up the right environment to write code in is crucial, simple things like accidentally using Python 3.10 features that don't exist in 3.7 yet can cause a lot of failing code. We recommend reading up on our [setting a development environment](https://github.com/Matiiss/pygame_examples/blob/main/SETUP.md)


# Opening an issue
  - Found a bug in the application? Something that could be improved? Something that you wish to be added? [Issues](https://github.com/Matiiss/pygame_examples/issues) are the place for this! 
## Basic guidelines
  - Please keep the title as short as possible, while still being relevant to the issue.
  - If it is a bug report, a screen shot would be greatly appreciated.
  - If you already have a fix that you are working on, or you would like to work on it, please do mention it. We can assign you if it gets approved.
## Making an example suggestion
  - Opening an issue is fine, but if you just want to discuss your idea, or get it out there, we have a [discord server](https://discord.gg/DCGyWedkde) for this. 
  - Try to make example suggestions that highlight things that would likely want to be done. Examples such as a very specific dialogue system, or a coin incrementation system, might be used in games, but are probably not things that are seeked out for specifically. 
  - Avoid making huge example suggestions! Such as suggesting to remake Zelda or Doom in pygame. These are considered too large, and might be better off in separate repositories of their own.
  - Try to be as specific as possible when making an example suggestion. Being too broad can cause confusion, and may also not always be what you had in mind.
## Making a bug report 
  - Make sure you are running the latest version of `pgex` before reporting -- it may have already been fixed. If you *are* running the latest version, and the bug persists, do not hesitate to make the bug report. 

# Making a Pull Request
  - Alright, here is where we get into the nitty-gritty part of it. 
  - We recommend using version control to make branches, and push them to your fork.
## Basic guidelines
  - It is fine if your PR(Pull Request) is really small. Even changing a single character, to fix a typo, is a relevant change and we would appreciate it! No PR is too small.
  - If the change is small, directly making a PR would be a good idea. Even if it doesn't get approved, not a lot of effort would have been wasted.
  - If the change is slightly larger, making an issue first is recommended, it isn't very likely to get approved and merged into the `main` branch if it is a large PR out of the blue.
  - Please only work on issues you were assigned to; You can do this by making a comment on the issue you would like to work on. If not, someone may have been assiged in the meantime and your effort would be wasted, which is something we would like to avoid. 
  - Link the relevant issue in your PR description, so that it shows up as mentioned in the relevant issue.
  - Please do not attempt to fix things outside of the PR's scope. This could cause easily-avoidable merge conflicts, for example if another person was already assigned and working on an issue relevant to it, but fixed it in a different way. If you see typos, but this wasn't within the scope of your PR, please make a separate issue for this.
## Version control and the command line interface
  - The `git` command line interface is surpringly easy to use. Yes, really.
  - [Setting up a local development environment](https://github.com/Matiiss/pygame_examples/blob/main/SETUP.md) first is recommended.
  - Now that we have a local environment setup, let's start writing some code.
  - The first step to fixing an issue, is to make a branch for it:
  	- `git checkout -b feature/issue-n` replace `n` with the issue number.
  - Make your relevant changes here, please [use a consistent coding style](https://github.com/Matiiss/pygame_examples/blob/main/SETUP.md#use-a-consistent-coding-style)
  - After you are done with making your changes, run these two commands:
  	- `git add .`
  	- `git commit -m "short description explaining the changes you made"`
  - Or:
  	- `git commit -am "short description explaining the changes you made"`
  - Now you can push the code to your fork:
  	- `git push origin feature/issue-n`
  - Go to your fork, and you should see a `Compare and create a pull request` option.
  <img src="https://i.ytimg.com/vi/rgbCcBNZcdQ/maxresdefault.jpg"/>
  
  - Click on it, and create a pull request. Merge conflicts will be solved by maintainers if necessary. 
  - And there! You just made your first pull request to `pgex`! Now you can wait patiently for it to be reviewd, and hope it gets merged 🤞.


# Use a consistent coding style 
  - Before making a commit, make sure to run `before_commit.py` at the root of your project directory. This will reformat the files, 
sort the imports, and check if you have added license header doc-strings, if not it will do so. 
  - This may not however, change your code completely to follow [PEP8](https://peps.python.org/pep-0008/). Following it is mandatory. 
