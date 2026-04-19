# Guia de Contribuição (Contributing Guide)

Obrigado pelo seu interesse em contribuir para o **PDF to Audiobook CLI**! Este projeto segue padrões rigorosos de qualidade para garantir que a ferramenta permaneça eficiente, limpa e funcional.

## 🛠️ Ambiente de Desenvolvimento

Utilizamos o `uv` da Astral para gerenciamento de dependências e ambientes virtuais.

```bash
# Clone o repositório
git clone https://github.com/GeorgeMyller/pdf-audiobook.git
cd pdf-audiobook

# Instale as dependências e o projeto em modo editável
uv pip install -e .
```

## 🧹 Padrões de Código

Seguimos a filosofia **Clean Code** e utilizamos as seguintes ferramentas para garantir a qualidade:

- **Linting & Formatação**: `ruff`. Sempre execute `ruff check .` e `ruff format .` antes de submeter um PR.
- **Checagem de Tipos**: `mypy`. Todo o código deve passar no teste de tipos estrito (`mypy --strict src`).
- **Commits**: Utilizamos [Conventional Commits](https://www.conventionalcommits.org/) (ex: `feat: add support for local LLM cache`, `fix: handle edge-tts timeout`).

## 🧪 Testes

Não aceitamos novas funcionalidades sem testes.
- Utilizamos `pytest` para testes unitários e de integração.
- Os testes devem ser colocados na pasta `tests/`.
- Execute os testes com: `pytest`.

## 🔄 Fluxo de Desenvolvimento (TDD)

1. **Spec First**: Defina a funcionalidade no `.specs/` se for uma mudança estrutural.
2. **Test First**: Escreva um teste que falha para a nova funcionalidade.
3. **Code**: Implemente a lógica necessária.
4. **Refactor**: Limpe o código e garanta que todos os testes passam.

## 📝 Documentação

Se você adicionar uma nova funcionalidade, atualize:
1. O `README.md` (se houver novos comandos ou opções).
2. O `ARCHITECTURE.md` (se houver mudanças no fluxo de dados).

---

### Código de Conduta

Seja respeitoso e profissional em todas as interações. Estamos aqui para construir algo legal juntos! 🚀
