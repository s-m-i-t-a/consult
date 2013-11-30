# -*- coding: utf-8 -*-

import factory

from factory.mongoengine import MongoEngineFactory

from flask_musers.models import User


class UserFactory(MongoEngineFactory):
    FACTORY_FOR = User

    email = factory.Sequence(lambda n: u'jozin%d@zbazin.cz' % n)
    password = 'zbazojozo232'
    activated = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
