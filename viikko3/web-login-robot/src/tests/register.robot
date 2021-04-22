*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  rillipaa
    Set Password  crybaby92
    Set Password Confirmation  crybaby92
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ri
    Set Password  crybaby92
    Set Password Confirmation  crybaby92
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  rillipaa
    Set Password  crybab9
    Set Password Confirmation  crybab9
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  rillipaa
    Set Password  crybaby92
    Set Password Confirmation  crybaby96
    Submit Credentials
    Register Should Fail With Message  Invalid password confirmation

Login After Succesful Registration
    Set Username  jorma
    Set Password  jorma1234
    Set Password Confirmation  jorma1234
    Submit Credentials
    Go To Login Page
    Set Username  jorma
    Set Password  jorma1234
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ja
    Set Password  jarmo1234
    Set Password Confirmation  jarmo1234
    Submit Credentials
    Go To Login Page
    Set Username  ja
    Set Password  jarmo1234
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}