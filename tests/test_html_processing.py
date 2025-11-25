"""Tests for HTML processing in SimplePDF builder."""
import pytest
import re


def test_html_is_processed(sphinx_build):
    """Test that HTML is processed by SimplePDF builder."""
    result = sphinx_build(srcdir="basic_doc").build()

    # Original HTML should exist
    original_html = result.html_content("index")
    assert original_html

    # Processed HTML should be in debug output
    # (requires SimplePDF to log processed HTML)
    try:
        processed_html = result.processed_html()
        assert processed_html
        # Processed HTML should differ from original
        assert processed_html != original_html
    except ValueError:
        pytest.skip("SimplePDF debug output not available")


def test_anchors_are_preserved(sphinx_build):
    """Test that anchors/IDs are preserved in HTML processing."""
    result = sphinx_build(srcdir="with_toc").build()

    html = result.html_content("index")

    # Check for section anchors
    assert 'id="' in html or 'href="#' in html


def test_image_paths_are_resolved(sphinx_build):
    """Test that image paths are correctly resolved."""
    result = sphinx_build(srcdir="with_images").build()

    html = result.html_content("index")

    # Images should be referenced
    assert "<img" in html
    # No broken image references
    assert 'src=""' not in html


def test_css_is_applied(sphinx_build):
    """Test that SimplePDF theme CSS is applied."""
    result = sphinx_build(srcdir="basic_doc").build()

    html = result.html_content("index")

    # Should contain style information
    assert "<style" in html or 'rel="stylesheet"' in html
