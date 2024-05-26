from io import StringIO

import pytest
from lxml import etree

from udl2xml.implementation import get_implementation
from udl2xml.util import get_line
from udl2xml.xdata import handle_xdata


def test_cdata():
    """Tests for default CDATA wrapper"""
    
    udl = """
XData a
{
<root>Something in the way...</root>
}
""".lstrip()
    
    xd = call_handler(udl)
    xds = etree.tostring(xd, encoding='UTF-8').decode()
    assert xds.startswith('<Data><![CDATA['), "Content starts with CDATA wrapper"
    assert xds.endswith(']]></Data>\n'), "Content ends with CDATA wrapper"


def test_multiline_comment_inline():
    """Test multiline comment ending on the same line"""
    
    udl = """
Method Test()
{
	Set a = /* What do you think? */ 42
}
""".lstrip()
    stream = StringIO(udl)
    # Remove first two lines like actual code would
    get_line(stream)
    get_line(stream)
    
    impl = get_implementation(stream, 'objectscript', 'test')
    assert impl == '\tSet a = /* What do you think? */ 42', "End of comment detected"


def test_unknown_type():
    """Tests handling of an unhandled implementation type"""
    
    udl = StringIO()
    with pytest.raises(ValueError, match="Don't know how to parse"):
        get_implementation(udl, 'unknown_type', None)


def test_python_impl():
    """Tests retrieving a Python method implementation"""
    
    frag = '''
"""
A string {
"""
for n in range(5):
    pass # }
\'''}\'''
}
'''.lstrip()
    
    expect = '"""\nA string {\n"""\nfor n in range(5):\n    pass # }\n\'\'\'}\'\'\''
    
    stream = StringIO(frag)
    impl = get_implementation(stream, 'python', None)
    assert impl == expect, "Implementation extracted properly"
    
    
    


# -----

def call_handler(udl:str) -> etree._Element:
    """Helper to call the handler method"""
    
    root = etree.Element("dummy")
    root.text = '\n'
    stream = StringIO(udl)
    line = get_line(stream)
    
    handle_xdata(root, stream, line, None)
    
    assert len(root) == 1, 'XData element added'
    assert (data := root.find('.//Data')) is not None, "Data element present"
    return data

