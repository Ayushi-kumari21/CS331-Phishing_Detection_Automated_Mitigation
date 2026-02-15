# Software Architecture Design

## I. Selected Architecture Style

The most appropriate software architecture style for this project is the  
**Containerized Layered Modular Architecture**.

This architectural approach ensures:

- Clear separation of concerns across logical layers  
- High maintainability and scalability  
- Deployment consistency through containerization  
- Independent evolution of system components  

By combining a layered modular structure with containerized deployment, the system achieves both logical clarity and operational reliability.

---

## II. Granularity of Software Components

The system is divided into well-defined logical layers.  
Each layer has a clearly scoped responsibility to avoid tight coupling and promote maintainability.

---

### 1. API Layer

**Responsibilities:**
- Exposes RESTful endpoints to users and external services  
- Handles request routing and response formatting  
- Manages authentication and security validation  

**Granularity Design:**
- The layer is intentionally lightweight  
- It strictly focuses on communication and security  
- Business logic is not embedded here  

This separation ensures that changes to detection logic do not impact the API interface.

---

### 2. Business Logic Layer

**Responsibilities:**
- Implements core phishing detection workflows  
- Performs risk scoring  
- Conducts domain reputation checks  
- Integrates with external services (e.g., VirusTotal)  

**Granularity Design:**
- Each detection module is encapsulated as an independent component  
- Modules can evolve independently  
- Updating risk scoring logic does not affect authentication or API handling  

This modularity improves flexibility and long-term maintainability.

---

### 3. Data Persistence Layer

**Responsibilities:**
- Stores and retrieves user data  
- Manages phishing reports  
- Maintains threat intelligence records  

**Granularity Design:**
- All database operations are abstracted within this layer  
- Storage technology is decoupled from upper layers  

For example, switching from PostgreSQL to MongoDB would not impact the API or business logic layers.

---

## III. Role of Containerization

Beyond logical separation, the architecture is fully containerized using Docker.

### Infrastructure-Level Separation

Each major infrastructure component runs in its own isolated container:

- Backend server container  
- Database container  
- Future threat intelligence services container  

### Benefits of Containerization

- Deployment consistency across environments  
- Reproducibility of system setup  
- Easier debugging and service isolation  
- Independent scaling of components  
- Simplified updates and maintenance  

### Infrastructure Granularity

Each major service is packaged as a standalone container, enabling:

- Independent deployment  
- Version-controlled updates  
- Fault isolation  
- Horizontal scalability  

---
## Architecture Diagram
```mermaid
flowchart TB
    User[User/Client]

    subgraph APILayer["API Layer"]
        API[Fast API]
    end

    subgraph BusinessLayer["Service Layer"]
        Risk[Risk Engine]
        Authentication[Authentication]
        Threat[Threat Analyzer]
    end

    subgraph DataLayer["Data Layer"]
        DB[(DB)]
    end

    User --> API
    API --> Risk
    API --> Authentication
    API --> Threat
    Risk --> DB
   
