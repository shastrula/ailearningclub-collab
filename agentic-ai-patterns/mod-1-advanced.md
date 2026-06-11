# Advanced Agentic Patterns: Routing, Orchestration & MCP

**Duration:** 15 min

## Advanced Techniques

Moving beyond basics, Advanced Agentic Patterns: Routing, Orchestration & MCP in agentic-ai-patterns involves sophisticated techniques used by expert practitioners.

The transition from basic to advanced skills lies in understanding the underlying principles deeply enough to adapt them to novel situations.

## Deep Dive: Advanced Agentic Patterns: Routing, Orchestration & MCP

**Optimization Strategies** - Professional systems optimize Advanced Agentic Patterns: Routing, Orchestration & MCP across multiple dimensions: performance, correctness, maintainability, and cost. These tradeoffs aren't academic—they determine whether systems work in production.

**Scaling Patterns** - Techniques that work for small datasets often fail at scale. Understanding how to architect systems that grow reliably is what separates junior from senior engineers.

**Integration Architecture** - Real systems combine Advanced Agentic Patterns: Routing, Orchestration & MCP with many other components. Managing these dependencies while maintaining quality is a core challenge.

## Performance Considerations

Measuring and optimizing Advanced Agentic Patterns: Routing, Orchestration & MCP:
- Profile your system to find actual bottlenecks
- Benchmark competing approaches on your real data
- Understand the cost-benefit of each optimization
- Document your design decisions

## Production Deployment

Getting Advanced Agentic Patterns: Routing, Orchestration & MCP into production safely requires:
- Thorough testing with realistic data
- Gradual rollout to detect issues early
- Comprehensive monitoring to catch problems
- Clear procedures for rollback if needed

## Advanced Patterns

Expert practitioners use these patterns:
- Canary deployments for safe rollouts
- Feature flags for easy rollbacks
- Circuit breakers for fault tolerance
- Graceful degradation under load

## Research Frontiers

Recent advances in Advanced Agentic Patterns: Routing, Orchestration & MCP:
- New techniques that improve performance
- Better tools that reduce complexity
- Theoretical insights enabling new applications
- Industry reports documenting lessons learned

## Hands-On Mastery

True mastery comes from implementing Advanced Agentic Patterns: Routing, Orchestration & MCP in realistic scenarios, encountering problems, debugging them, and learning from experience.


## Code Examples

```python
# Naive approach: LLM decides every time
def naive_agent(query):
    response = llm.invoke(f"Use tools to answer: {query}")
    # Slow, expensive, unreliable
    return response
```

```python
from enum import Enum
import json

class AgentType(Enum):
    SEARCH = "search"
    CALCULATOR = "calculator"
    DATABASE = "database"
    SUMMARIZER = "summarizer"

def route_query(query: str) -> AgentType:
    """Route query to appropriate agent"""
    routing_prompt = f"""
    Classify this query into ONE category:
    - SEARCH: Information retrieval, web queries
    - CALCULATOR: Math, computations
    - DATABASE: Data lookups, SQL queries
    - SUMMARIZER: Text summarization, analysis
    
    Query: {query}
    
    Respond with ONLY the category name.
    """
    
    response = llm.invoke(routing_prompt)
    category = response.strip().upper()
    return AgentType[category]

# Specialized agents
class SearchAgent:
    def run(self, query):
        results = search_api.query(query)
        return f"Found {len(results)} results: {results[:3]}"

class CalculatorAgent:
    def run(self, query):
        # Extract math expression and compute
        expr = extract_math(query)
        return f"Result: {eval(expr)}"

class DatabaseAgent:
    def run(self, query):
        sql = llm.invoke(f"Convert to SQL: {query}")
        return db.execute(sql)

# Router
agents = {
    AgentType.SEARCH: SearchAgent(),
    AgentType.CALCULATOR: CalculatorAgent(),
    AgentType.DATABASE: DatabaseAgent(),
}

def intelligent_agent(query):
    agent_type = route_query(query)
    agent = agents[agent_type]
    return agent.run(query)

# Test
print(intelligent_agent("What is 2 + 2?"))  # → CalculatorAgent
print(intelligent_agent("Find AI news"))     # → SearchAgent
```

```python
from typing import List
import asyncio

class WorkerAgent:
    def __init__(self, name: str, expertise: str):
        self.name = name
        self.expertise = expertise
    
    async def execute(self, task: str) -> str:
        """Execute task within expertise"""
        prompt = f"""
        You are {self.name}, expert in {self.expertise}.
        Task: {task}
        Provide a focused, expert response.
        """
        return await llm.ainvoke(prompt)

class ManagerAgent:
    def __init__(self, workers: List[WorkerAgent]):
        self.workers = workers
    
    async def decompose(self, goal: str) -> List[str]:
        """Break goal into subtasks"""
        prompt = f"""
        Break this goal into 3-5 independent subtasks:
        Goal: {goal}
        
        Format as JSON:
        {{"subtasks": ["task1", "task2", ...]}}
        """
        response = await llm.ainvoke(prompt)
        return json.loads(response)["subtasks"]
    
    async def orchestrate(self, goal: str) -> str:
        """Coordinate workers to achieve goal"""
        # Step 1: Decompose
        subtasks = await self.decompose(goal)
        
        # Step 2: Assign to workers
        tasks = []
        for i, subtask in enumerate(subtasks):
            worker = self.workers[i % len(self.workers)]
            tasks.append(worker.execute(subtask))
        
        # Step 3: Execute in parallel
        results = await asyncio.gather(*tasks)
        
        # Step 4: Synthesize
        synthesis_prompt = f"""
        Synthesize these results into a coherent answer:
        {json.dumps(dict(zip(subtasks, results)))}
        """
        return await llm.ainvoke(synthesis_prompt)

# Usage
workers = [
    WorkerAgent("DataAnalyst", "data analysis and statistics"),
    WorkerAgent("Engineer", "system design and architecture"),
    WorkerAgent("Researcher", "literature review and trends"),
]

manager = ManagerAgent(workers)

# Run
result = asyncio.run(manager.orchestrate(
    "Design a scalable ML inference system"
))
print(result)
```

```python
# Without MCP: Each tool has different interface
def use_calculator(expr):
    return eval(expr)

def use_search(query):
    return search_api.query(query)

def use_database(sql):
    return db.execute(sql)

# LLM must learn each interface → fragile
```

```python
from typing import Any, Dict
import json

class MCPTool:
    """Model Context Protocol Tool"""
    def __init__(self, name: str, description: str, schema: Dict):
        self.name = name
        self.description = description
        self.schema = schema  # JSON Schema for inputs
    
    def invoke(self, params: Dict) -> str:
        """Execute tool with validated params"""
        raise NotImplementedError

class CalculatorTool(MCPTool):
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Perform mathematical calculations",
            schema={
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression (e.g., '2 + 2')"
                    }
                },
                "required": ["expression"]
            }
        )
    
    def invoke(self, params: Dict) -> str:
        try:
            result = eval(params["expression"])
            return json.dumps({"result": result, "error": None})
        except Exception as e:
            return json.dumps({"result": None, "error": str(e)})

class SearchTool(MCPTool):
    def __init__(self):
        super().__init__(
            name="search",
            description="Search the web for information",
            schema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max results (default 5)"
                    }
                },
                "required": ["query"]
            }
        )
    
    def invoke(self, params: Dict) -> str:
        results = search_api.query(params["query"], limit=params.get("limit", 5))
        return json.dumps({"results": results, "error": None})

# Tool registry
tools = {
    "calculator": CalculatorTool(),
    "search": SearchTool(),
}

# LLM uses standardized interface
def mcp_agent(query: str) -> str:
    """Agent using MCP tools"""
    messages = [{"role": "user", "content": query}]
    
    # Tell LLM about available tools
    tools_description = json.dumps([
        {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.schema
        }
        for tool in tools.values()
    ])
    
    system_prompt = f"""
    You have access to these tools:
    {tools_description}
    
    When you need to use a tool, respond with:
    <tool_use>
    {{"name": "tool_name", "params": {{...}}}}
    </tool_use>
    """
    
    response = llm.invoke(system_prompt + query)
    
    # Parse tool calls
    if "<tool_use>" in response:
        tool_call = json.loads(response.split("<tool_use>")[1].split("</tool_use>")[0])
        tool = tools[tool_call["name"]]
        result = tool.invoke(tool_call["params"])
        return f"Tool result: {result}"
    
    return response

# Test
print(mcp_agent("What is 2 + 2?"))
print(mcp_agent("Search for AI news"))
```

## Practice in Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main/agentic-ai-patterns/mod-1-advanced.ipynb)

