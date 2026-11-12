# GitHub API Integration

A small integration that uses the [GitHub REST API](https://docs.github.com/rest) to list and summarize a user's public repositories.

## Usage

```bash
python list_repos.py octocat
```

## How it works

The script calls `GET /users/{user}/repos` and prints the repository name, star count, and primary language for the most recently updated repositories.

## Requirements

- Python 3.8+ (standard library only, no external dependencies)

## License

MIT
