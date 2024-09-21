import os
import sys
import subprocess
import importlib.util

def check_file_exists(filename):
    return os.path.exists(filename)

def check_branch_exists(branch_name):
    result = subprocess.run(['git', 'branch', '--list', branch_name], capture_output=True, text=True)
    return branch_name in result.stdout

def check_pull_request():
    # This is a simplified check. In a real scenario, you'd use GitHub API.
    return os.path.exists('.git/PULL_REQUEST_MSGNUM')

def check_merge_conflict_resolved():
    result = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=U'], capture_output=True, text=True)
    return result.stdout.strip() == ''

def check_readme_updated():
    with open('README.md', 'r') as f:
        content = f.read()
    return 'New Feature' in content or 'new feature' in content

def check_project_board():
    # This is a simplified check. In a real scenario, you'd use GitHub API.
    return os.path.exists('.github/projects/1')

def check_game_implementation():
    spec = importlib.util.spec_from_file_location("snake_game", "src/snake_game.py")
    snake_game = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(snake_game)
    
    game = snake_game.SnakeGame()
    
    # Check if key methods are implemented
    methods_to_check = ['move_snake', 'change_direction', 'is_collision', 'update', 'draw']
    for method in methods_to_check:
        if getattr(game, method).__code__.co_code == b'd\x00S\x00':
            print(f"Method {method} is not implemented.")
            return False
    
    # Run the game for a few steps to check basic functionality
    for _ in range(10):
        game.update()
    
    return game.score >= 0 and len(game.snake) > 0

def main():
    checks = {
        "Snake game file exists": check_file_exists("src/snake_game.py"),
        "Feature branch exists": check_branch_exists("feature/new-feature"),
        "Pull request created": check_pull_request(),
        "Merge conflicts resolved": check_merge_conflict_resolved(),
        "README.md updated": check_readme_updated(),
        "Project board created": check_project_board(),
        "Game implementation": check_game_implementation()
    }

    all_passed = True
    for check, result in checks.items():
        status = "Passed" if result else "Failed"
        print(f"{check}: {status}")
        if not result:
            all_passed = False

    if all_passed:
        print("\nCongratulations! All checks passed.")
    else:
        print("\nSome checks failed. Please review and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
