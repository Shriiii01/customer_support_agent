# Usage Examples

This document provides examples of how to use the Customer Support Agent.

## Basic Usage

1. **Start the application:**
   ```bash
   streamlit run main.py
   ```

2. **Enter your OpenAI API key** in the input field at the top

3. **Enter a Customer ID** in the sidebar (e.g., "CUST-12345")

4. **Start chatting** with the AI agent

## Generating Synthetic Data

To test the agent with realistic data:

1. Enter a customer ID
2. Click "Generate Synthetic Data" in the sidebar
3. Wait for the data generation to complete
4. Click "View Customer Profile" to see the generated data
5. Start chatting - the agent will use this context

## Viewing Memory

To see what the agent remembers:

1. Enter a customer ID
2. Have a conversation with the agent
3. Click "View Memory Info" in the sidebar
4. See all stored memories for that customer

## Example Conversation

**Customer:** "When will my order arrive?"

**Agent:** (Uses memory to find order details and provides personalized response)

**Customer:** "Can I change the shipping address?"

**Agent:** (Remembers the order and helps update shipping)
