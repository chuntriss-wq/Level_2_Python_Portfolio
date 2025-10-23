# 1. THE LINTER FUNCTION (Updated with Colon Check)
def check_code_for_errors(code_snippet):
    warnings = []
    # Strip any leading/trailing whitespace from the whole snippet
    code_snippet = code_snippet.strip() 
    code_lines = code_snippet.split('\n') # Split the code into a list of lines

    # --- A. Check 1: Missing Imports (First non-empty line) ---
    first_line = code_lines[0].strip()
    if first_line and not first_line.startswith('import') and not first_line.startswith('#'):
        warnings.append("WARNING: Missing essential 'import' statement. Did you forget 'import requests'?")

    # --- B & C. Check 2 & 3: Syntax Errors in Line Breaks ---
    for i, line in enumerate(code_lines):
        line_content = line.strip()

        # Check for function/block starters (def, if, for)
        if line_content.startswith('def ') or line_content.startswith('if ') or line_content.startswith('for '):
            
            # --- C. Check 3: Missing Colon ---
            if not line_content.endswith(':'):
                warnings.append(f"ERROR: Line {i + 1} ('{line_content}') is missing a colon (:) at the end.")

            # --- B. Check 2: Indentation Error after a Block Start ---
            # Checks if the line after is NOT indented and NOT empty (only check if colon is present to avoid double reporting)
            elif line_content.endswith(':'): 
                if i + 1 < len(code_lines) and not code_lines[i + 1].startswith(' ') and code_lines[i + 1].strip():
                    warnings.append(f"ERROR: Line {i + 2} (after '{line_content}') is not indented. Check for missing spaces!")

    return warnings # Return the list of errors found

# 2. THE FAKE CODE TO DEBUG (This code now has THREE errors)
code_to_check = """
# This code simulates a student's submission.
# It is missing an import, a colon, and has an indentation error.
def check_status(health)
    if health < 100:
    print("Health Low")
    """

# 3. RUN THE DEBUGGING TOOL
results = check_code_for_errors(code_to_check)

# 4. OUTPUT THE RESULTS
if results:
    print("--- Debugging Tool Report ---")
    for warning in results:
        print(f"- {warning}")
    print("--- FIX THESE ERRORS! ---")
else:
    print("PASS: No common errors found.")
   

