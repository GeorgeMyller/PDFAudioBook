import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from src.audio_generator import AudioGenerator

@pytest.mark.asyncio
@patch('edge_tts.Communicate')
async def test_generate_audio(mock_communicate_class):
    mock_comm = AsyncMock()
    mock_communicate_class.return_value = mock_comm
    
    generator = AudioGenerator()
    await generator.generate_audio("Hello", "output.mp3")
    
    # Check if Communicate was called with correct parameters
    mock_communicate_class.assert_called_once_with("Hello", "pt-BR-AntonioNeural", rate="+0%")
    # Check if save was called
    mock_comm.save.assert_called_once_with("output.mp3")

@pytest.mark.asyncio
@patch('edge_tts.VoicesManager.create')
async def test_list_voices(mock_voices_create):
    mock_vm = MagicMock()
    mock_voices_create.return_value = mock_vm
    
    generator = AudioGenerator()
    await generator.list_voices(filter_lang="pt-BR")
    
    mock_vm.find.assert_called_once_with(Locale="pt-BR")
