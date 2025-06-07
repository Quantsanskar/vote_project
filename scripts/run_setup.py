import os
import subprocess
import sys

print("🚀 Setting up your Django Vote Tracker project...")

# Create static directories
static_dir = "static"
if not os.path.exists(static_dir):
    os.makedirs(static_dir)
    print(f"✅ Created {static_dir} directory")

# Create subdirectories for static files
subdirs = ["css", "js", "images"]
for subdir in subdirs:
    path = os.path.join(static_dir, subdir)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"✅ Created {path} directory")

# Create templates directory
templates_dir = "templates"
if not os.path.exists(templates_dir):
    os.makedirs(templates_dir)
    print(f"✅ Created {templates_dir} directory")

# Create vote_tracker directory if it doesn't exist
vote_tracker_dir = "vote_tracker"
if not os.path.exists(vote_tracker_dir):
    os.makedirs(vote_tracker_dir)
    print(f"✅ Created {vote_tracker_dir} directory")

# Create migrations directory
migrations_dir = os.path.join(vote_tracker_dir, "migrations")
if not os.path.exists(migrations_dir):
    os.makedirs(migrations_dir)
    print(f"✅ Created {migrations_dir} directory")

# Create __init__.py files
init_files = [
    os.path.join(vote_tracker_dir, "__init__.py"),
    os.path.join(migrations_dir, "__init__.py"),
    "vote_project/__init__.py"
]

for init_file in init_files:
    if not os.path.exists(init_file):
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(init_file), exist_ok=True)
        with open(init_file, "w") as f:
            f.write("# This file makes Python treat the directory as a package\n")
        print(f"✅ Created {init_file}")

print("\n🎉 Setup complete! Your project structure is ready.")
print("\n📋 Next steps:")
print("1. Run: python manage.py migrate")
print("2. Run: python manage.py runserver")
print("3. Visit: http://localhost:8000/ (voting page)")
print("4. Visit: http://localhost:8000/baby/ (girlfriend's page)")
print("\n💕 Your romantic vote tracker is ready to make her happy!")
