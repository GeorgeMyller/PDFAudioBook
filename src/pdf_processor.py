import fitz  # PyMuPDF
from pathlib import Path

class PDFProcessor:
    def __init__(self, cache_dir: str = ".cache/markdown"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def extract_markdown(self, pdf_path: str) -> str:
        """Extrai texto do PDF usando PyMuPDF (compatível com Python 3.9)."""
        pdf_name = Path(pdf_path).stem
        cache_file = self.cache_dir / f"{pdf_name}.md"

        # Verifica cache
        if cache_file.exists():
            print(f"Usando Markdown em cache: {cache_file}")
            return cache_file.read_text()

        print(f"Extraindo texto de {pdf_path} via PyMuPDF...")
        
        # Extração via PyMuPDF
        doc = fitz.open(pdf_path)
        full_text = []
        for page in doc:
            full_text.append(page.get_text())
        
        markdown_content = "\n\n".join(full_text)

        # Salva no cache
        cache_file.write_text(markdown_content)
        return markdown_content
