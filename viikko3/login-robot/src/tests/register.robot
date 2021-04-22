*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jorma  jorma123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username and Valid Password
    Input Credentials  jo  jorma888
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  rillipaa  cryba88
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  rillipaa  crybabyyy
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123