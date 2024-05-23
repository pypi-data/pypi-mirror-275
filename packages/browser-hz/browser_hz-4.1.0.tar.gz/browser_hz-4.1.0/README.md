# Advertisements Browser

[<img src="https://img.shields.io/badge/development-advertisements_test-purple">](https://github.com/hubzaj/advertisements-test)
[![version](https://img.shields.io/pypi/v/browser-hz)](https://pypi.org/project/browser-hz/)

## Background

The initiation of this project had the goal of gaining a comprehensive understanding of the fundamental mechanisms behind Python packages, their distribution, and the process of releasing them. Poetry, a project and dependency management tool, was employed to achieve this objective. The resulting package was designed for internal use across different Python projects, including [advertisements-test](https://github.com/hubzaj/advertisements-test). Its main purpose is to provide insight into package management intricacies while serving as a valuable resource for a variety of Python projects.

### How to build project

Requirements:

-     Python ^3.11
-     Poetry ^1.5.1

### Working with terminal

1. Install `asdf` with required plugins.

 ```
  > brew install asdf
  > asdf plugin-add python
  > asdf plugin-add poetry
  > asdf install
 ```

### Configuration

Configuration is designed in a way to be controlled by environment variables.

    [BROWSER]

##### Default:

* Browser: `Chrome (without headless)`

#### Supported browsers:

* `CHROME`
* `CHROME_HEADLESS`
* `CHROME_IN_DOCKER` [NOT READY YET]

