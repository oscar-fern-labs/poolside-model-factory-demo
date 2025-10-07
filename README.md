# 🏭 Poolside Model Factory Demo

A comprehensive proof-of-concept demonstration of Poolside's Model Factory architecture with enhanced metrics and interactive LLM playground.

## 🌟 Live Demo

**🔗 Enhanced Frontend:** https://webapp-morphvm-1y1tpw5s.http.cloud.morph.so
**🔗 Backend API:** https://backend-morphvm-1y1tpw5s.http.cloud.morph.so

### 🎯 Enhanced Demo Features

#### 📊 **Interactive Dashboard Tabs**
- **Factory Overview**: Real-time stats, pipeline visualization, repository grid
- **Enhanced Metrics**: Comprehensive system monitoring across all components
- **LLM Playground**: Interactive chat with trained CodeLLM models
- **Live Experiments**: Real-time training progress with detailed metrics

#### 🔥 **Enhanced Metrics Dashboard**
- **Titan Training Engine**: GPU utilization (88%), throughput (1474 tokens/sec), training efficiency (85.9%)
- **Atlas Inference Engine**: Request rates (176 req/sec), latency (151ms), cache hit rate (77.3%)
- **Data Pipeline Analytics**: Throughput (867.5 GB/h), processing accuracy (95.11%), quality score (95.5%)
- **System Health**: Uptime (2364 hours), availability (99.5%), error rate (0.85%)

#### 🤖 **LLM Playground Features**
- **5 Trained CodeLLM Models**: React (92.5%), Vue (90.6%), Django (87.9%), Flask (87.1%), Express (80.9%)
- **Interactive Chat Interface**: Real-time conversations with model selection
- **Model Capabilities**: Code generation, explanations, debugging, optimization
- **Response Metrics**: Processing time, confidence scores, response length tracking

#### 🚀 **Core Demo Features**
- **One-Click Demo**: Start 5 CodeLLM training experiments instantly
- **Live Experiments**: Progress tracking with loss/accuracy metrics  
- **Auto-Refresh**: Updates every 5 seconds for real-time monitoring
- **Model Factory Pipeline**: Visual 5-stage workflow (Data → Titan → Atlas → Code → Evaluation)

## 🚀 Quick Start

1. Visit the Frontend Dashboard above
2. Click "🚀 Start Quick Demo"
3. Watch the Model Factory pipeline activate
4. See 5 training experiments start automatically
5. Monitor real-time progress and metrics

## 🏗️ Architecture

Based on Poolside's Model Factory blog series, implementing:

- **🔧 Data Pipeline** - Repository ingestion and processing
- **⚡ Titan Training** - Distributed GPU training simulation  
- **🚀 Atlas Inference** - Code generation and inference
- **💻 Code Execution** - Containerized testing environment
- **📊 Evaluation** - Automated benchmarking framework

## 📁 Sample Data

10 popular repositories included:
React, Vue, Django, Flask, Express, TensorFlow, PyTorch, NumPy, Pandas, Kubernetes

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python, asyncio
- **Frontend**: HTML5, CSS3, Vanilla JavaScript with glassmorphism design
- **Database**: PostgreSQL (Neon) integration ready
- **Deployment**: Containerized services

## 🔌 Enhanced API Endpoints

### Core Factory APIs
- `GET /api/factory/stats` - Factory overview with model accuracy metrics
- `GET /api/experiments` - Live training experiments with progress tracking
- `POST /api/factory/quick-demo` - Start 5 training experiments instantly
- `GET /api/repositories` - 10 sample repositories with quality metrics

### New Enhanced APIs
- `GET /api/metrics/performance` - Comprehensive system metrics (Titan, Atlas, Pipeline, Health)
- `GET /api/available-models` - Trained CodeLLM models with capabilities
- `POST /api/chat` - Interactive LLM chat with model selection and metrics

### API Response Examples
```json
// Enhanced Performance Metrics
{
  "titan_metrics": {
    "active_training_jobs": 0,
    "avg_throughput_tokens_per_sec": 1474,
    "gpu_cluster_utilization": 0.88,
    "distributed_training_efficiency": 0.859,
    "memory_efficiency": 0.82
  },
  "atlas_metrics": {
    "inference_requests_per_sec": 176,
    "avg_latency_ms": 151,
    "model_serving_nodes": 11,
    "cache_hit_rate": 0.773,
    "concurrent_users": 177
  }
}

// LLM Chat Response
{
  "response": "Here's a React component solution...",
  "conversation_id": 8,
  "model_id": 1,
  "metrics": {
    "response_length": 304,
    "processing_time_ms": 938,
    "confidence": 0.89
  }
}
```

## 📊 Enhanced Features

### 🎯 **Core Features**
- Real-time factory statistics dashboard with 4-tab interface
- Interactive pipeline visualization with stage animations
- Live experiment tracking with detailed progress metrics
- One-click demo launching 5 simultaneous training experiments
- Auto-refresh functionality every 5 seconds for live data

### 🔥 **Enhanced Features**
- **Comprehensive Metrics Dashboard**: 4 metric categories (Titan, Atlas, Pipeline, Health)
- **LLM Playground**: Interactive chat with 5 trained CodeLLM models
- **Model Selection**: Choose from React, Vue, Django, Flask, Express specialists
- **Real-time Chat**: Processing time, confidence scores, response metrics
- **Advanced UI**: Tabbed interface with enhanced glassmorphism design

### 🤖 **LLM Capabilities**
- **Code Generation**: Create functions, classes, components
- **Code Explanation**: Understand complex algorithms and patterns
- **Debugging**: Find and fix code issues with AI assistance
- **Optimization**: Performance improvements and best practices

## 🎨 Enhanced UI Design

- **Modern Tab Interface**: 4-section dashboard (Overview, Metrics, Playground, Experiments)
- **Enhanced Glassmorphism**: Advanced blur effects with better transparency
- **Interactive Chat UI**: Professional messaging interface with avatars
- **Responsive Metrics**: Grid-based metric cards with hover effects
- **Real-time Indicators**: Live progress bars, spinners, and status badges
- **Advanced Animations**: Smooth transitions and loading states

Built as a technical demonstration of modern ML infrastructure patterns and contemporary web design.

---

**License**: MIT | **Created**: October 2025 | **Status**: ✅ Complete & Deployed

## 🆕 Latest Enhancements

### 🤖 Interactive LLM Playground
- **Chat Interface**: Interactive conversations with trained CodeLLM models
- **Model Selection**: Choose from specialized models based on repository training data
- **Real-time Metrics**: Response time, confidence scores, and detailed processing metrics
- **Code Capabilities**: Generate functions, explain algorithms, debug code, optimize solutions
- **Smart Context**: Models provide repository-specific insights and coding best practices

### 📊 Advanced Performance Analytics
- **Titan Training Metrics**: GPU cluster utilization, distributed training efficiency, memory usage
- **Atlas Inference Analytics**: Request throughput, latency distribution, cache performance
- **Data Pipeline Insights**: Processing accuracy, deduplication rates, quality scores
- **System Health Dashboard**: Uptime tracking, error rates, availability monitoring
- **Real-time Visualization**: Live charts and performance trends

### 🎯 Enhanced API Endpoints
- `POST /api/chat` - Interactive LLM conversations with model selection
- `GET /api/available-models` - List of trained models ready for interaction
- `GET /api/metrics/performance` - Comprehensive system performance data
- `GET /api/experiments/{id}/metrics` - Detailed training metrics and evaluation scores

### 💬 LLM Chat Examples
```bash
# Chat with a trained model
curl -X POST https://backend-morphvm-1y1tpw5s.http.cloud.morph.so/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Write a Python function for binary search", "model_id": 1}'

# Get available models
curl https://backend-morphvm-1y1tpw5s.http.cloud.morph.so/api/available-models

# Get performance metrics
curl https://backend-morphvm-1y1tpw5s.http.cloud.morph.so/api/metrics/performance
```

