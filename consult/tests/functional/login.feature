# Feature: Registered user can log in
    # As registered user
    # I want to log in to my account
    # Then I can create and manage my pages and account settings


    Scenario: Correct login as registered user
        Given I am on login page
        And a customer named "Josef Pokusny" with email "pokus@hokus.cz" and password "jednadva"
        When I sign in as "Josef Pokusny"
        Then I see my dashboard
        And I see message "Logged in successfully."


    Scenario: Log out user
        Given a customer named "Karel Odhlasovac" with email "odkarel@logout.cz" and password "odhlasitme"
        And I am logged in as "Karel Odhlasovac"
        When I try log out
        Then I will see login page


    Scenario: Incorrect login
        Given I am on login page
        And a unregistred customer named "John Zaskodnik" with email "john@dark.cz" and password "1234567890"
        When I sign in as "John Zaskodnik"
        Then I see same login page with error validations "Your username and password didn't match. Please try again."

