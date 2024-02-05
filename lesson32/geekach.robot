*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${start_url}    https://geekach.com.ua/
${browser}    gc
${title_text}   Результати пошуку «Війна Персня» - Настільні ігри | Купити настільну гру в Україні, Києві за низькою ціною | інтернет магазин Geekach Shop

*** Test Cases ***
Valid Search
    Open Browser To Main Page
    Type In Search Text    Війна Персня
    Time To Sleep
    Submit Search
    Result Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Main Page
    Open Browser    ${start_url}    ${browser}

Type In Search Text
    [Arguments]    ${searchtext}
    Input Text    xpath://input[@placeholder="пошук товарів"]   Війна Персня

Time To Sleep
    Sleep    3

Submit Search
    Click Button    xpath://button[@type="submit"]

Result Page Should Be Open
    Title Should Be    ${title_text}



