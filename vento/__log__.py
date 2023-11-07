
{'date': 'Tue Nov 07 2023 09:49:25.261 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  ---------
            ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Nov 07 2023 09:49:54.421 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 97
    IlhaProibida()
  module <module> line 29
    self.terrenos[1].ocupa(self.peao)
IndexError: list index out of range
'''},
{'date': 'Tue Nov 07 2023 09:50:55.826 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  ---------
            ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Nov 07 2023 11:45:40.83 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 184
    ilha()
TypeError: 'module' object is not callable
'''},
{'date': 'Tue Nov 07 2023 11:57:11.527 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Bemvindos à Ilha Poibida - montagem do tabuleiro
cartas tesouro: [f, v, t, h, a, f, f, , t, , v, a, a, t, , f, h, h, d, d, t, a, t, v, v, f, a, v]
cartas de inundacao: [17, 20, 3, 16, 7, 11, 18, 13, 9, 21, 8, 10, 12, 22, 4, 5, 14, 0, 15, 23, 6, 19, 2, 1]
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 55
    IlhaProibida()
  module <module> line 29
    print("cartas distribuidas:", self.distribuir_cartas_tesouro(self.cartas_tesouro))
  module <module> line 32
    return sample(cartas,2)
NameError: name 'sample' is not defined
'''},
{'date': 'Tue Nov 07 2023 11:58:06.670 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Bemvindos à Ilha Poibida - montagem do tabuleiro
cartas tesouro: [f, f, , h, f, a, v, a, f, , a, t, v, t, a, a, v, f, v, t, v, d, d, t, h, , t, h]
cartas de inundacao: [7, 14, 17, 15, 6, 20, 10, 12, 4, 23, 2, 9, 0, 11, 13, 22, 5, 1, 21, 16, 3, 18, 8, 19]
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 55
    IlhaProibida()
  module <module> line 29
    print("cartas distribuidas:", self.distribuir_cartas_tesouro(self.cartas_tesouro))
  module <module> line 32
    return random.sample(cartas,2)
AttributeError: 'function' object has no attribute 'sample'
'''},