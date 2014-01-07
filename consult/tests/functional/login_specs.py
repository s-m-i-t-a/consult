# -*- coding: utf-8 -*-
'''
Feature: Registered user can log in
    As registered user
    I want to log in to my account
    Then I can create, edit, delete my questions or answers, vote on others items
'''

import pytest

# XXX: from tests.factories not work, because import colliding with other package
from ..factories import UserFactory


pytestmark = pytest.mark.usefixtures("db")


LOGIN_URL = '/login/'
DASHBOARD_URL = '/dashboard/'


def test_corect_login_as_registred_user(live_server, browser):
    ''' Scenario: Correct login as registered user'''

    # Given I am on login page
    browser.visit(live_server + LOGIN_URL)

    # And a customer named "Josef Pokusny" with email "pokus@hokus.cz" and password "jednadva"
    full_name = u'Josef Pokusny'
    names = full_name.split()
    first_name = names[0]
    last_name = names[-1]
    user = {
        'email': u'pokus@hokus.cz',
        'password': 'jednadva',
        'full_name': full_name,
        'first_name': first_name,
        'last_name': last_name,
    }

    UserFactory(email=user['email'], password=user['password'], first_name=first_name, last_name=last_name)

    # When I sign in as "Josef Pokusny"
    browser.fill('email', user['email'])
    browser.fill('password', user['password'])

    btn = browser.find_by_xpath('//button[text()="Login"]')
    btn.first.click()

    # Then I see my dashboard
    assert browser.url.find(DASHBOARD_URL) > -1
    assert browser.is_text_present('Dashboard')

    # And I see message "Logged in successfully."
    assert browser.is_text_present(u'Logged in successfully', wait_time=10)


def test_user_logout(live_server, browser):
    '''
    Scenario: Log out user
    '''
    # Given a customer named "Karel Odhlasovac" with email "odkarel@logout.cz" and password "odhlasitme"
    full_name = u'Karel Odhlasovac'
    names = full_name.split()
    first_name = names[0]
    last_name = names[-1]
    user = {
        'email': u'odkarel@logout.cz',
        'password': 'odhlasitme',
        'full_name': full_name,
        'first_name': first_name,
        'last_name': last_name,
    }

    UserFactory(email=user['email'], password=user['password'], first_name=first_name, last_name=last_name)

    # And I am logged in as "Karel Odhlasovac"
    browser.visit(live_server + LOGIN_URL)

    browser.fill('email', user['email'])
    browser.fill('password', user['password'])

    btn = browser.find_by_xpath('//button[text()="Login"]')
    btn.first.click()

    # When I try log out
    browser.click_link_by_partial_href('logout')

    # Then I will see login page
    assert browser.url.find(LOGIN_URL) > -1
    assert browser.is_text_present('Login')


def test_incorrect_login(live_server, browser):
    '''
    Scenario: Incorrect login
    '''
    # Given I am on login page
    browser.visit(live_server + LOGIN_URL)

    # And a unregistred customer named "John Zaskodnik" with email "john@dark.cz" and password "1234567890"
    full_name = u'John Zaskodnik'
    names = full_name.split()
    first_name = names[0]
    last_name = names[-1]
    user = {
        'email': u'john@dark.cz',
        'password': '1234567890',
        'full_name': full_name,
        'first_name': first_name,
        'last_name': last_name,
    }

    # When I sign in as "John Zaskodnik"
    browser.fill('email', user['email'])
    browser.fill('password', user['password'])

    btn = browser.find_by_xpath('//button[text()="Login"]')
    btn.first.click()

    # Then I see same login page with error validations "Your username and password didn't match. Please try again."
    assert browser.url.find(LOGIN_URL) > -1
    assert browser.is_text_present('Your username and password didn\'t match. Please try again.')
