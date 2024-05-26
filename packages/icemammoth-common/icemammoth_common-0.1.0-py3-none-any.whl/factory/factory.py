# -*- coding: utf-8 -*-

from base.singleton import SingletonMeta
from util.log_util import logger

class Factory(metaclass=SingletonMeta):
    
    def __init__(self):
        self.productions = {}

    def register(self,type,production):
        if type not in self.productions:
            logger.info(f'{self.__class__.__module__}.{self.__class__.__name__} register {type}:{production.__class__.__module__}.{production.__class__.__name__}')
            self.productions[type] = production

    def create(self,type):
        production = self.productions.get(type)
        logger.info(f'create type {type} production {production}')
        return production

class FactoryProduction(type):

    def __new__(cls,*args,**kwargs):
        instance=super().__new__(cls,cls.__name__,args,kwargs)#产生一个新类
        cls.__register_model_entity(instance)
        return instance
 
    def __init__(self):
        pass
 
    @classmethod
    def __register_model_entity(cls, instance):
        instanceType = instance.getType()
        if instanceType is None:
            return
        factory = cls.getFactory()
        factory.register(type,instance)

    @classmethod
    def getFactory():
        pass

    def getType(self):
        pass
