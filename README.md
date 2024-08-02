<h1> Financial Overview </h1>

Categorisation and visualistion of financial spendings (based on Santander monthly bank statements)


<h2> src </h2>
Contains the source files with functoins

- <h4> Additional Functions </h4>
    File for smaller functions used by other functions

- <h4> Get Expense Categories </h4>
    Function to create dictionary of expense categories from csv file.
    
    - **Input**: csv file, expense categories and key words
    - **Output**: dictionary

-  <h4> Simplify Statements  </h4>
    Function to categorise expenses using categories from csv file.
    
    - **Input**: Excel spreadsheet, bank statement
    - **Ouput**: Excel spreadsheet, simplified bank statement

<h2> Tests </h2>
Contains the unittest script and test files

- <h4> Simplify Test </h4>
    Unittest for GetExpenseCategory and SimplifyStatement functions
