# Azure Natural Language Agent

This agent allows you to query Azure resources in plain English using OpenAI's Agent SDK and Google Gemini.

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

## License
MIT License
