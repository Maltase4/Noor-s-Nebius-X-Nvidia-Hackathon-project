import streamlit as st
import base64
from ai_client import ask_ai
from memory import save_recycled_item, get_stats
from tools import lookup_local_rule, web_search

# Page Configuration
st.set_page_config(page_title="Personal Recycling Assistant", page_icon="🌱", layout="centered")

st.title("🌱 Personal Recycling Assistant")
st.caption("Powered by NVIDIA Models & Nebius Cloud | Personal AI Track")

# Sidebar - Display Memory and Explicit Logging Button
with st.sidebar:
    st.header("📊 Personal Memory")
    total_items = get_stats()
    st.metric(label="Total Items Logged", value=total_items)
    
    st.divider()
    
    # --- EXPLICIT LOGGING SECTION ---
    st.subheader("📝 Log Recycled Item")
    item_to_log = st.text_input("What did you recycle or dispose of?", placeholder="e.g., Cardboard box")
    
    if st.button("Log Item"):
        if item_to_log.strip():
            save_recycled_item(item_to_log)
            st.success(f"Successfully logged: {item_to_log}!")
            st.rerun()
        else:
            st.warning("Please type an item name before logging.")
            
    st.caption("Logging your recycled/disposed items would help the model perform better")
    # ------------------------------------
    
    st.divider()

    # --- WEB SEARCH TOGGLE ---
    st.subheader("🌐 Web Search")
    use_web_search = st.toggle("Enable Tavily web search", value=True)
    st.caption("Fetches up-to-date recycling info from the web for each question.")
    # -------------------------
    
    st.divider()
    st.subheader("💡 Instructions")
    st.write("• Upload a photo of an item to scan it.")
    st.write("• Ask questions about local recycling guidelines.")

# Initialize Chat Memory in Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": (
                "You are a helpful, eco-friendly Personal Recycling Assistant. "
                "Provide clear, direct advice on how to recycle items, offer sustainable alternatives, "
                "and help users track their waste. Each user message may include local guideline data "
                "and web search results. Use them when relevant, and mention source URLs when you rely "
                "on web results. If the sources conflict with the local guidelines, say so."
            )
        }
    ]

# Render Chat History
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            if isinstance(msg["content"], list):
                for item in msg["content"]:
                    if item.get("type") == "text":
                        st.markdown(item["text"])
                    elif item.get("type") == "image_url":
                        st.image(item["image_url"]["url"], caption="Uploaded Image", width=300)
            else:
                st.markdown(msg["content"])

# --- OPTIONAL IMAGE UPLOADER ---
uploaded_file = st.file_uploader("Upload a photo of an item to scan (optional):", type=["jpg", "jpeg", "png"])

# Chat Input Box
if prompt := st.chat_input("Ask how to recycle an item..."):
    
    content_payload = []
    
    # Process image if uploaded
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        base64_image = base64.b64encode(bytes_data).decode("utf-8")
        image_url = f"data:image/jpeg;base64,{base64_image}"
        
        content_payload.append({
            "type": "image_url",
            "image_url": {"url": image_url}
        })
    
    # Tool 1: local rule lookup
    tool_hint = lookup_local_rule(prompt)

    # Tool 2: Tavily web search (optional)
    web_context = ""
    if use_web_search:
        with st.spinner("Searching the web..."):
            web_context = web_search(prompt)

    enhanced_text = f"User query: {prompt}\n[Local Guideline Tool Data: {tool_hint}]"
    if web_context:
        enhanced_text += f"\n[Web Search Results (Tavily): {web_context}]"
    
    content_payload.append({
        "type": "text",
        "text": enhanced_text
    })

    # Render User Input in Streamlit UI
    with st.chat_message("user"):
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Image", width=300)
        st.markdown(prompt)

    # Save to session history
    st.session_state.messages.append({"role": "user", "content": content_payload})

    # Query Nebius AI
    with st.chat_message("assistant"):
        with st.spinner("Analyzing recycling guidelines..."):
            ai_reply = ask_ai(st.session_state.messages)
            st.markdown(ai_reply)

    # Append AI Response
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})