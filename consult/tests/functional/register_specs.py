# -*- coding: utf-8 -*-

import re

import pytest

from functools import partial

from pytest_bdd import scenario, given, when, then


# XXX: from tests.factories not work, because import colliding with other package
from ..factories import UserFactory


pytestmark = pytest.mark.usefixtures("db")

scenario = partial(scenario, 'register.feature')
test_register_known_user = scenario('Register konwn user')
test_register_unknown_user = scenario('Register unknown user')


REGISTER_URL = '/register/'


@given('I visit register page')
def visit_register_page(browser, live_server):
    browser.visit(live_server + REGISTER_URL)


@given(re.compile('I fill form with email "(?P<email>\w+@\w+\.\w+)" and password "(?P<password>\w+)"'))
def registred_user(browser, email, password):
    browser.fill('email', email)
    browser.fill('password', password)
    browser.fill('password_again', password)

    #registred_user = {'email': email, 'password': password}
    #print registred_user
    #return registred_user


@when(re.compile('I click in button "(?P<button>.*)"'))
def i_click_on_button(browser, button):
    #btn = browser.find_by_tag("button")
    btn = browser.find_by_xpath('//button[text()="%s"]' % button)
    btn.first.click()


@then(re.compile('I see page with message "(?P<message>.*)\.\.\."'))
def i_see_page_with_message(browser, message):
    assert browser.is_text_present(message)


@then('system save user into database')
def system_save_user_into_database():
    from flask_musers.models import User

    assert len(User.objects) == 1
    #users = User.objects.filter(email=registred_user['email'])
    #assert len(users) == 1

    #user = users[0]
    #assert user.check_password(registred_user['password'])


@given(re.compile('system have stored user with email "(?P<email>\w+@\w+\.\w+)" and password "(?P<password>\w+)"'))
def stored_user(email, password):
    user = {
        'email': email,
        'password': password
    }

    UserFactory(email=email, password=password)

    return user


@then(re.compile('I see same page with message "(?P<message>.*)"'))
def i_see_page_with_message_second(browser, message):
    assert browser.url.find(REGISTER_URL) > -1
    assert browser.is_text_present(message, wait_time=10)


#@given('I fill form without email and password "{password}"')
#def i_not_fill_email(context, password):
    #context.browser.fill('password', password)
    #context.browser.fill('password_again', password)


#@given('I fill form with email "{email}" and empty password')
#def i_fill_email(context, email):
    #context.browser.fill('email', email)


#@given('I fill form with email "{email}" and first password "{password}" and second password "{password_again}"')
#def i_fill_different_passwords(context, email, password, password_again):
    #context.browser.fill('email', email)
    #context.browser.fill('password', password)
    #context.browser.fill('password_again', password_again)
