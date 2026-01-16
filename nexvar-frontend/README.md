# NexVar: Genomic Analysis Workspace

The **NexVar Frontend** is a high-precision, web-based interface designed to interact with the NexVar foundation model. It serves as the primary workbench for researchers to conduct variant effect prediction, visualize genomic data, and interpret model outputs alongside clinical databases.

## Platform Overview

This application bridges the gap between massive-scale computational biology (H100-accelerated inference) and accessible clinical research. It provides a visual environment for:

1.  **Variant Analysis**: Real-time scoring of Single Nucleotide Variants (SNVs) using the NexVar 7B/40B models.
2.  **Contextual Visualization**: Integration with UCSC Genome Browser APIs for reference sequence verification.
3.  **Comparative Genomics**: Side-by-side evaluation of Model Predictions (AI) vs. ClinVar Classifications (Biological Truth).
4.  **Gene Exploration**: Searchable interface for inspecting genes (e.g., *BRCA1*, *TP53*) and their known pathogenic variants.

## Technical Architecture

Built on the [T3 Stack](https://create.t3.gg/), the platform prioritizes type safety, performance, and scientific accuracy.

-   **Framework**: [Next.js](https://nextjs.org) (App Router) for server-side rendering and rapid data fetching.
-   **Styling System**: [Tailwind CSS](https://tailwindcss.com) + [Shadcn UI](https://ui.shadcn.com) for a clean, distraction-free research aesthetic.
-   **Data Interchange**: Strictly typed API layers ensuring data integrity between the Python backend and React frontend.

## Deployment Strategy

The frontend is architected for stateless deployment on **Railway**, decoupling the user interface from the heavy-compute backend.

### Prerequisites
-   **Active Backend**: A running instance of the NexVar Inference Engine (deployed on Modal).
-   **API Endpoint**: The `https://...modal.run` URL from your backend deployment.

### Railway Deployment Guide

1.  **Repository Association**: Connect this repository (`nexvar-frontend`) to a new Railway project.
2.  **Environment Configuration**:
    -   `NEXT_PUBLIC_API_URL`: Set this to your Modal Backend Endpoint.
3.  **Build Pipeline**:
    -   Build Command: `npm run build`
    -   Start Command: `npm run start`

## Development Environment

To contribute to the workspace implementation:

```bash
# Install dependencies
npm install

# Start development server
# Ensure your local or remote backend is active
npm run dev
```

---
*Part of the NexVar Project: Genome modeling and design across all domains of life.*
