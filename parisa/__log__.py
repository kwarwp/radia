
{'date': 'Tue Oct 24 2023 10:43:55.72 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 42
  n = 5
  ^
IndentationError: unexpected indent
'''},
{'date': 'Tue Oct 24 2023 10:45:24.618 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 42
  w = 5
  ^
IndentationError: unexpected indent
'''},
{'date': 'Tue Oct 24 2023 13:04:06.830 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 98
    IlhaProibida()
  module <module> line 32
    self.peao.mover(self.terreno[0])
AttributeError: 'IlhaProibida' object has no attribute 'terreno'
'''},
{'date': 'Tue Oct 31 2023 12:15:12.179 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 50
  self.terrenos = [Terreno(cena=self.oceano, posy=px // 6,
                                                                                                                                                                                                    ^
SyntaxError: invalid syntax
'''},