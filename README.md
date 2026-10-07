# Customer Support Agent Prototype

A beginner-friendly agent prototype inspired by e-commerce/printing customer support.

## What it does

The agent receives a customer request, decides what action is needed, calls a small tool, and returns an answer or escalates the request to a human.

### Tools

- `lookup_order()` - checks an order status
- `search_faq()` - searches a small FAQ knowledge base
- `escalate_to_human()` - escalates requests the agent cannot confidently handle

### Example

```text
Customer: Where is my order SM1002?
Agent: Order SM1002 is currently Shipped. It is for Custom labels and the estimated date is October 9.
```

```text
Customer: I want my money back
Agent: Refund requests are reviewed by the support team based on the order status.
```

```text
Customer: I have a complicated problem
Agent: ESCALATED: I could not confidently determine how to solve this request.
```

## Run locally

Python 3 is required.

```bash
python app.py
```

No API key or paid service is required.

## Why I built it

This project demonstrates the basic agent pattern:

**User request → decision → tool use → response/escalation**

A future version could connect the tools to real APIs, a database, an LLM, and an order-management system.
