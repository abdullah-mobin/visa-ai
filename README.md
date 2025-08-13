# visa-ai
voice based ai <hr>

### requirements

- linux pc
- downloaded ollama (https://ollama.com/download)
- a LLM from ollama (https://ollama.com/models)
- install dependencies from requirements.txt

### how to run

- install ollama
```
curl -fsSL https://ollama.com/install.sh | sh
```

- get model
```
ollama pull llama3.2:1b
```

- clone the repo
```
git clone https://github.com/abdullah-mobin/visa-ai.git
```

- move to cloned dir

```
cd visa-ai 
```
- install requirements by pip
```
pip install -r requirement.txt
```

- move to api
```
cd api
```

- run in cli

```
python3 main.py 2> /dev/null
```

- u might create a .sh and add to bin
- find an example here: 
```
#!/bin/bash
cd your_path_here
source .VISA/bin/activate
cd api
python3 main.py 2> /dev/null
```