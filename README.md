# solucionAgenticaAZURE
IEBS-Desarrollo de una Solución de IA Generativa Agéntica con técnicas de RAG, evaluation y function calling

# Diagrama de Servicios Azure para Receta Pasta App

```mermaid
graph TD
  U[Usuario Web] -->|Interacción| A[App + Agente Conversacional]
  A -->|Llamadas HTTP| F[Azure Function: get_recipe]
  A -->|LLM / Embeddings| O[OpenAI]
  A -->|UI| S[Streamlit / Chatlit]
  A -->|Monitoreo| M[Azure Monitor]
  A -->|Telemetría| I[Application Insights]

  subgraph Infraestructura Azure
    F
    M
    I
  end
