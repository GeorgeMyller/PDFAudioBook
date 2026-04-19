import click
import asyncio
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from src.pdf_processor import PDFProcessor
from src.context_engine import QwenEnricher
from src.audio_generator import AudioGenerator

console = Console()

async def run_pipeline(pdf_path: str, output_path: str, voice: str, rate: str, chunk_size: int):
    """Orquestra o pipeline completo de conversão."""
    
    input_file = Path(pdf_path)
    if not input_file.exists():
        console.print(f"[red]Erro: Arquivo {pdf_path} não encontrado.[/red]")
        return

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console
    ) as progress:
        
        # Passo 1: Extração de PDF
        task1 = progress.add_task("[cyan]Extraindo Markdown do PDF...", total=100)
        processor = PDFProcessor()
        try:
            markdown_content = processor.extract_markdown(pdf_path)
            progress.update(task1, completed=100)
        except Exception as e:
            console.print(f"[red]Erro na extração: {e}[/red]")
            return

        # Passo 2: Processamento via LLM
        task2 = progress.add_task("[magenta]Enriquecendo texto via Qwen3...", total=100)
        enricher = QwenEnricher()
        try:
            # Dividimos o processo em enriquecimento (que já tem print interno ou podemos melhorar)
            enriched_text = enricher.enrich_text(markdown_content, chunk_size=chunk_size)
            progress.update(task2, completed=100)
        except Exception as e:
            console.print(f"[red]Erro no LLM: {e}[/red]. Certifique-se de que o Ollama está rodando.")
            return

        # Passo 3: Geração de Áudio
        task3 = progress.add_task("[green]Gerando Audiobook (EdgeTTS)...", total=100)
        generator = AudioGenerator(voice=voice, rate=rate)
        try:
            await generator.generate_audio(enriched_text, str(output_file))
            progress.update(task3, completed=100)
        except Exception as e:
            console.print(f"[red]Erro no TTS: {e}[/red]")
            return

    console.print(f"\n[bold green]Sucesso![/bold green] Audiobook gerado em: [blue]{output_file}[/blue]")

@click.command()
@click.argument('pdf_path', type=click.Path(exists=True))
@click.option('--output', '-o', default="outputs/audiobook.mp3", help="Caminho do arquivo de saída.")
@click.option('--voice', '-v', default="pt-BR-AntonioNeural", help="Voz do EdgeTTS.")
@click.option('--rate', '-r', default="+0%", help="Velocidade da fala (ex: +10% ou -5%).")
@click.option('--chunk-size', '-c', default=5000, help="Tamanho dos blocos de texto para o LLM.")
def main(pdf_path, output, voice, rate, chunk_size):
    """PDF to Audiobook CLI - Usando Qwen3 e EdgeTTS localmente."""
    asyncio.run(run_pipeline(pdf_path, output, voice, rate, chunk_size))

if __name__ == "__main__":
    main()
