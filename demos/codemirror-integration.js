// CodeMirror Integration for Demo Code Blocks
// Replaces complex HTML syntax highlighting with proper code editor display

(function () {
  'use strict';

  const CONFIG = {
    debug: true,
    cdnBase: 'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16',
  };

  function log(message) {
    if (CONFIG.debug) {
      console.log(`📝 CodeMirror Integration: ${message}`);
    }
  }

  // Load CodeMirror CSS and JS
  function loadCodeMirror() {
    return new Promise((resolve, reject) => {
      // Check if CodeMirror is already loaded
      if (window.CodeMirror) {
        log('CodeMirror already loaded');
        resolve();
        return;
      }

      // Load CSS first
      const css = document.createElement('link');
      css.rel = 'stylesheet';
      css.href = `${CONFIG.cdnBase}/codemirror.min.css`;
      document.head.appendChild(css);

      // Load theme CSS
      const theme = document.createElement('link');
      theme.rel = 'stylesheet';
      theme.href = `${CONFIG.cdnBase}/theme/dracula.min.css`;
      document.head.appendChild(theme);

      // Load main CodeMirror JS
      const script = document.createElement('script');
      script.src = `${CONFIG.cdnBase}/codemirror.min.js`;
      script.onload = () => {
        // Load language modes
        const modes = [
          'javascript/javascript.min.js',
          'css/css.min.js',
          'xml/xml.min.js', // For HTML
          'htmlmixed/htmlmixed.min.js',
        ];

        let loadedModes = 0;
        const totalModes = modes.length;

        modes.forEach((mode) => {
          const modeScript = document.createElement('script');
          modeScript.src = `${CONFIG.cdnBase}/mode/${mode}`;
          modeScript.onload = () => {
            loadedModes++;
            if (loadedModes === totalModes) {
              log('CodeMirror loaded successfully with all modes');
              resolve();
            }
          };
          modeScript.onerror = () => {
            loadedModes++;
            if (loadedModes === totalModes) {
              log('CodeMirror loaded (some modes failed)');
              resolve();
            }
          };
          document.head.appendChild(modeScript);
        });
      };
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }

  // Extract clean code from HTML spans
  function extractCode(htmlContent) {
    // Create a temporary element to parse HTML
    const temp = document.createElement('div');
    temp.innerHTML = htmlContent;

    // Try to extract text content, preserving structure
    let code = temp.textContent || temp.innerText || '';

    // Clean up and format with proper JavaScript structure
    code = code
      .replace(/\s+/g, ' ') // Normalize spaces first
      .replace(
        /\/\/\s*([^;{}]*?)(?=\s*(?:class|function|const|let|var|export|import|\w+\s*[=:]|\{|\}|$))/g,
        '// $1\n'
      ) // Comments before declarations
      .replace(/;\s*(?=\/\/)/g, ';\n') // Line break before comments after statements
      .replace(/;\s*(?=\w)/g, ';\n') // Line breaks after semicolons before code
      .replace(/{\s*(?!\s*})/g, '{\n  ') // Format opening braces (not empty objects)
      .replace(/}\s*(?=\w|\/\/)/g, '}\n\n') // Format closing braces with double line break
      .replace(/}\s*$/g, '}') // Clean closing brace at end
      .replace(/\n\s*\n\s*\n/g, '\n\n') // Max double newlines
      .replace(/^\s*\n|\n\s*$/g, '') // Remove leading/trailing empty lines
      .trim();

    // Fix indentation
    const lines = code.split('\n');
    let indentLevel = 0;
    const indentedLines = lines.map((line, index) => {
      const trimmed = line.trim();
      if (!trimmed) return '';

      // Decrease indent for closing braces
      if (trimmed.startsWith('}')) {
        indentLevel = Math.max(0, indentLevel - 1);
      }

      const indentedLine = '  '.repeat(indentLevel) + trimmed;

      // Increase indent after opening braces
      if (trimmed.endsWith('{')) {
        indentLevel++;
      }

      return indentedLine;
    });

    return indentedLines.join('\n');
  }

  // Convert code block to CodeMirror editor
  function convertCodeBlock(element, index) {
    try {
      const originalCode = extractCode(element.innerHTML);

      if (!originalCode.trim()) {
        log(`Block ${index} is empty, skipping`);
        return;
      }

      // Clear the original content
      element.innerHTML = '';

      // Determine language mode from data-lang attribute
      const lang = element.getAttribute('data-lang') || 'javascript';
      const modeMap = {
        js: 'javascript',
        javascript: 'javascript',
        html: 'htmlmixed',
        css: 'css',
        xml: 'xml',
      };
      const mode = modeMap[lang] || 'javascript';

      // Create CodeMirror instance
      const editor = CodeMirror(element, {
        value: originalCode,
        mode: mode,
        theme: 'dracula',
        lineNumbers: true,
        readOnly: true,
        lineWrapping: true,
        indentUnit: 2,
        tabSize: 2,
        styleActiveLine: false,
        matchBrackets: true,
        autoCloseBrackets: true,
        foldGutter: true,
        gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter'],
        extraKeys: {
          'Ctrl-Space': 'autocomplete',
        },
      });

      // Style the editor container
      element.style.border = '1px solid #404040';
      element.style.borderRadius = '8px';
      element.style.overflow = 'hidden';
      element.style.fontSize = '14px';

      // Adjust editor height based on content
      const lineCount = originalCode.split('\n').length;
      const height = Math.max(150, Math.min(400, lineCount * 20 + 40));
      editor.setSize(null, height);

      log(`Converted block ${index} with ${lineCount} lines`);
    } catch (error) {
      log(`Error converting block ${index}: ${error.message}`);
      // Keep original content on error
    }
  }

  // Convert all code blocks to CodeMirror
  function convertAllCodeBlocks() {
    const codeBlocks = document.querySelectorAll('.code-block[data-lang]');

    if (codeBlocks.length === 0) {
      log('No code blocks found');
      return;
    }

    log(`Converting ${codeBlocks.length} code blocks to CodeMirror`);

    codeBlocks.forEach((block, index) => {
      convertCodeBlock(block, index + 1);
    });

    log('Code block conversion complete');
  }

  // Initialize when DOM is ready
  function init() {
    log('Initializing CodeMirror integration...');

    loadCodeMirror()
      .then(() => {
        // Small delay to ensure DOM is ready
        setTimeout(convertAllCodeBlocks, 100);
      })
      .catch((error) => {
        log(`Failed to load CodeMirror: ${error.message}`);
        console.error('CodeMirror loading failed:', error);
      });
  }

  // Auto-initialize based on DOM state
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Make functions globally available for debugging
  window.CodeMirrorDemo = {
    convert: convertAllCodeBlocks,
    extractCode,
    config: CONFIG,
  };

  log('CodeMirror integration initialized');
})();
