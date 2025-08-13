import subprocess

rules = "(response limit within 1 paragraphs, a paragraph can contain maximum 3 sentences, your name is veronicca)"

def query_ollama(prompt):
    # `ollama run llama3` must be preloaded
    process = subprocess.Popen(
        ["ollama", "run", "llama3.2:1b"],  # or whatever model you use
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=prompt+"\n"+rules)
    if stderr:
        print("Error:", stderr)
    return stdout.strip()
