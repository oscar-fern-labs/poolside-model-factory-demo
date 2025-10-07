from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio
import random
from datetime import datetime
from typing import Dict, List, Any
from pydantic import BaseModel

# Simple in-memory storage for demo
repositories = [
    {"id": 1, "name": "react", "url": "https://github.com/facebook/react", "description": "A JavaScript library for building user interfaces", "language": "JavaScript", "stars": 227000, "forks": 46000, "status": "available"},
    {"id": 2, "name": "vue", "url": "https://github.com/vuejs/vue", "description": "Progressive JavaScript framework", "language": "JavaScript", "stars": 207000, "forks": 33000, "status": "available"},
    {"id": 3, "name": "django", "url": "https://github.com/django/django", "description": "High-level Python web framework", "language": "Python", "stars": 78000, "forks": 31000, "status": "available"},
    {"id": 4, "name": "flask", "url": "https://github.com/pallets/flask", "description": "Lightweight Python web framework", "language": "Python", "stars": 67000, "forks": 16000, "status": "available"},
    {"id": 5, "name": "express", "url": "https://github.com/expressjs/express", "description": "Fast, unopinionated web framework for Node.js", "language": "JavaScript", "stars": 65000, "forks": 15000, "status": "available"},
    {"id": 6, "name": "tensorflow", "url": "https://github.com/tensorflow/tensorflow", "description": "An Open Source Machine Learning Framework", "language": "C++", "stars": 185000, "forks": 74000, "status": "available"},
    {"id": 7, "name": "pytorch", "url": "https://github.com/pytorch/pytorch", "description": "Tensors and Dynamic neural networks", "language": "Python", "stars": 82000, "forks": 22000, "status": "available"},
    {"id": 8, "name": "numpy", "url": "https://github.com/numpy/numpy", "description": "The fundamental package for scientific computing", "language": "Python", "stars": 27000, "forks": 9000, "status": "available"},
    {"id": 9, "name": "pandas", "url": "https://github.com/pandas-dev/pandas", "description": "Flexible and powerful data analysis", "language": "Python", "stars": 43000, "forks": 17000, "status": "available"},
    {"id": 10, "name": "kubernetes", "url": "https://github.com/kubernetes/kubernetes", "description": "Production-Grade Container Scheduling and Management", "language": "Go", "stars": 110000, "forks": 39000, "status": "available"}
]

experiments = []
training_jobs = []
evaluations = []
active_jobs = {}

app = FastAPI(
    title="Poolside Model Factory Demo",
    description="A proof of concept demo of Poolside's Model Factory architecture",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExperimentCreate(BaseModel):
    name: str
    repository_id: int
    model_architecture: str = "transformer"

@app.get("/")
async def root():
    return {"message": "Poolside Model Factory API", "version": "1.0.0"}

@app.get("/api/factory/stats")
async def get_factory_stats():
    active_training = len([job for job in training_jobs if job.get("status") == "running"])
    completed_experiments = [exp for exp in experiments if exp.get("status") == "completed"]
    avg_accuracy = sum([exp.get("accuracy", 0) for exp in completed_experiments]) / max(len(completed_experiments), 1)
    
    return {
        "total_repositories": len(repositories),
        "total_experiments": len(experiments),
        "active_training_jobs": active_training,
        "total_evaluations": len(evaluations),
        "avg_model_accuracy": avg_accuracy,
        "gpu_utilization": 0.7,
        "available_gpus": 300,
        "total_gpus": 1000
    }

@app.get("/api/repositories")
async def get_repositories():
    return repositories

@app.get("/api/experiments")
async def get_experiments():
    return experiments

@app.post("/api/experiments")
async def create_experiment(experiment: ExperimentCreate):
    exp_id = len(experiments) + 1
    new_experiment = {
        "id": exp_id,
        "name": experiment.name,
        "repository_id": experiment.repository_id,
        "model_architecture": experiment.model_architecture,
        "status": "preparing",
        "progress": 0.0,
        "loss": None,
        "accuracy": None,
        "created_at": datetime.utcnow().isoformat(),
        "config": {
            "hidden_size": 768,
            "num_layers": 12,
            "num_heads": 12,
            "vocab_size": 50257
        }
    }
    experiments.append(new_experiment)
    
    # Start training simulation
    asyncio.create_task(simulate_training(exp_id))
    
    return new_experiment

async def simulate_training(experiment_id: int):
    """Simulate training progress"""
    experiment = next((exp for exp in experiments if exp["id"] == experiment_id), None)
    if not experiment:
        return
    
    # Create training job
    job = {
        "id": len(training_jobs) + 1,
        "experiment_id": experiment_id,
        "status": "running",
        "current_step": 0,
        "total_steps": 1000,
        "gpu_count": random.randint(8, 64)
    }
    training_jobs.append(job)
    
    experiment["status"] = "running"
    experiment["started_at"] = datetime.utcnow().isoformat()
    
    # Simulate training steps
    for step in range(1000):
        await asyncio.sleep(0.1)  # Fast simulation
        
        job["current_step"] = step + 1
        progress = (step + 1) / 1000
        experiment["progress"] = progress
        experiment["loss"] = 4.0 * (1 - progress) + 0.5 + random.uniform(-0.2, 0.2)
        experiment["accuracy"] = min(0.95, progress * 0.8 + random.uniform(0, 0.15))
        
        if step % 100 == 0:  # Log every 100 steps
            print(f"Training {experiment['name']}: Step {step + 1}/1000, Loss: {experiment['loss']:.3f}")
    
    # Complete training
    job["status"] = "completed"
    experiment["status"] = "completed"
    experiment["completed_at"] = datetime.utcnow().isoformat()
    
    # Run evaluations
    benchmarks = ["HumanEval", "MBPP", "CodeT5", "RepoQA", "SWE-Bench"]
    for benchmark in benchmarks:
        eval_result = {
            "id": len(evaluations) + 1,
            "experiment_id": experiment_id,
            "benchmark_name": benchmark,
            "score": random.uniform(0.3, 0.9),
            "status": "completed"
        }
        evaluations.append(eval_result)
    
    print(f"Training completed for {experiment['name']}")

@app.get("/api/experiments/{experiment_id}")
async def get_experiment(experiment_id: int):
    experiment = next((exp for exp in experiments if exp["id"] == experiment_id), None)
    if not experiment:
        return {"error": "Experiment not found"}
    return experiment

@app.get("/api/experiments/{experiment_id}/evaluations")
async def get_experiment_evaluations(experiment_id: int):
    return [eval for eval in evaluations if eval["experiment_id"] == experiment_id]

@app.get("/api/training-jobs")
async def get_training_jobs():
    result = []
    for job in training_jobs:
        experiment = next((exp for exp in experiments if exp["id"] == job["experiment_id"]), None)
        result.append({
            **job,
            "experiment_name": experiment["name"] if experiment else "Unknown",
            "progress": job["current_step"] / job["total_steps"]
        })
    return result

@app.post("/api/factory/quick-demo")
async def run_quick_demo():
    """Start quick demo with sample experiments"""
    created_experiments = []
    
    for i, repo in enumerate(repositories[:5]):  # Use first 5 repos
        experiment = {
            "id": len(experiments) + 1,
            "name": f"CodeLLM_{repo['name']}_experiment",
            "repository_id": repo["id"],
            "model_architecture": "transformer",
            "status": "preparing",
            "progress": 0.0,
            "loss": None,
            "accuracy": None,
            "created_at": datetime.utcnow().isoformat(),
            "config": {
                "hidden_size": 768,
                "num_layers": 12,
                "num_heads": 12
            }
        }
        experiments.append(experiment)
        created_experiments.append(experiment)
        
        # Start training with delay
        asyncio.create_task(delayed_training(experiment["id"], i * 2))
    
    return {
        "message": "Quick demo started!",
        "experiments_started": len(created_experiments),
        "note": "Training will begin automatically. Check /api/factory/stats for progress."
    }

async def delayed_training(experiment_id: int, delay: int):
    await asyncio.sleep(delay)
    await simulate_training(experiment_id)

@app.get("/api/atlas/inference")
async def run_inference(prompt: str = "Write a function to sort an array"):
    """Simulate Atlas inference"""
    await asyncio.sleep(0.5)
    return {
        "response": f"# Generated code for: {prompt}\n\ndef solution():\n    return 'AI-generated solution'",
        "tokens_generated": random.randint(50, 200),
        "inference_time_ms": random.randint(100, 500),
        "confidence": random.uniform(0.7, 0.95)
    }

@app.post("/api/code/execute")
async def execute_code(data: dict):
    """Simulate code execution"""
    await asyncio.sleep(0.2)
    success = random.choice([True, True, True, False])
    return {
        "id": random.randint(1, 1000),
        "repository_id": data.get("repository_id", 1),
        "code_snippet": data.get("code_snippet", ""),
        "execution_result": "Test passed ✅" if success else "Test failed ❌",
        "success": success,
        "execution_time_ms": random.randint(50, 200),
        "created_at": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    print("🏭 Starting Poolside Model Factory Demo...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
