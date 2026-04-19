import ollama

class QwenEnricher:
    def __init__(self, model: str = "qwen3:14b", host: str = "http://localhost:11434"):
        self.model = model
        self.client = ollama.Client(host=host)
        self.system_prompt = (
            "Você é um roteirista de audiolivros profissional especializado em Português do Brasil. "
            "Sua tarefa é transformar o conteúdo de um Markdown extraído de um PDF em um script "
            "de narração fluido e natural em PT-BR.\n\n"
            "Diretrizes:\n"
            "1. Remova ruídos: números de página, cabeçalhos repetitivos, rodapés e notas de fim.\n"
            "2. Humanize o texto: Se houver tabelas, resuma os dados principais de forma narrativa "
            "ou ignore se forem puramente técnicas. Se houver fórmulas complexas, descreva-as de forma simples.\n"
            "3. Estrutura: Mantenha a ordem dos capítulos e seções.\n"
            "4. Tom: Mantenha o tom original do autor, garantindo que a prosódia seja natural para o público brasileiro.\n"
            "5. Silencie o lixo: Ignore referências bibliográficas extensas no meio do texto.\n"
            "Output: Apenas o texto limpo para narração em Português do Brasil, sem comentários seus."
        )

    def process_chunk(self, text: str) -> str:
        """Process a single chunk of text via Qwen3."""
        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Transforme este trecho em script de narração:\n\n{text}"}
            ]
        )
        return response['message']['content']

    def enrich_text(self, markdown_text: str, chunk_size: int = 5000) -> str:
        """Divide the text into chunks and process each through the LLM."""
        # Simple character-based chunking (can be improved to respect paragraph boundaries)
        chunks = [markdown_text[i:i + chunk_size] for i in range(0, len(markdown_text), chunk_size)]
        
        enriched_chunks = []
        for i, chunk in enumerate(chunks):
            # i+1 for log
            print(f"Processando bloco {i+1}/{len(chunks)} via Qwen3...")
            enriched_chunks.append(self.process_chunk(chunk))
            
        return "\n\n".join(enriched_chunks)
