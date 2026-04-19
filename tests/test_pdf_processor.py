import pytest
from src.pdf_processor import PDFProcessor

def test_pdf_processor_initialization():
    processor = PDFProcessor()
    assert processor is not None

def test_extract_markdown_failure_on_missing_file():
    processor = PDFProcessor()
    with pytest.raises(FileNotFoundError):
        processor.extract_markdown("non_existent.pdf")

def test_cache_mechanism(tmp_path):
    # Mock behavior for cache
    pdf_path = tmp_path / "test.pdf"
    pdf_path.write_text("dummy pdf")
    
    processor = PDFProcessor(cache_dir=tmp_path / "cache")
    # This should fail first because implementation is empty
    result = processor.extract_markdown(str(pdf_path))
    assert result is not None
