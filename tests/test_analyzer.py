import pytest
from pyreachx.analyzer import CodeAnalyzer
from pyreachx.config import AnalyzerConfig
from pyreachx.result import UnreachableCode

def test_analyze_simple_function(tmp_path):
    code = """
def used_function():
    return 42

def unused_function():
    return 24

def main():
    return used_function()
"""
    file_path = tmp_path / "test_module.py"
    file_path.write_text(code)
    analyzer = CodeAnalyzer(AnalyzerConfig())
    result = analyzer.analyze(str(file_path), "main")
    
    unreachable_functions = [
        item for item in result.unreachable_items 
        if item.code_type == 'function'
    ]
    unreachable_names = [item.name for item in unreachable_functions]
    assert "unused_function" in unreachable_names
    assert "used_function" not in unreachable_names

def test_analyze_class_methods(tmp_path):
    code = """
class TestClass:
    def used_method(self):
        return 42
        
    def unused_method(self):
        return 24
        
def main():
    t = TestClass()
    return t.used_method()
"""
    file_path = tmp_path / "test_module.py"
    file_path.write_text(code)
    analyzer = CodeAnalyzer(AnalyzerConfig())
    result = analyzer.analyze(str(file_path), "main")
    
    unreachable_methods = [
        item for item in result.unreachable_items 
        if item.code_type == 'method'
    ]
    unreachable_names = [item.name for item in unreachable_methods]
    assert "TestClass.unused_method" in unreachable_names
    assert "TestClass.used_method" not in unreachable_names