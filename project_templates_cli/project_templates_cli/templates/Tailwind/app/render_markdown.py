from fasthtml.common import NotStr, FT
import mistletoe
from lxml import html, etree

class_map = {
    # Headings with gradient accents
    'h1': 'text-4xl font-bold mt-12 mb-6 gradient-text-primary',
    'h2': 'text-3xl font-bold mt-10 mb-5 gradient-text-secondary',
    'h3': 'text-2xl font-semibold mt-8 mb-4 text-indigo-700',
    'h4': 'text-xl font-semibold mt-6 mb-3 text-purple-700',
    
    # Body text optimized for reading
    'p': 'text-lg leading-relaxed mb-6 text-gray-800',
    'a': 'text-indigo-600 hover:text-indigo-800 underline decoration-2 decoration-indigo-200 hover:decoration-indigo-500 transition-all duration-300',
    
    # Lists with improved spacing and subtle markers
    'ul': 'space-y-3 mb-6 ml-6 text-lg text-gray-800 list-disc marker:text-indigo-400',
    'ol': 'space-y-3 mb-6 ml-6 text-lg text-gray-800 list-decimal marker:text-indigo-400',
    'li': 'leading-relaxed pl-2',
    
    # Code blocks with modern styling
    'pre': 'bg-indigo-50 rounded-xl p-6 mb-6 shadow-inner overflow-x-auto border border-indigo-100',
    'code': 'bg-indigo-50 px-2 py-0.5 rounded-md text-indigo-700 font-mono text-sm',
    'pre code': 'bg-transparent p-0 text-gray-800 font-mono text-sm block',
    
    # Blockquotes with gradient border
    'blockquote': '''
        pl-6 border-l-4 border-gradient-to-b from-indigo-400 to-purple-400 
        italic mb-6 text-gray-700 py-2 bg-gradient-to-r from-purple-50 to-transparent
    ''',
    
    # Tables with consistent styling
    'table': '''
        w-full mb-6 border-collapse border border-indigo-200 rounded-lg overflow-hidden
        bg-white shadow-sm
    ''',
    'th': '''
        bg-gradient-to-r from-indigo-50 to-purple-50 
        p-4 text-left font-semibold text-indigo-700 border-b border-indigo-200
    ''',
    'td': 'p-4 border-b border-indigo-100 text-gray-700',
    
    # Horizontal rule with subtle gradient
    'hr': '''
        my-12 h-px bg-gradient-to-r from-transparent via-indigo-200 to-transparent
        border-0 opacity-70
    ''',
    
    # Images with consistent styling
    'img': '''
        max-w-full h-auto rounded-xl shadow-lg mb-6 
        border-2 border-indigo-100 hover:shadow-xl transition-shadow duration-300
    '''}

def apply_classes(html_str:str, # Html string
                  class_map=class_map, # Class map
                 )->str: # Html string with classes applied
    "Apply classes to html string"
    if not html_str: return html_str
    try:
        html_str = html.fromstring(html_str)
        for selector, classes in class_map.items():
            # Handle descendant selectors (e.g., 'pre code')
            xpath = '//' + '/descendant::'.join(selector.split())
            for element in html_str.xpath(xpath):
                existing_class = element.get('class', '')
                new_class = f"{existing_class} {classes}".strip()
                element.set('class', new_class)
        return etree.tostring(html_str, encoding='unicode', method='html')
    except etree.ParserError:
        return html_str

def render_md(md_content:str, # Markdown content
               class_map=class_map, # Class map
              )->FT: # Rendered markdown
    "Renders markdown using mistletoe and lxml"
    if md_content=='': return md_content
    # Check for required dependencies        
    html_content = mistletoe.markdown(md_content) #, mcp.PygmentsRenderer)
    return NotStr(apply_classes(html_content, class_map))
