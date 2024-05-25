# About

-	Do you have a [SUAI](https://pro.guap.ru) student profile?
-	Are you tired of entering your password every day, only to check your reports?
-	Do you want to automate the process of retrieving reports' status?

Then fear not: the `suai-observer` is for you.

# Features

-	A library for scraping the [SUAI profile](https://pro.guap.ru/inside/profile) website
-	An executable to output reports in JSON format
-	A TOML config file for an executable
-	Caches cookies to a file like a browser

# Install

```sh
pip install suai-observer
```

Or, clone this repository and do:

```sh
pip install .
```

# Usage

Create a config file `config.toml` like [this example](example-config.toml).
Make sure to provide your valid login data.
Then, run:

```sh
suai-observer config.toml
```

Make sure to provide an argument pointing to a config file.
