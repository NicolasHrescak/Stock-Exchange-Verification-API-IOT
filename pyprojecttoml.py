[tool.poetry]
name = "python-template"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.10.0,<3.12"
alpha-vantage = "^2.3.1"
pandas = "^2.2.2"
requests = "^2.32.3"

[tool.pyright]
# https://github.com/microsoft/pyright/blob/main/docs/configuration.md
useLibraryCodeForTypes = true
exclude = [".cache"]

[tool.ruff]
# https://beta.ruff.rs/docs/configuration/
select = ['E', 'W', 'F', 'I', 'B', 'C4', 'ARG', 'SIM']
ignore = ['W291', 'W292', 'W293']

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"