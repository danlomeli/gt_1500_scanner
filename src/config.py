"""
config.py: Configuration settings for the application.

This module contains various configuration settings and constants used throughout
the application. It defines file paths, hyperparameters, data settings, model settings,
logging settings, and more. The configuration settings can be easily modified to adapt
to different environments or requirements.

Usage:
    from config import DATA_DIR, LEARNING_RATE, MODEL_SAVE_PATH
"""

import os

# Project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Data directory
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

# Output directory for saved models, plots, etc.
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Random seed for reproducibility
RANDOM_SEED = 42

# Hyperparameters
LEARNING_RATE = 1e-3
BATCH_SIZE = 64
NUM_EPOCHS = 10
HIDDEN_SIZE = 128
DROPOUT = 0.5

# Data settings
TRAIN_SPLIT = 0.8  # 80% for training, 20% for validation
TARGET_COLUMN = "target"  # Name of the target column in your data

# Model settings
MODEL_NAME = "my_model"
MODEL_SAVE_PATH = os.path.join(OUTPUT_DIR, f"{MODEL_NAME}.pkl")

# Logging settings
LOG_FILE = os.path.join(OUTPUT_DIR, "logs.txt")
LOG_LEVEL = "INFO"  # Can be 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'

# Plotting settings
PLOT_STYLE = "seaborn-darkgrid"  # Matplotlib style for plots
PLOT_FIGSIZE = (8, 6)  # Default figure size for plots
PLOT_DPI = 300  # DPI for saving plots

# Experiment tracking
WANDB_PROJECT = "my_project"  # Weights & Biases project name
WANDB_ENTITY = "my_username"  # Weights & Biases entity (username or team name)

# Import API keys if available
SAM_API_KEY = os.getenv("SAM_API_KEY", "default_sam_api_key")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "default_openai_api_key")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "default_anthropic_api_key")
