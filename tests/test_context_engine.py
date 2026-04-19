from unittest.mock import patch
from src.context_engine import QwenEnricher

@patch('ollama.Client')
def test_process_chunk(mock_client_class):
    # Mock Ollama response
    mock_client = mock_client_class.return_value
    mock_client.chat.return_value = {
        'message': {'content': 'Texto processado'}
    }
    
    enricher = QwenEnricher()
    result = enricher.process_chunk("Texto original")
    
    assert result == "Texto processado"
    mock_client.chat.assert_called_once()

@patch('src.context_engine.QwenEnricher.process_chunk')
def test_enrich_text_chunking(mock_process_chunk):
    mock_process_chunk.return_value = "P"
    
    enricher = QwenEnricher()
    # 10 chars, chunk_size=5 -> 2 chunks
    result = enricher.enrich_text("1234567890", chunk_size=5)
    
    assert result == "P\n\nP"
    assert mock_process_chunk.call_count == 2
