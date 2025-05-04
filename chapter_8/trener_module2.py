"""Импортируем модуль"""
# import trener_module
# trener_module.make_pizza(27, 'peperoni')
# trener_module.make_pizza(40, 'mushrooms', 'extra cheese', 'green peper')
'''Импортируем фунцию с указанием псевдонима'''
# from chapter_8.trener_module import make_pizza as mk
# mk(27, 'peperoni')
# mk(40, 'mushrooms', 'extra cheese', 'green peper')
'''Импортируем модуль с указанием псевдонимадонима'''
import trener_module as t
t.make_pizza(27, 'peperoni')
t.make_pizza(40, 'mushrooms', 'extra cheese', 'green peper')