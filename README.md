# Azure Natural Language Agent


This project allows you to interact with **Azure resources** using **plain English** through the **OpenAI's Agent SDK** and **Google Gemini**. It provides an easy-to-use interface for querying **Azure Key Vaults**, **Resource Groups**, and other Azure resources in a simple, natural language format.

## Features:
- Use natural language to query **Azure resources**.
- Used **Google Gemini LLM** for natural language processing.
- Fetch **Azure resources** like Key Vaults and Resource Groups through **Azure SDK for Python**.
- Runs via **CLI** and an interactive **Streamlit Web Interface**.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7+ 
- **Azure CLI** for authentication (Follow the installation guide: [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli))
- **Streamlit** for the web interface (Run `pip install streamlit` if needed)
- **Google Gemini API Key** (Sign up for Gemini API access)




## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/azure-agent.git
    cd azure-agent
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables in `.env` file:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    AZURE_SUBSCRIPTION_ID=your_azure_subscription_id_here
    ```

4. Run the agent via CLI:
    ```bash
    python app.py ask "How many Key Vaults do I have?"
    ```

5. Alternatively, run the Streamlit Web interface:
    ```bash
    streamlit run streamlit_app.py
    ```

---

### **Project Screenshot**

![List Resource Groups](images/list-resource-groups.png)
![List Key Vaults](images/list-key-vaults.png)

## License
MIT License
