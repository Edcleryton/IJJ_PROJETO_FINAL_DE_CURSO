@echo off
call venv\Scripts\activate

echo Executando testes Behave...
behave

echo Executando testes Newman...
newman run tests\API\API_IJJ.postman_collection.json -e tests\API\API_IJJ.postman_environment.json -r cli,htmlextra --reporter-htmlextra-export reports\Newman_API_Test_Report.html

pause 