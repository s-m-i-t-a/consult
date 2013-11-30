# Feature: Register anonymous user
    # As anonymous user
    # I want register
    # Then I can sign in my account

    # Pokud neni scenar jako prvni, tak vytvori i existujiciho uzivatele,
    # tedy system asi neulozi usera (proc?) a necha ho klidne vytvorit.
    #
    # Mozna pricina je mazani databaze po kazdem scenari,
    # ale proc by mazal vlastne az treti setp?
    Scenario: Register konwn user
        Given I visit register page
        And system have stored user with email "user@example.org" and password "vimnevim"
        And I fill form with email "user@example.org" and password "nevim_heslo123"
        When I click in button "Sign up"
        Then I see same page with message "Correct your registration data and please try again."


    Scenario: Register unknown user
        Given I visit register page
        And I fill form with email "user@example.org" and password "nevim_heslo123"
        When I click in button "Sign up"
        Then I see page with message "Thank you,..."
        #And I receive mail with message "Thank you,..."
        And system save user into database


    Scenario: Register unknown user with wrong email
        Given I visit register page
        And I fill form with email "nevim" and password "heslo123"
        When I click in button "Register"
        Then I see same page with message "Enter a valid e-mail address."


    Scenario: Register unknown user with empty email
        Given I visit register page
        And I fill form without email and password "heslo123"
        When I click in button "Register"
        Then I see same page with message "This field is required."


    Scenario: Register unknown user with empty password
        Given I visit register page
        And I fill form with email "nevim@nevim.cz" and empty password
        When I click in button "Register"
        Then I see same page with message "This field is required."


    Scenario: Register unknown user with different passwords
        Given I visit register page
        And I fill form with email "nevim@nevim.cz" and first password "heslo123" and second password "321olseh"
        When I click in button "Register"
        Then I see same page with message "Passwords is not equal!"
