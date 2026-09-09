#!/usr/bin/env python3

import pytest
from myman import myman

class TestMyManIndex:
    """Test basic indexing."""

    def test_index_one(self):
        """Test that index '1' returns exptected value."""
        s = myman.myman(ind=1)
        assert s == "My man looks like Pat Boone being tased.\n\t -- about Stephen Miller on 2026-07-16\n"

    def test_zero_on_bad_target(self):
        """Test that empty string is return on mismatched subset"""
        s = myman.myman(target="abc123")
        assert s == ""

    def test_zero_on_bad_index(self):
        """Test that empty string is return on mismatched subset"""
        s = myman.myman(ind="abc123")
        assert s == ""

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
