# Entrevista para desenvolvedor VIACast

As orientações que seguem são intencionalmente não específicas. Interprete cada situação da forma que acreditar ser mais adequada, especificando quaisquer suposições feitas.

## Validação de código

Você recebeu dois arquivos, um com um código em C ([reverse_string.c](./reverse_string.c)), outro em Python ([shapes.py](./shapes.py)). Ambos precisam ser validados antes de serem incluídos na base de código principal de um projeto.
Avalie os seguintes pontos para os dois programas:

1. Em situações usuais, o código irá funcionar como esperado?
2. Existe alguma situação em que não irá funcionar?
3. Caso exista alguma situação em que o código não irá funcionar, quais alterações seriam necessárias para corrigir os problemas?
4. Pensando na legibilidade, facilidade de manutenção por outros desenvolvedores, e extensibilidade, você faria alguma refatoração no código?

## Implementação

Você precisa implementar uma função em Python que recebe um único argumento `n` e retorna o `n`-ésimo elemento da sequência de Fibonacci. Essa função deve ser extremamente otimizada, pois trata-se de uma função crítica do projeto, a qual será chamada com alta frequência e com valores grandes de `n`. (>1000).

```python
def fibonacci(n: int) -> int:
  ....
```
