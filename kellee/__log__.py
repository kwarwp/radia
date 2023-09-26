
{'date': 'Tue Sep 26 2023 11:42:13.669 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 30
    IlhaProibida()
  module <module> line 13
    portao = Terreno(PORTAO_BRONZE, x=10, y=50, w=100, h=100, tit="Portao de Bronze",cena=oceano)
TypeError: __init__() got an unexpected keyword argument 'x'
'''},