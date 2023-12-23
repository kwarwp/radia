
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
{'date': 'Tue Dec 12 2023 08:43:08.552 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Bemvindos à Ilha Poibida - montagem do tabuleiro
cartas tesouro: [v, , f, , f, t, f, h, f, d, a, a, h, a, t, a, v, , v, t, t, h, t, v, v, f, d, a]
cartas de inundacao: [12, 9, 7, 13, 0, 17, 20, 3, 18, 2, 19, 6, 22, 5, 1, 21, 15, 14, 10, 4, 11, 16, 23, 8]
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
  module <module> line 162
    ilha()
  module vento.cartas line 29
    print("cartas distribuidas:", self.distribuir_cartas_tesouro(self.cartas_tesouro))
  module vento.cartas line 32
    return random.sample(cartas,2)
AttributeError: 'function' object has no attribute 'sample'
'''},
{'date': 'Tue Dec 12 2023 08:43:12.644 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Bemvindos à Ilha Poibida - montagem do tabuleiro
cartas tesouro: [t, f, a, a, f, t, v, h, , t, f, a, v, f, v, v, a, h, d, h, v, t, f, d, , a, t, ]
cartas de inundacao: [14, 0, 10, 11, 6, 8, 9, 5, 17, 18, 19, 22, 20, 23, 21, 7, 13, 4, 15, 2, 1, 3, 16, 12]
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
  module <module> line 162
    ilha()
  module vento.cartas line 29
    print("cartas distribuidas:", self.distribuir_cartas_tesouro(self.cartas_tesouro))
  module vento.cartas line 32
    return random.sample(cartas,2)
AttributeError: 'function' object has no attribute 'sample'
'''},
{'date': 'Tue Dec 12 2023 08:46:24.624 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Bemvindos à Ilha Poibida - montagem do tabuleiro
cartas tesouro: [a, t, t, v, v, f, a, , a, v, d, a, t, v, v, t, h, a, f, f, h, t, , f, h, d, f, ]
cartas de inundacao: [13, 3, 6, 0, 19, 8, 21, 12, 9, 5, 14, 18, 20, 4, 2, 22, 7, 11, 23, 16, 15, 10, 17, 1]
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
  module <module> line 162
    ilha()
  module vento.cartas line 29
    print("cartas distribuidas:", self.distribuir_cartas_tesouro(self.cartas_tesouro))
  module vento.cartas line 32
    return random.sample(cartas,2)
AttributeError: 'function' object has no attribute 'sample'
'''},
{'date': 'Tue Dec 19 2023 11:31:32.479 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 374
    setup(numero_jogadores=4)
  module <module> line 202
    tesouros = criar_artefatos()
  module <module> line 172
    artefato1 = Artefato("   TESOURO FOGO  ", "")
TypeError: 'module' object is not callable
'''},
{'date': 'Tue Dec 19 2023 11:34:36.631 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 374
    setup(numero_jogadores=4)
  module <module> line 202
    tesouros = criar_artefatos()
  module <module> line 178
    lista_de_artefatos.append(artefato2)
NameError: name 'artefato2' is not defined
'''},
{'date': 'Tue Dec 19 2023 11:35:20.326 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 374
    setup(numero_jogadores=4)
  module <module> line 231
    lista_tesouros = tesouros.copy()
AttributeError: 'NoneType' object has no attribute 'copy'
'''},
{'date': 'Tue Dec 19 2023 11:36:06.626 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 374
    setup(numero_jogadores=4)
  module <module> line 202
    tesouros = criar_artefatos()
  module <module> line 172
    artefato1 = Artefato("   TESOURO FOGO  ", "")
TypeError: 'module' object is not callable
'''},
{'date': 'Sat Dec 23 2023 12:28:39.31 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''Bemvindos à Ilha Poibida - montagem do tabuleiro
cartas tesouro: [t, f, a, a, v, , a, v, t, h, a, d, v, f, h, t, f, , f, v, d, t, h, t, a, , v, f]
cartas de inundacao: [7, 17, 16, 10, 23, 18, 19, 0, 14, 2, 11, 6, 3, 12, 9, 15, 4, 8, 21, 13, 22, 1, 5, 20]
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
  module <module> line 162
    ilha()
  module vento.cartas line 29
    print("cartas distribuidas:", self.distribuir_cartas_tesouro(self.cartas_tesouro))
  module vento.cartas line 32
    return random.sample(cartas,2)
AttributeError: 'function' object has no attribute 'sample'
'''},
{'date': 'Sat Dec 23 2023 12:28:39.177 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''Bemvindos à Ilha Poibida - montagem do tabuleiro
cartas tesouro: [h, d, v, t, d, t, f, v, t, a, f, f, , a, , v, f, , a, v, t, f, h, v, a, t, h, a]
cartas de inundacao: [17, 7, 16, 14, 18, 15, 2, 13, 9, 19, 0, 20, 4, 6, 22, 1, 11, 10, 5, 23, 8, 3, 21, 12]
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
  module <module> line 162
    ilha()
  module vento.cartas line 29
    print("cartas distribuidas:", self.distribuir_cartas_tesouro(self.cartas_tesouro))
  module vento.cartas line 32
    return random.sample(cartas,2)
AttributeError: 'function' object has no attribute 'sample'
'''},