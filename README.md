# ecommerce-recommender

Estrutura base para o Tech Challenge Fase 02 (Etapa 1: Clean Code e Estrutura).

## Estrutura de pastas

```text
.
├── configs/
│   ├── base.yaml
│   ├── mlflow.yaml
│   └── model.yaml
├── data/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   └── raw/
├── models/
├── src/
│   └── recommender/
│       ├── data/
│       ├── features/
│       ├── models/
│       ├── pipelines/
│       ├── training/
│       └── utils/
└── tests/
	├── integration/
	└── unit/
```

## Responsabilidade de cada pasta

- `src/`: codigo-fonte do projeto (logica de negocio e pipeline).
- `tests/`: testes unitarios e de integracao.
- `data/`: dados versionados e intermediarios do pipeline.
- `models/`: artefatos de modelo treinado (pesos, serializacoes, exportacoes).
- `configs/`: configuracoes declarativas (app, modelo, MLflow, paths).

## Convencoes recomendadas para a Etapa 1

- `src/recommender/pipelines/`: orquestracao de preprocessamento, treino e avaliacao.
- `src/recommender/models/`: definicao de arquitetura e factory para criar modelos.
- `src/recommender/features/`: transformacoes de features e estrategias de preprocessamento.
- `src/recommender/training/`: loops de treino, validacao e metricas.
- `src/recommender/utils/`: funcoes utilitarias pequenas e coesas.

Essa estrutura atende ao requisito de diretórios base e facilita evoluir para as proximas etapas (Poetry, Docker, DVC e MLflow).
