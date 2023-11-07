
{'date': 'Tue Nov 07 2023 11:40:17.645 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 40
    Jogador()
  module <module> line 26
    self.mao = MaoJogador(dono=self)
  module <module> line 35
    print(f"A mão do {self.dono.nome} possui {len(self.cartas)} cartas")
  module <module> line 1
    (self.dono.nome)
AttributeError: 'Jogador' object has no attribute 'nome'
'''},