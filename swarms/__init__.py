"""Swarms - A framework for orchestrating multi-agent AI systems.

This package provides tools for building, managing, and deploying
swarms of AI agents that can collaborate to solve complex tasks.
"""

from swarms.agents import Agent
from swarms.swarms import (
    BaseSwarm,
    SequentialWorkflow,
    ConcurrentWorkflow,
    MixtureOfAgents,
)
from swarms.memory import (
    BaseMemory,
    ConversationMemory,
)
from swarms.models import (
    BaseLLM,
    OpenAIChat,
)
from swarms.utils.loguru_logger import logger

__version__ = "0.1.0"
__author__ = "Swarms Team"
__license__ = "MIT"

__all__ = [
    # Core agent
    "Agent",
    # Swarm orchestration
    "BaseSwarm",
    "SequentialWorkflow",
    "ConcurrentWorkflow",
    "MixtureOfAgents",
    # Memory
    "BaseMemory",
    "ConversationMemory",
    # Models
    "BaseLLM",
    "OpenAIChat",
    # Utilities
    "logger",
    # Metadata
    "__version__",
    "__author__",
    "__license__",
]
