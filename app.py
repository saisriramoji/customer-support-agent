
"""
Sticker Mule-style Customer Support Agent
A beginner-friendly agent prototype.

The agent:
1. Understands a customer request using simple intent detection.
2. Calls a relevant tool (order lookup, shipping lookup, FAQ).
3. Decides whether it can answer or should escalate to a human.
"""

ORDERS = {
    "SM1001": {"status": "In production", "product": "Custom stickers", "eta": "October 10"},
    "SM1002": {"status": "Shipped", "product": "Custom labels", "eta": "October 9"},
    "SM1003": {"status": "Delivered", "product": "Custom magnets", "eta": "October 5"},
}

FAQ = {
    "refund": "Refund requests are reviewed by the support team based on the order status.",
    "shipping": "Shipping time depends on the product, production time, and delivery method.",
    "artwork": "Artwork should be high quality and match the required dimensions and file format.",
}


# -------- Tools the agent can use --------

def lookup_order(order_id):
    """Tool: look up an order."""
    return ORDERS.get(order_id.upper())


def search_faq(topic):
    """Tool: search a small FAQ knowledge base."""
    return FAQ.get(topic.lower())


def escalate_to_human(reason):
    """Tool: create a human-support escalation."""
    return f"ESCALATED: {reason}"


# -------- Agent logic --------

def find_order_id(message):
    """Find an order ID such as SM1001 in the message."""
    words = message.upper().replace(",", " ").replace(".", " ").split()
    for word in words:
        if word.startswith("SM") and word[2:].isdigit():
            return word
    return None


def support_agent(message):
    """
    Main agent loop:
    observe -> decide -> use a tool -> respond
    """
    text = message.lower()
    order_id = find_order_id(message)

    # Decision 1: order status
    if order_id and any(word in text for word in ["order", "status", "where", "track", "shipping"]):
        order = lookup_order(order_id)

        if not order:
            return escalate_to_human(f"Order {order_id} was not found.")

        return (
            f"Order {order_id} is currently **{order['status']}**. "
            f"It is for {order['product']} and the estimated date is {order['eta']}."
        )

    # Decision 2: common FAQ questions
    if "refund" in text or "money back" in text:
        answer = search_faq("refund")
        return answer

    if "ship" in text or "delivery" in text:
        answer = search_faq("shipping")
        return answer

    if "artwork" in text or "file" in text or "design" in text:
        answer = search_faq("artwork")
        return answer

    # Decision 3: uncertain request -> human
    return escalate_to_human(
        "I could not confidently determine how to solve this request."
    )


if __name__ == "__main__":
    print("=" * 55)
    print("Sticker Mule Customer Support Agent")
    print("Type 'quit' to exit.")
    print("=" * 55)

    while True:
        user_message = input("\nCustomer: ")

        if user_message.lower() == "quit":
            print("Agent: Goodbye!")
            break

        print("Agent:", support_agent(user_message))
