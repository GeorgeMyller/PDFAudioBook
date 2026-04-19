# Tasks: PDF to Audiobook (Local Qwen3)

## Phase 1: Environment & Foundation
Objetivo: Configurar o ambiente com `uv` e as dependências base.

- [ ] Instalar o `uv` (forçando instalação local se necessário) <!-- id: 1.1 -->
- [ ] Inicializar projeto Python com `uv init` <!-- id: 1.2 -->
- [ ] Configurar `pyproject.toml` com `ruff` e `mypy` <!-- id: 1.3 -->
- [ ] Adicionar dependências principais: `edge-tts`, `ollama`, `marker-pdf` (ou `docling`) <!-- id: 1.4 -->

## Phase 2: PDF processing & Markdown
Objetivo: Garantir que o PDF seja convertido em Markdown limpo.

- [ ] Implementar módulo `pdf_processor.py` usando `marker-pdf` <!-- id: 2.1 -->
- [ ] Testar extração com um PDF de exemplo <!-- id: 2.2 -->
- [ ] Implementar sistema de cache para o Markdown gerado <!-- id: 2.3 -->

## Phase 3: Qwen3 Integration (Ollama)
Objetivo: Integrar o LLM para limpar e estruturar o roteiro de narração.

- [ ] Criar classe `QwenEnricher` para comunicação com Ollama API <!-- id: 3.1 -->
- [ ] Definir System Prompt otimizado para audiolivros <!-- id: 3.2 -->
- [ ] Implementar lógica de chunking de texto (para livros grandes) <!-- id: 3.3 -->
- [ ] Validar limpeza de texto (remoção de cabeçalhos/notas) <!-- id: 3.4 -->

## Phase 4: TTS Pipeline (EdgeTTS)
Objetivo: Gerar o áudio final a partir do texto processado.

- [ ] Implementar `audio_generator.py` usando `edge-tts` <!-- id: 4.1 -->
- [ ] Adicionar suporte a seleção de vozes e ajuste de velocidade <!-- id: 4.2 -->
- [ ] Implementar concatenação de chunks de áudio <!-- id: 4.3 -->

## Phase 5: CLI Orchestration & Final Polish
Objetivo: Criar a interface de comando e validar o fluxo completo.

- [ ] Implementar CLI principal com `click` ou `argparse` <!-- id: 5.1 -->
- [ ] Adicionar indicadores de progresso (ex: `rich` ou `tqdm`) <!-- id: 5.2 -->
- [ ] Realizar teste fim-a-fim: PDF -> Markdown -> Qwen3 -> Audio <!-- id: 5.3 -->
- [ ] Documentar uso no README.md <!-- id: 5.4 -->
