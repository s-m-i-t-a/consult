# -*- coding: utf-8 -*-
'''
Feature: Register anonymous user
    As anonymous user
    I want register
    Then I can sign in my account
'''

import re

import pytest


# XXX: from tests.factories not work, because import colliding with other package
from ..factories import UserFactory


pytestmark = pytest.mark.usefixtures("db")


REGISTER_URL = '/register/'


def test_register_known_user(live_server, browser):
    '''
    Scenario: Register konwn user
    '''
    # Given I visit register page
    browser.visit(live_server + REGISTER_URL)

    # And system have stored user with email "user@example.org" and password "vimnevim"
    user = {
        'email': 'user@example.org',
        'password': 'vimnevim'
    }

    UserFactory(email=user['email'], password=user['password'])

    # And I fill form with email "user@example.org" and password "nevim_heslo123"
    password = 'nevim_heslo123'
    browser.fill('email', user['email'])
    browser.fill('password', password)
    browser.fill('password_again', password)

    # When I click in button "Sign up"
    btn = browser.find_by_xpath('//button[text()="Sign up"]')
    btn.first.click()

    # Then I see same page with message "Correct your registration data and please try again."
    assert browser.is_text_present("Correct your registration data and please try again.")


def test_register_unknown_user(live_server, browser):
    '''
    Scenario: Register unknown user
    '''
    # Given I visit register page
    browser.visit(live_server + REGISTER_URL)

    # And I fill form with email "user@example.org" and password "nevim_heslo123"
    password = 'nevim_heslo123'
    browser.fill('email', 'user@example.org')
    browser.fill('password', password)
    browser.fill('password_again', password)

    # When I click in button "Sign up"
    btn = browser.find_by_xpath('//button[text()="Sign up"]')
    btn.first.click()

    # Then I see page with message "Thank you,..."
    assert browser.is_text_present("Thank you,")

    # And system save user into database
    from flask_musers.models import User
    assert len(User.objects) == 1


def test_register_user_with_wrong_email(live_server, browser):
    '''
    Scenario: Register unknown user with wrong email
    '''

    # Given I visit register page
    browser.visit(live_server + REGISTER_URL)

    # And I fill form with email "nevim" and password "heslo123"
    password = 'heslo123'
    browser.fill('email', 'nevim')
    browser.fill('password', password)
    browser.fill('password_again', password)

    # When I click in button "Sign up"
    btn = browser.find_by_xpath('//button[text()="Sign up"]')
    btn.first.click()

    # Then I see same page with message "Enter a valid e-mail address."
    assert browser.url.find(REGISTER_URL) > -1
    assert browser.is_text_present('Enter a valid e-mail address.', wait_time=10)


def test_register_user_with_empty_email_field(live_server, browser):
    '''
    Scenario: Register unknown user with empty email
    '''

    # Given I visit register page
    browser.visit(live_server + REGISTER_URL)

    # And I fill form without email and password "heslo123"
    password = 'heslo123'
    browser.fill('email', '')
    browser.fill('password', password)
    browser.fill('password_again', password)

    # When I click in button "Sign up"
    btn = browser.find_by_xpath('//button[text()="Sign up"]')
    btn.first.click()

    # Then I see same page with message "This field is required."
    assert browser.url.find(REGISTER_URL) > -1
    assert browser.is_text_present('This field is required.', wait_time=10)


def test_register_user_with_different_passwords(live_server, browser):
    '''
    Scenario: Register unknown user with different passwords
    '''
    # Given I visit register page
    browser.visit(live_server + REGISTER_URL)

    # And I fill form with email "nevim@nevim.cz" and first password "heslo123" and second password "321olseh"
    browser.fill('email', 'nevim@nevim.cz')
    browser.fill('password', 'heslo123')
    browser.fill('password_again', '321olseh')

    # When I click in button "Sign up"
    btn = browser.find_by_xpath('//button[text()="Sign up"]')
    btn.first.click()

    # Then I see same page with message "Passwords is not equal!"
    assert browser.url.find(REGISTER_URL) > -1
    assert browser.is_text_present('Passwords is not equal!', wait_time=10)
