#!/usr/bin/env python3
"""List public repositories for a GitHub user using the GitHub REST API."""

import json
import sys
import urllib.request

API = "https://api.github.com"


def get_json(url):
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "github-api-integration",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main():
    user = sys.argv[1] if len(sys.argv) > 1 else "octocat"
    repos = get_json(f"{API}/users/{user}/repos?per_page=100&sort=updated")
    print(f"Public repositories for {user}: {len(repos)}")
    for repo in repos[:20]:
        print(
            f"- {repo['name']} "
            f"({repo['stargazers_count']} stars, {repo['language'] or 'unknown'})"
        )


if __name__ == "__main__":
    main()
