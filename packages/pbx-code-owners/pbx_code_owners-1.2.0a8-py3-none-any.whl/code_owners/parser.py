import subprocess  # nosec

import requests
import yaml

from code_owners import config


def load_codeowners() -> dict:
    with open(config.CODEOWNERS_FILE) as file:
        return yaml.safe_load(file)


def get_changed_paths() -> list[str]:
    current_branch_name = config.CI_COMMIT_BRANCH
    print(f"Current branch: {current_branch_name}")
    subprocess.run(["git", "fetch", "origin", "master:master"])  # nosec
    source_commit = (
        subprocess.run(  # nosec
            ["git", "merge-base", config.DEFAULT_BRANCH, current_branch_name],
            stdout=subprocess.PIPE,
        )
        .stdout.decode()
        .strip()
    )
    print(f"Source commit: {source_commit}")
    git_diff = subprocess.run(  # nosec
        ["git", "diff", "--name-only", source_commit], stdout=subprocess.PIPE
    )
    return git_diff.stdout.decode().splitlines()


def match_any_path(
    sub_paths: list[str], base_paths: list[str], excluded_paths: list[str]
) -> bool:
    if "." in base_paths:
        return True

    matched_paths = (
        sub_path
        for sub_path in sub_paths
        for base_path in base_paths
        if sub_path.startswith(base_path)
        and not any(
            sub_path.startswith(excluded_path) for excluded_path in excluded_paths
        )
    )
    try:
        next(matched_paths)
    except StopIteration:
        return False
    return True


def discussion_exists(content: str) -> bool:
    url = config.GITLAB_DISCUSSIONS_URL
    headers = {"PRIVATE-TOKEN": config.GITLAB_TOKEN}
    resp = requests.get(url, headers=headers, timeout=(3, 30))
    resp.raise_for_status()
    discussions = resp.json()
    filtered_discussions = (
        discussion
        for discussion in discussions
        if discussion["notes"][0]["body"] == content
    )
    try:
        next(filtered_discussions)
    except StopIteration:
        return False
    return True


def notify_owners(owners: str, section_name: str) -> None:
    owners_string = ", ".join(owners)
    content = f'Section "{section_name}" requires codeowner approval: {owners_string}'
    if discussion_exists(content):
        return

    url = config.GITLAB_DISCUSSIONS_URL
    headers = {"PRIVATE-TOKEN": config.GITLAB_TOKEN}
    resp = requests.post(url, headers=headers, json={"body": content}, timeout=(3, 30))
    resp.raise_for_status()


def main() -> None:
    codeowners = load_codeowners()
    print(f"Loaded config: {codeowners}")
    changed_paths = get_changed_paths()
    print(f"Changed paths: {changed_paths}")
    if not changed_paths:
        print("No changes, checking codeowners stopped")
        return

    for section in codeowners["sections"]:
        if match_any_path(changed_paths, section["paths"], section.get("exclude", [])):
            print(f"Matched section {section}")
            notify_owners(section["owners"], section["name"])
    return


if __name__ == "__main__":
    main()
