# Linter Tool: Checks Python code for style violations

# --- DATA (The "Code" we are checking) ---
# A list of code lines, some are good, some are bad.
code_lines = [
    "if x > 5:",        # Good line
    "y = 10;",          # BAD: Has unnecessary semicolon
    "  for i in range(5):", # Good line (indented for loop)
    "z = 20"            # Good line (no semicolon needed)
]

# --- RECIPE: CODE REUSABILITY (Function) ---

def check_semicolon(line):
    # Use negative indexing to check the LAST character
    
    # We must first remove any leading or trailing whitespace before checking the last character
    line = line.strip() 

    # --- DECISION RECIPE: IF BLOCK ---
    if line[-1] == ';':
        # FIX: Using '{line}' correctly displays the content of the 'line' variable
        print(f"🚨 Line: '{line}' - LINTER ERROR: Unnecessary semicolon.")
    else:
        # --- DECISION RECIPE: ELSE BLOCK ---
        # FIX: Using '{line}' correctly displays the content of the 'line' variable
        print(f"✅ Line: '{line}' - Semicolon check passed.")

# --- REPETITION RECIPE (Loop over all code lines) ---
print("--- Semicolon Check Running ---")

# Loop over the list of lines we defined above
for code_line in code_lines:
    check_semicolon(code_line)
    
    