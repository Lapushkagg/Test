# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.


Для запуска тестов и формирования отсчтов необходимо:
    Ввести в консоль команду pytest --alluredir allure-result 

Для открытие отсчета во вкладки браузера необходимо:
    Ввести в консоль команду allure serve allure-result