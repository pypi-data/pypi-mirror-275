Hello Python enthusiasts!

I’m excited to introduce [Rootify](https://github.com/jimmys-code/rootify), a simple yet powerful Python package that automatically sets your working directory to the project root. This tool is perfect for developers who often struggle with relative paths and want a consistent environment for running scripts.

### Why Rootify?

One of the common challenges in Python development is ensuring that scripts run correctly regardless of their location within the project structure. Often, scripts have to be executed from specific directories to avoid path issues, which can complicate testing and development. Rootify solves this problem by automatically setting the working directory to the project root, allowing your Python scripts to run the same way regardless of where they are located within the project.

### Benefits

- **Ease of Use**: Just import Rootify, and it will set your working directory to the project root.
- **Flexibility**: Works with any marker (e.g., `.git`). This means you can move your Python scripts to any folder within your project, and they will still run correctly.
- **Consistency**: Ensures your scripts run from the project root, making imports and file paths more predictable.
- **Improved Testing**: Allows you to easily test modules from adjacent folders or parent folders without worrying about path issues.

### Installation

You can install Rootify from PyPI:

```sh
pip install rootify
```