# Space Reader

`space-reader` is a tool that can read a workspace URL and convert the content into LLM-friendly format.

## Installation

```shell
pip install sreader
```

## Usage

```python
from sreader import read

read("<workspace URL>")
```

## Support Workspace

- Local File (e.g., `/Users/user/desktop/demo.pdf`)
- Local Directory (e.g., `/Users/user/desktop/demo`)
- Remote File with Access (e.g., `https://example.com/demo.pdf`)
- GitHub Repo with Access (e.g., `https://github.com/user/demo`)

## Support Formats

#### Markdown

```python
read("<workspace URL>", format="markdown")

"""
## /Users/user/desktop/demo
- ****
  - a.py
  - c.py
  - b.py
  - **d**
    - g.py
    - **f**
      - f.py
  - **e**
"""
```

#### JSON and Dict

```python
read("<workspace URL>", format="json")  # or "dict"

"""
{
    "/Users/user/desktop/demo": {
        "files": [
            "a.py",
            "c.py",
            "b.py"
        ],
        "dirs": {
            "d": {
                "files": [
                    "g.py"
                ],
                "dirs": {
                    "f": {
                        "files": [
                            "f.py"
                        ],
                        "dirs": {}
                    }
                }
            },
            "e": {
                "files": [],
                "dirs": {}
            }
        }
    }
}
"""
```

#### Tree

```python
read("<workspace URL>", format="tree")

"""
/Users/user/desktop/demo
└── 
    ├── a.py
    ├── c.py
    ├── b.py
    ├── d
    │   ├── g.py
    │   └── f
    │       └── f.py
    └── e
"""
```

## Examples

- [Simple print](https://github.com/huangyz0918/space-reader/blob/main/example/simple.py)
- [File system Q&A Chatbot](https://github.com/huangyz0918/space-reader/blob/main/example/chatbot.py)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


