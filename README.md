# 🐍 Snake Game: Git & GitHub Workflow Assignment

Welcome to the Snake Game project! This assignment will guide you through a typical Git and GitHub workflow while building a classic Snake game. Let's slither into the world of collaborative coding! 🚀

## 🎯 Objectives

- Practice Git branching, committing, and merging
- Create and manage Pull Requests
- Handle merge conflicts
- Implement a simple Snake game in Python
- Use GitHub Projects for basic project management

## 🗺️ Assignment Roadmap

### 1. 🏁 Getting Started

1. Accept the GitHub Classroom assignment link
2. Clone your new repository:
   ```
   git clone [your-repo-url]
   cd [your-repo-name]
   ```

### 2. 📖 Project Setup

1. Read the `README.md` file carefully
2. Familiarize yourself with the `snake_game.py` file structure

### 3. 🌿 Feature Branch

1. Create a new branch for your feature:
   ```
   git checkout -b feature/snake-movement
   ```

### 4. 🖥️ Implement Game Logic

1. Open `snake_game.py`
2. Implement the following methods:
   - `move_snake()`
   - `change_direction()`
   - `is_collision()`
   - `update()`
   - `draw()`
3. Add user input handling in the `main()` function

### 5. 🧪 Testing

1. Run the game to ensure it works:
   ```
   python snake_game.py
   ```
2. Play your game! Make sure the snake moves, grows, and the game ends on collision

### 6. 💾 Commit Your Changes

1. Stage your changes:
   ```
   git add snake_game.py
   ```
2. Commit your changes:
   ```
   git commit -m "Implement snake movement and game logic"
   ```
3. Push your branch:
   ```
   git push origin feature/snake-movement
   ```

### 7. 🔀 Create a Pull Request

1. Go to your repository on GitHub
2. Click "Compare & pull request" for your `feature/snake-movement` branch
3. Fill in the PR description, explaining your changes
4. Create the Pull Request

### 8. 🤖 Code Review Simulation

1. Run the review bot:
   ```
   python review_bot.py
   ```
2. Address any feedback by making necessary changes
3. Commit and push any additional changes

### 9. 🔨 Handle Merge Conflicts

1. Generate a mock conflict:
   ```
   python conflict_generator.py
   ```
2. Resolve the conflict in `snake_game.py`
3. Stage, commit, and push the conflict resolution:
   ```
   git add snake_game.py
   git commit -m "Resolve merge conflict in game board size"
   git push origin feature/snake-movement
   ```

### 10. 📝 Update Documentation

1. Update `README.md` with information about your new feature
2. Commit and push the changes:
   ```
   git add README.md
   git commit -m "Update README with new feature description"
   git push origin feature/snake-movement
   ```

### 11. 🏁 Final Checks

1. Run the submission checker:
   ```
   python check_submission.py
   ```
2. Make sure all checks pass

### 12. 🎉 Merge the Pull Request

1. Go to your Pull Request on GitHub
2. If all checks pass, merge the PR into the main branch

### 13. 🧹 Clean Up

1. Switch back to the main branch:
   ```
   git checkout main
   ```
2. Pull the latest changes:
   ```
   git pull origin main
   ```

### 14. 📊 Project Management

1. Go to the Projects tab on GitHub
2. Move your task card to the "Done" column

## 🏆 Submission

Your work is submitted when:
- Your Pull Request is merged into the main branch
- All checks in `check_submission.py` pass
- Your README is updated with the new feature description

## 🆘 Need Help?

If you get stuck or have questions, don't hesitate to:
- Review the provided documentation
- Use Git's `--help` option for command details
- Reach out to your instructor or TAs

Happy coding, and may your snake grow long and prosper! 🐍✨
