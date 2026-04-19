# Requirements: PDF to Audiobook (Local Qwen3)

## Overview

Este sistema converte livros em PDF para arquivos de áudio (Audiobooks), utilizando inteligência artificial local (**Qwen3** via **Ollama**) para limpar, estruturar e narrar o conteúdo. O objetivo é criar uma experiência de audição fluida, removendo ruídos de formatação comuns em PDFs (cabeçalhos, rodapés, tabelas) e gerando um áudio de alta qualidade usando o **EdgeTTS**.

## User Stories

### US-1: Conversão de PDF para Texto Estruturado (Markdown)
Como usuário, quero converter meu PDF para Markdown para que o conteúdo seja extraído preservando a hierarquia de capítulos e removendo elementos não narrativos.

**Acceptance Criteria:**
- [ ] O sistema deve carregar um arquivo PDF como entrada.
- [ ] Utilizar `marker-pdf` ou `docling` para extrair o texto em formato Markdown.
- [ ] O resultado deve ser um arquivo Markdown limpo na pasta temporária do projeto.

### US-2: Enriquecimento e Limpeza via Qwen3
Como usuário, quero que o Qwen3 processe o conteúdo extraído para remover erros de OCR, silenciar referências/tabelas e preparar o "script" de narração.

**Acceptance Criteria:**
- [ ] Conectar ao modelo Qwen3 via API local do Ollama (`localhost:11434`).
- [ ] Solicitar ao modelo a limpeza do texto para narração (remover índices, números de página, cabeçalhos repetitivos).
- [ ] O modelo deve retornar o texto pronto para ser enviado ao TTS.

### US-3: Geração de Áudio (Audiobook)
Como usuário, quero que o script final seja convertido em áudio para que eu possa ouvi-lo.

**Acceptance Criteria:**
- [ ] Utilizar a biblioteca `edge-tts` para converter o texto enriquecido em áudio MP3.
- [ ] O sistema deve salvar o arquivo de saída com o nome do livro e timestamp.
- [ ] O processamento deve ser feito em blocos (chunks) para evitar limites de buffer.

## Constraints

- **Inference**: Deve rodar localmente via Ollama (sem dependência de APIs pagas de LLM).
- **TTS**: Dependente da conectividade do EdgeTTS (mas gratuito e leve).
- **Package Manager**: Uso obrigatório de `uv` e `pyproject.toml` conforme regras globais.
- **Language**: Python 3.9+.

## Out of Scope

- Interface Gráfica (GUI) complexa — o sistema será focado em CLI.
- Tradução de idiomas (focado no idioma original do PDF inicialmente).
- Clonagem de voz personalizada (focado em vozes pré-definidas do EdgeTTS).

## Dependencies

- **Ollama**: Rodando localmente com o modelo `qwen3` baixado.
- **uv**: Gerenciador de dependências.
- **edge-tts**: Biblioteca Python para síntese de voz.
- **marker-pdf**: Biblioteca para conversão de PDF para Markdown.

---

## Notes
Referência de projeto similar citado pelo usuário: Uso de Qwen3 + EdgeTTS para audiobooks.
