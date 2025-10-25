# Linter Tool: Checks Python code for style violations

# --- DATA (The "Code" we are checking) ---
# A list of code lines, some are good, some are bad.
code_lines = [
    "if x > 5:",            # 0 spaces (OK)
    "y = 10;",              # 0 spaces, but semicolon (ERROR)
    "  for i in range(5):", # 2 spaces (OK)
    "  z = 20",             # 2 spaces (OK)
    "     def my_func():",  # 5 spaces (ERROR)
    "w = 30"                # 0 spaces (OK)
]

# --- 1. RECIPE: CHECK SEMICOLONS (Decision Recipe) ---
def check_semicolon(line):
    # We must first remove any leading or trailing whitespace before checking the last character
    trimmed_line = line.strip() 

    # If the line is empty after stripping, pass it (don't check)
    if not trimmed_line:
        return

    # Use negative indexing to check the LAST character
    if trimmed_line[-1] == ';':
        print(f"🚨 Line: '{line.strip()}' - LINTER ERROR: Unnecessary semicolon.")
    else:
        print(f"✅ Line: '{line.strip()}' - Semicolon check passed.")

# --- 2. RECIPE: CHECK INDENTATION (Repetition Recipe) ---
def check_indentation(line):
    # Skip checking empty lines
    if not line.strip():
        return
        
    space_count = 0
    i = 0  # This is our index, starting at the first character (0)

    # WHILE loop repeats AS LONG AS the current character is a space AND we haven't gone past the end of the line.
    while i < len(line) and line[i] == ' ':
        
        # A) Increment the space_count variable (count the space)
        space_count += 1 
        # B) Increment the index 'i' to look at the next character
        i += 1           

    # DECISION: Check if the count is valid (Python standard is 0 or 2 spaces)
    if space_count == 0 or space_count == 2:
        print(f"✅ Line: '{line.strip()}' - Indentation check passed ({space_count} spaces).")
    else:
        # We also check for tabs, which are 4 spaces, and flag those.
        print(f"❌ Line: '{line.strip()}' - LINTER ERROR: Indentation is {space_count} spaces. Should be 0 or 2.")

# --- 3. REPETITION RECIPE (Loop over all code lines) ---
print("--- Semicolon Check Running ---")

# Loop over the list of lines to run the first check
for code_line in code_lines:
    check_semicolon(code_line)
    
print("\n--- Indentation Check Running ---")

# Loop over the list of lines again to run the new check
for code_line in code_lines:
    check_indentation(code_line)
