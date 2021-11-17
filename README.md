# Behave + Allure

Start the grid:
```sh
$ cd selenium_grid
$ sudo docker-compose up -d
```

Running the scenarios:
```sh
$ behave -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features
```

Serving the report
```sh
$ allure serve allure_result_folder/
```