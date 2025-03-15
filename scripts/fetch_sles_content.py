import os
import subprocess

SLES_REPO_URL = "<https://github.com/SUSE/release-notes>"
SLES_BRANCH = "main"
SLES_CONTENT_FILE = "release-notes.adoc"
LEAP_CONTENT_FILE = "leap-release-notes.adoc"

def clone_sles_repo():
    if not os.path.exists("sles-release-notes"):
        subprocess.run(["git", "clone", SLES_REPO_URL, "sles-release-notes"])
    else:
        subprocess.run(["git", "-C", "sles-release-notes", "pull"])

def fetch_sles_content():
    with open(f"sles-release-notes/{SLES_CONTENT_FILE}", "r") as sles_file:
        sles_content = sles_file.read()
    return sles_content

def merge_content(sles_content):
    with open(LEAP_CONTENT_FILE, "a") as leap_file:
        leap_file.write("\\n\\n")
        leap_file.write("== SLES Release Notes\\n")
        leap_file.write(sles_content)

def main():
    clone_sles_repo()
    sles_content = fetch_sles_content()
    merge_content(sles_content)

if __name__ == "__main__":
    main()
