*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demowebshop.tricentis.com

*** Test Cases ***
LoginTest
    open browser    ${url}  ${browser}
    maximize browser window
#    set selenium speed  3 seconds
    wait until page contains    Register
    LoginToApplication
    close browser

*** Keywords ***
LoginToApplication
    click link  //a[contains(text(),'Register')]
    Select Radio Button     Gender  F
    input text  //input[contains(@name,'FirstName')]    Linh
    input text  //input[contains(@name,'LastName')]   Nguyen
    input text  //div[contains(@class,'inputs')]//input[contains(@name,'Email')]   linh1123@gmail.com

    input text  //input[@name = 'Password']     123
    input text  //input[@name = 'ConfirmPassword']  123
    click element   //input[@name = 'register-button']
