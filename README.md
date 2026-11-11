# 🎧 PDF to Audiobook CLI

> **Transforme seus PDFs em Audiobooks fluidos com a potência do Qwen3 local e a naturalidade do EdgeTTS.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Ollama: Qwen3](https://img.shields.io/badge/LLM-Qwen3%20(Ollama)-orange.svg)](https://ollama.ai/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

O **PDF to Audiobook CLI** é uma ferramenta profissional para converter livros digitais em áudio. Diferente de conversores simples, ele utiliza Inteligência Artificial local para limpar o texto de cabeçalhos, rodapés e erros de OCR, gerando uma narrativa natural e contínua.

---

## ✨ Funcionalidades

- 🧠 **IA Editorial Local**: Usa o modelo **Qwen3** (via Ollama) para remover ruídos e adaptar o texto para narração.
- 🎙️ **Narrativa de Alta Fidelidade**: Integração com **EdgeTTS** para vozes neurais extremamente naturais.
- 📄 **Extração Inteligente**: Conversão precisa de PDF para Markdown usando `marker-pdf`.
- ⚡ **Performance com `uv`**: Gerenciamento de dependências ultra-rápido e ambiente isolado.
- 📊 **Progresso em Tempo Real**: Interface CLI elegante com barras de progresso informativas.

---

## 🚀 Instalação Rápida

Este projeto recomenda o uso do gerenciador de pacotes [uv](https://github.com/astral-sh/uv).

```bash
# Clone o repositório
git clone https://github.com/GeorgeMyller/PDFAudioBook.git
cd PDFAudioBook

# Crie o ambiente e instale as dependências
uv venv
source .venv/bin/activate  # (ou .venv\Scripts\activate no Windows)
uv pip install -e .
```

### Pré-requisitos
- **Ollama**: Instalado e rodando.
- **Modelo Qwen3**: Execute `ollama pull qwen3`.

---

## 📖 Como Usar

Converta seu primeiro livro com um comando simples:

```bash
pdf-high-audio seu_livro.pdf
```

### Opções Disponíveis

| Opção | Descrição | Padrão |
| :--- | :--- | :--- |
| `-o, --output` | Caminho do arquivo MP3 final | `outputs/audiobook.mp3` |
| `-v, --voice` | Voz do EdgeTTS (ex: `pt-BR-AntonioNeural`) | `pt-BR-AntonioNeural` |
| `-r, --rate` | Velocidade da fala (ex: `+10%`, `-5%`) | `+0%` |
| `-c, --chunk-size` | Tamanho do texto enviado à IA por vez | `5000` |

---

## 🛠️ Estrutura do Projeto

Para detalhes técnicos, consulte a [Documentação de Arquitetura](ARCHITECTURE.md).

```text
├── src/
│   ├── main.py            # Orquestrador CLI
│   ├── pdf_processor.py   # Extração de Markdown
│   ├── context_engine.py  # Processamento via Qwen3
│   └── audio_generator.py # Geração de Áudio (TTS)
├── tests/                 # Suíte de testes (pytest)
└── .specs/                # Especificações de design e requisitos
```

---

## 🤝 Contribuição

Interessado em melhorar o projeto? Veja nosso [Guia de Contribuição](CONTRIBUTING.md).

---

## ⚖️ Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido por [GeorgeMyller](https://github.com/GeorgeMyller)**
